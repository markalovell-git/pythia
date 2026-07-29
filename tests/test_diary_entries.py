import uuid
from datetime import datetime, date

from tests.conftest import TestingSessionLocal
from app.common.database import DiaryEntry


def _create_entry(client, user_id, **overrides):
    payload = {
        "entry_date": "1991-02-02",
        "content": "A big day.",
        **overrides,
    }
    return client.post(f"/api/create_diary_entry/{user_id}", json=payload)


class TestDiaryEntries:
    def test_create_full_fields(self, client, created_user):
        loc = client.post("/api/locations", json={"name": "Richardson, TX"}).json()
        resp = _create_entry(
            client, created_user,
            title="Last performance of Damn Yankees",
            visual_cues="Red beret, red shirt, suspenders.",
            categories=["studies_and_arts", "landmark"],
            entry_time="19:00",
            location_id=loc["location_id"],
            segment_start=True,
            segment_color="255,0,0",
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["categories"] == ["studies_and_arts", "landmark"]
        assert data["title"] == "Last performance of Damn Yankees"
        assert data["visual_cues"] == "Red beret, red shirt, suspenders."
        assert data["entry_time"] == "19:00"
        assert data["location_name"] == "Richardson, TX"
        assert data["destination_id"] is None
        assert data["segment_start"] is True
        assert data["segment_color"] == "255,0,0"

    def test_create_defaults_to_unsorted(self, client, created_user):
        resp = _create_entry(client, created_user)
        assert resp.status_code == 200
        data = resp.json()
        assert data["categories"] == ["unsorted"]
        assert data["segment_start"] is False
        assert data["location_id"] is None

    def test_pipe_string_roundtrip_in_db(self, client, created_user):
        resp = _create_entry(client, created_user, categories=["family", "world"])
        entry_id = resp.json()["entry_id"]
        db = TestingSessionLocal()
        try:
            row = db.query(DiaryEntry).filter(DiaryEntry.entry_id == entry_id).one()
            assert row.categories == "|family|world|"
        finally:
            db.close()

    def test_unknown_slug_preserved(self, client, created_user):
        resp = _create_entry(client, created_user, categories=["travel"])
        assert resp.json()["categories"] == ["travel"]

    def test_legacy_row_serializes_with_defaults(self, client, created_user):
        # Simulate a row created before the structured-entry columns existed.
        db = TestingSessionLocal()
        try:
            now = datetime.utcnow()
            db.add(DiaryEntry(
                entry_id=str(uuid.uuid4()),
                user_id=created_user,
                entry_date=date(2026, 1, 1),
                content="Old-style plain entry",
                created_at=now,
                updated_at=now,
            ))
            db.commit()
        finally:
            db.close()
        resp = client.get(f"/api/get_diary_entries/{created_user}", params={"date": "2026-01-01"})
        [data] = resp.json()
        assert data["categories"] == ["unsorted"]
        assert data["title"] is None
        assert data["location_name"] is None
        assert data["segment_start"] is False

    def test_multiple_entries_per_day(self, client, created_user):
        _create_entry(client, created_user, title="Morning", entry_time="09:00")
        _create_entry(client, created_user, title="Evening", entry_time="21:00")
        resp = client.get(f"/api/get_diary_entries/{created_user}", params={"date": "1991-02-02"})
        titles = [e["title"] for e in resp.json()]
        assert titles == ["Morning", "Evening"]

    def test_update_partial_fields(self, client, created_user):
        entry_id = _create_entry(client, created_user, title="Before").json()["entry_id"]
        resp = client.put(f"/api/update_diary_entry/{entry_id}", json={
            "categories": ["outing"],
            "segment_start": True,
            "segment_color": "0,255,0",
        })
        data = resp.json()
        assert data["title"] == "Before"  # untouched
        assert data["categories"] == ["outing"]
        assert data["segment_start"] is True
        assert data["segment_color"] == "0,255,0"

    def test_global_ordering_across_days(self, client, created_user):
        # Unfiltered fetch (no ?date=) is what the arrow-navigation UI relies
        # on: date first, then time, then insertion order within a day.
        _create_entry(client, created_user, entry_date="2026-07-19", title="Evening", entry_time="19:30")
        _create_entry(client, created_user, entry_date="2026-05-04", title="Early start", entry_time="08:30")
        _create_entry(client, created_user, entry_date="2026-07-19", title="Woke unplaced", entry_time=None)
        _create_entry(client, created_user, entry_date="2026-06-12", title="A day without hours", entry_time=None)
        _create_entry(client, created_user, entry_date="2026-07-19", title="Morning walk", entry_time="07:45")
        _create_entry(client, created_user, entry_date="2026-07-02", title="Late thoughts", entry_time="21:15")

        resp = client.get(f"/api/get_diary_entries/{created_user}")
        titles = [e["title"] for e in resp.json()]
        assert titles == [
            "Early start",
            "A day without hours",
            "Late thoughts",
            "Woke unplaced",
            "Morning walk",
            "Evening",
        ]

    def test_diary_dates(self, client, created_user):
        _create_entry(client, created_user, entry_date="1991-02-02")
        _create_entry(client, created_user, entry_date="1991-02-02")
        _create_entry(client, created_user, entry_date="1992-03-03")
        resp = client.get(f"/api/diary_dates/{created_user}")
        assert sorted(resp.json()) == ["1991-02-02", "1992-03-03"]


class TestLocations:
    def test_create_and_search(self, client):
        client.post("/api/locations", json={
            "name": "Toronto, Canada", "latitude": 43.65, "longitude": -79.38,
            "timezone": "America/Toronto",
        })
        client.post("/api/locations", json={"name": "Richardson, TX"})
        resp = client.get("/api/locations", params={"q": "toronto"})
        [loc] = resp.json()
        assert loc["name"] == "Toronto, Canada"
        assert loc["timezone"] == "America/Toronto"
        assert len(client.get("/api/locations").json()) == 2

    def test_dedupe_case_insensitive(self, client):
        first = client.post("/api/locations", json={"name": "Richardson, TX"}).json()
        second = client.post("/api/locations", json={"name": "richardson, tx"}).json()
        assert second["location_id"] == first["location_id"]

    def test_dedupe_backfills_coords(self, client):
        name_only = client.post("/api/locations", json={"name": "Richardson, TX"}).json()
        assert name_only["latitude"] is None
        filled = client.post("/api/locations", json={
            "name": "Richardson, TX", "latitude": 32.95, "longitude": -96.73,
            "timezone": "America/Chicago",
        }).json()
        assert filled["location_id"] == name_only["location_id"]
        assert filled["latitude"] == 32.95
        assert filled["timezone"] == "America/Chicago"

    def test_update_location(self, client):
        loc = client.post("/api/locations", json={"name": "Somewhere"}).json()
        resp = client.put(f"/api/locations/{loc['location_id']}", json={
            "latitude": 1.0, "longitude": 2.0, "timezone": "UTC",
        })
        data = resp.json()
        assert data["latitude"] == 1.0
        assert data["timezone"] == "UTC"

    def test_blank_name_rejected(self, client):
        resp = client.post("/api/locations", json={"name": "   "})
        assert resp.status_code == 422
