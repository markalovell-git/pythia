from datetime import date

import pytest

from app.backend.diary_import import parse_diary_xml


def _event(entry_date="2 Feb 1991", extra="", description="A day."):
    return (
        "<vt:diary_event>\n"
        "<vt:category>|landmark|travel|</vt:category>\n"
        f"<vt:date>{entry_date}</vt:date>\n"
        "<vt:location>Dallas</vt:location>\n"
        f"{extra}"
        f"<vt:description>{description}</vt:description>\n"
        "</vt:diary_event>\n"
    )


class TestParseDiaryXml:
    @pytest.mark.parametrize("raw,expected", [
        ("2 Feb 1991", date(1991, 2, 2)),
        ("07 December 2025", date(2025, 12, 7)),
        ("06 Dec, 2025", date(2025, 12, 6)),
        ("4 October, 2025", date(2025, 10, 4)),
        ("Feb 27 2019", date(2019, 2, 27)),
        ("Oct 14, 2025", date(2025, 10, 14)),
        ("April 25, 2025", date(2025, 4, 25)),
        ("May 1 2016", date(2016, 5, 1)),
        ("28 Sept 2019", date(2019, 9, 28)),
        ("Sept 1 2020", date(2020, 9, 1)),
        ("6 September 2025", date(2025, 9, 6)),
        ("16 april 2019", date(2019, 4, 16)),
        ("18 sep 2019", date(2019, 9, 18)),
    ])
    def test_full_date_formats(self, raw, expected):
        entry = parse_diary_xml(_event(raw))[0]
        assert entry.entry_date == expected
        assert entry.month_only is False

    @pytest.mark.parametrize("raw,expected", [
        ("Jun 1992", date(1992, 6, 1)),
        ("April 2017", date(2017, 4, 1)),
    ])
    def test_month_only_becomes_first_of_month(self, raw, expected):
        entry = parse_diary_xml(_event(raw))[0]
        assert entry.entry_date == expected
        assert entry.month_only is True

    @pytest.mark.parametrize("raw,expected", [
        ("3:00pm", "15:00"),
        ("12:30am", "00:30"),
        ("12:30pm", "12:30"),
        ("9:05", "09:05"),
        ("00:00", "00:00"),
        ("2h", "12:01"),
        ("25:00", "12:01"),
        ("13:00pm", "12:01"),
    ])
    def test_time_normalised(self, raw, expected):
        entry = parse_diary_xml(_event(extra=f"<vt:time>{raw}</vt:time>\n"))[0]
        assert entry.entry_time == expected

    def test_missing_time_gets_default(self):
        assert parse_diary_xml(_event())[0].entry_time == "12:01"

    def test_bare_ampersand_is_repaired_but_entities_survive(self):
        entry = parse_diary_xml(_event(description="Tracey & Steve &amp; Joe &W"))[0]
        assert entry.content == "Tracey & Steve & Joe &W"

    def test_all_fields_mapped(self):
        entry = parse_diary_xml(_event(extra=(
            "<vt:destination>Toronto</vt:destination>\n"
            "<vt:title>The title</vt:title>\n"
            "<vt:visuals>Red beret</vt:visuals>\n"
            "<vt:segment_start>\n<vt:color>255,0,0</vt:color>\n</vt:segment_start>\n"
        )))[0]
        assert entry.categories == "|landmark|travel|"
        assert entry.location == "Dallas"
        assert entry.destination == "Toronto"
        assert entry.title == "The title"
        assert entry.visual_cues == "Red beret"
        assert entry.segment_start is True
        assert entry.segment_color == "255,0,0"

    def test_optional_fields_absent(self):
        entry = parse_diary_xml(_event())[0]
        assert entry.title is None
        assert entry.visual_cues is None
        assert entry.destination is None
        assert entry.segment_start is False
        assert entry.segment_color is None

    def test_multiline_content_keeps_inner_newlines(self):
        entry = parse_diary_xml(_event(description="\nFirst.\nSecond.\n"))[0]
        assert entry.content == "First.\nSecond."

    def test_bad_date_names_the_entry(self):
        with pytest.raises(ValueError, match=r"Entry 2.*sometime"):
            parse_diary_xml(_event() + _event("sometime"))

    def test_missing_date_rejected(self):
        with pytest.raises(ValueError, match="Entry 1"):
            parse_diary_xml("<vt:diary_event><vt:description>x</vt:description></vt:diary_event>")

    @pytest.mark.parametrize("text", ["", "just some text", "<other>x</other>"])
    def test_no_entries_rejected(self, text):
        with pytest.raises(ValueError, match="No diary entries"):
            parse_diary_xml(text)

    def test_malformed_xml_rejected(self):
        with pytest.raises(ValueError, match="Not a valid"):
            parse_diary_xml("<vt:diary_event><vt:date>2 Feb 1991")


def _import(client, user_id, xml):
    return client.post(f"/api/import_diary/{user_id}", json={"xml": xml})


def _entries(client, user_id):
    return client.get(f"/api/get_diary_entries/{user_id}").json()


def _create_entry(client, user_id, content="Existing"):
    resp = client.post(
        f"/api/create_diary_entry/{user_id}",
        json={"entry_date": "2000-01-01", "content": content},
    )
    assert resp.status_code == 200


class TestImportEndpoint:
    def test_replaces_existing_entries(self, client, created_user):
        _create_entry(client, created_user, "old one")
        _create_entry(client, created_user, "old two")
        resp = _import(client, created_user, _event(description="new"))
        assert resp.status_code == 200
        assert resp.json() == {"deleted": 2, "imported": 1, "month_only_dates": 0}
        assert [e["content"] for e in _entries(client, created_user)] == ["new"]

    def test_other_users_entries_untouched(self, client, created_user):
        other = client.post("/api/submit_user_data", json={
            "username": "other",
            "name": "Other Person",
            "birth_datetime": "1985-01-01T12:00:00",
            "birth_timezone": "America/Chicago",
            "birth_location": "Chicago, IL",
            "birth_lat": 41.8781,
            "birth_lon": -87.6298,
        }).json()["user_id"]
        _create_entry(client, other, "theirs")
        assert _import(client, created_user, _event()).status_code == 200
        assert [e["content"] for e in _entries(client, other)] == ["theirs"]

    @pytest.mark.parametrize("bad", [
        "",
        "<vt:diary_event><vt:date>2 Feb 1991",
        _event() + _event("sometime"),
    ])
    def test_bad_file_leaves_existing_entries_intact(self, client, created_user, bad):
        _create_entry(client, created_user)
        resp = _import(client, created_user, bad)
        assert resp.status_code == 422
        assert [e["content"] for e in _entries(client, created_user)] == ["Existing"]

    def test_unknown_user_404(self, client):
        assert _import(client, "nobody", _event()).status_code == 404

    def test_same_day_entries_keep_file_order(self, client, created_user):
        xml = "".join(_event(description=f"entry {i}") for i in range(5))
        assert _import(client, created_user, xml).status_code == 200
        assert [e["content"] for e in _entries(client, created_user)] == [
            f"entry {i}" for i in range(5)
        ]

    def test_locations_reused_case_insensitively(self, client, created_user):
        existing = client.post("/api/locations", json={"name": "DALLAS"}).json()
        xml = _event() + _event(extra="<vt:destination>Toronto</vt:destination>\n")
        assert _import(client, created_user, xml).status_code == 200
        entries = _entries(client, created_user)
        assert {e["location_id"] for e in entries} == {existing["location_id"]}
        assert entries[0]["location_name"] == "DALLAS"
        assert entries[1]["destination_name"] == "Toronto"

    def test_categories_and_segment_round_trip(self, client, created_user):
        xml = _event(extra="<vt:segment_start><vt:color>1,2,3</vt:color></vt:segment_start>\n")
        assert _import(client, created_user, xml).status_code == 200
        entry = _entries(client, created_user)[0]
        assert entry["categories"] == ["landmark", "travel"]
        assert entry["segment_start"] is True
        assert entry["segment_color"] == "1,2,3"

    def test_month_only_count_reported(self, client, created_user):
        resp = _import(client, created_user, _event("Jun 1992") + _event())
        assert resp.json()["month_only_dates"] == 1

    def test_reimport_gives_same_count(self, client, created_user):
        xml = _event() + _event("Jun 1992")
        _import(client, created_user, xml)
        resp = _import(client, created_user, xml)
        assert resp.json()["deleted"] == 2
        assert len(_entries(client, created_user)) == 2


def _export(client, user_id):
    resp = client.get(f"/api/export_diary/{user_id}")
    assert resp.status_code == 200
    return resp.json()


_COMPARED_FIELDS = (
    "entry_date", "entry_time", "content", "title", "visual_cues", "categories",
    "location_name", "destination_name", "segment_start", "segment_color",
)


def _comparable(client, user_id):
    return [{f: e[f] for f in _COMPARED_FIELDS} for e in _entries(client, user_id)]


class TestExportEndpoint:
    def test_round_trip_preserves_every_field(self, client, created_user):
        full = _event(extra=(
            "<vt:time>3:00pm</vt:time>\n"
            "<vt:destination>Toronto</vt:destination>\n"
            "<vt:title>Tracey &amp; Steve &lt;party&gt;</vt:title>\n"
            "<vt:visuals>Red beret</vt:visuals>\n"
            "<vt:segment_start>\n<vt:color>255,0,0</vt:color>\n</vt:segment_start>\n"
        ), description="Line one.\nLine two &amp; more.")
        _import(client, created_user, full + _event("Jun 1992") + _event(description="third"))
        before = _comparable(client, created_user)

        exported = _export(client, created_user)
        assert exported["exported"] == 3
        assert exported["username"] == "jdoe"
        assert _import(client, created_user, exported["xml"]).status_code == 200
        assert _comparable(client, created_user) == before

    def test_output_matches_legacy_shape(self, client, created_user):
        _import(client, created_user, _event())
        xml = _export(client, created_user)["xml"]
        assert xml.startswith("<vt:diary_event>\n<vt:category>|landmark|travel|</vt:category>\n")
        assert "<vt:date>2 Feb 1991</vt:date>" in xml
        assert "<?xml" not in xml

    def test_segment_without_color_and_empty_content_round_trip(self, client, created_user):
        client.post(f"/api/create_diary_entry/{created_user}", json={
            "entry_date": "2000-01-01", "content": "", "segment_start": True,
        })
        before = _comparable(client, created_user)
        xml = _export(client, created_user)["xml"]
        assert _import(client, created_user, xml).status_code == 200
        assert _comparable(client, created_user)[0]["segment_start"] is True
        assert _comparable(client, created_user)[0]["content"] == before[0]["content"]

    def test_characters_invalid_in_xml_are_dropped(self, client, created_user):
        _create_entry(client, created_user, "bad\x0bchar")
        xml = _export(client, created_user)["xml"]
        assert _import(client, created_user, xml).status_code == 200
        assert _entries(client, created_user)[0]["content"] == "badchar"

    def test_only_this_users_entries_exported(self, client, created_user):
        other = client.post("/api/submit_user_data", json={
            "username": "other",
            "name": "Other Person",
            "birth_datetime": "1985-01-01T12:00:00",
            "birth_timezone": "America/Chicago",
            "birth_location": "Chicago, IL",
            "birth_lat": 41.8781,
            "birth_lon": -87.6298,
        }).json()["user_id"]
        _create_entry(client, other, "theirs")
        _create_entry(client, created_user, "mine")
        xml = _export(client, created_user)["xml"]
        assert "mine" in xml and "theirs" not in xml

    def test_empty_diary_exports_nothing(self, client, created_user):
        assert _export(client, created_user)["exported"] == 0

    def test_unknown_user_404(self, client):
        assert client.get("/api/export_diary/nobody").status_code == 404
