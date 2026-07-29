#!/usr/bin/env python3
"""Seed (or remove) a handful of fake diary entries for manual testing.

Exercises the arrow-navigation ordering in the Diary tab: entries spread
across more than a month, plus one day with three entries — some timed,
some not — so you can click through and confirm the order matches
`diary_model.order_entries` (date, then time-of-day, then entry order).

Two write modes:

  --via-api  (default when the app/backend is running on 127.0.0.1:8000)
      POSTs through the running backend. Use this while the app is open —
      it is the only mode guaranteed to hit the same database the running
      app has open, and it works from sandboxed shells whose filesystem
      writes get redirected away from the real data dir.

  --direct
      Opens the encrypted DB itself via SQLAlchemy. Use when the app is
      NOT running.

Usage:
    uv run python scripts/seed_diary.py --username Mark
    uv run python scripts/seed_diary.py --list-users
    uv run python scripts/seed_diary.py --username Mark --dry-run
    uv run python scripts/seed_diary.py --username Mark --remove
"""
import argparse
import sys
import uuid
from datetime import date, datetime, timedelta

import httpx

_BASE_URL = "http://127.0.0.1:8000/api"
_HEALTH_URL = "http://127.0.0.1:8000/health"  # health sits at the root, not under /api

# Fixed namespace -> deterministic entry_ids in --direct mode, so re-running
# replaces rather than duplicates. (The API assigns its own ids, so --via-api
# de-duplicates by title instead.)
_NAMESPACE = uuid.UUID("f11a7e3e-3a4d-4e0a-9a12-123456789abc")

# (days-after-base, entry_time or None, title, content)
_SEED = [
    (0,  "08:30", "Early start", "Up before the alarm, felt clear-headed."),
    (39, None,    "A day without hours", "No particular time attached to this one."),
    (59, "21:15", "Late thoughts", "Winding down, thinking back over the week."),
    (76, None,    "Woke unplaced", "First entry of the day, no time noted."),
    (76, "07:45", "Morning walk", "Walked the long way round; good light."),
    (76, "19:30", "Evening, three of three", "Third entry logged today, in the evening."),
]

_BASE_DATE = date(2026, 5, 4)
_SEED_TITLES = {title for _, _, title, _ in _SEED}


def _planned() -> list[tuple[date, str | None, str, str]]:
    return [
        (_BASE_DATE + timedelta(days=offset), entry_time, title, content)
        for offset, entry_time, title, content in _SEED
    ]


def _print_plan(rows, user_label: str, verb: str):
    print(f"{verb} {len(rows)} entries for {user_label}:")
    for entry_date, entry_time, title, _ in rows:
        print(f"  {entry_date}  {entry_time or '(no time)':>9}  {title}")


# ── API mode ─────────────────────────────────────────────────────────────────

def _api_available() -> bool:
    try:
        return httpx.get(_HEALTH_URL, timeout=2.0).status_code == 200
    except Exception:
        return False


def _api_users() -> list[dict]:
    return httpx.get(f"{_BASE_URL}/list_users", timeout=10.0).json()


def _api_resolve_user(users: list[dict], user_id: str | None, username: str | None) -> str:
    if user_id:
        return user_id
    if username:
        matches = [u for u in users if u["username"].lower() == username.lower()]
        if not matches:
            names = ", ".join(u["username"] for u in users) or "(none)"
            sys.exit(f"No user named {username!r}. Available: {names}")
        return matches[0]["user_id"]
    if not users:
        sys.exit("No users found — create a profile in the app first.")
    if len(users) > 1:
        options = "\n".join(f"  {u['user_id']}  ({u['username']})" for u in users)
        sys.exit(f"Multiple users found; pass --username or --user-id:\n{options}")
    return users[0]["user_id"]


def _api_clear_seeded(user_id: str) -> int:
    existing = httpx.get(f"{_BASE_URL}/get_diary_entries/{user_id}", timeout=10.0).json()
    removed = 0
    for entry in existing:
        if entry.get("title") in _SEED_TITLES:
            httpx.delete(f"{_BASE_URL}/delete_diary_entry/{entry['entry_id']}", timeout=10.0)
            removed += 1
    return removed


def _run_via_api(args):
    if not _api_available():
        sys.exit(
            "Backend not reachable at 127.0.0.1:8000.\n"
            "Start the app first, or use --direct if the app is not running."
        )
    users = _api_users()
    if args.list_users:
        for u in users:
            print(f"{u['user_id']}  {u['username']}")
        return

    user_id = _api_resolve_user(users, args.user_id, args.username)
    label = next((u["username"] for u in users if u["user_id"] == user_id), user_id)
    rows = _planned()

    if args.remove:
        if args.dry_run:
            print(f"Would delete seeded entries for {label}.")
            return
        print(f"Removed {_api_clear_seeded(user_id)} seeded diary entries for {label}.")
        return

    if args.dry_run:
        _print_plan(rows, label, "Would seed")
        return

    _api_clear_seeded(user_id)  # keeps re-runs idempotent
    for entry_date, entry_time, title, content in rows:
        resp = httpx.post(
            f"{_BASE_URL}/create_diary_entry/{user_id}",
            json={
                "entry_date": str(entry_date),
                "content": content,
                "title": title,
                "entry_time": entry_time,
                "categories": ["unsorted"],
            },
            timeout=10.0,
        )
        resp.raise_for_status()
    _print_plan(rows, label, "Seeded")


# ── Direct-DB mode ───────────────────────────────────────────────────────────

def _run_direct(args):
    from app.common.database import SessionLocal, init_db, DiaryEntry, UserData

    init_db()
    db = SessionLocal()
    try:
        users = db.query(UserData).all()
        if args.list_users:
            for u in users:
                print(f"{u.user_id}  {u.username}")
            return

        if args.user_id:
            user_id = args.user_id
        elif args.username:
            matches = [u for u in users if u.username.lower() == args.username.lower()]
            if not matches:
                names = ", ".join(u.username for u in users) or "(none)"
                sys.exit(f"No user named {args.username!r}. Available: {names}")
            user_id = matches[0].user_id
        elif not users:
            sys.exit("No users found — create a profile in the app first.")
        elif len(users) > 1:
            options = "\n".join(f"  {u.user_id}  ({u.username})" for u in users)
            sys.exit(f"Multiple users found; pass --username or --user-id:\n{options}")
        else:
            user_id = users[0].user_id

        label = next((u.username for u in users if u.user_id == user_id), user_id)
        rows = _planned()
        ids = [
            str(uuid.uuid5(_NAMESPACE, f"{d}:{t}:{title}"))
            for d, t, title, _ in rows
        ]

        if args.remove:
            if args.dry_run:
                print(f"Would delete {len(ids)} seeded entries for {label}.")
                return
            deleted = (
                db.query(DiaryEntry)
                .filter(DiaryEntry.entry_id.in_(ids))
                .delete(synchronize_session=False)
            )
            db.commit()
            print(f"Removed {deleted} seeded diary entries for {label}.")
            return

        if args.dry_run:
            _print_plan(rows, label, "Would seed")
            return

        base_created = datetime(2026, 7, 28, 9, 0, 0)
        for i, ((entry_date, entry_time, title, content), entry_id) in enumerate(zip(rows, ids)):
            created_at = base_created + timedelta(minutes=i)  # fixes insertion order
            db.merge(DiaryEntry(
                entry_id=entry_id,
                user_id=user_id,
                entry_date=entry_date,
                content=content,
                created_at=created_at,
                updated_at=created_at,
                title=title,
                categories="|unsorted|",
                entry_time=entry_time,
                segment_start=0,
            ))
        db.commit()
        _print_plan(rows, label, "Seeded")
    finally:
        db.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user-id", help="User to seed entries for")
    parser.add_argument("--username", help="User to seed entries for, by username")
    parser.add_argument("--list-users", action="store_true", help="List profiles and exit")
    parser.add_argument("--remove", action="store_true", help="Delete the seeded entries instead")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen, do nothing")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--via-api", action="store_true", help="Write through the running backend")
    mode.add_argument("--direct", action="store_true", help="Open the encrypted DB directly")
    args = parser.parse_args()

    if args.direct:
        _run_direct(args)
    elif args.via_api or _api_available():
        _run_via_api(args)
    else:
        _run_direct(args)


if __name__ == "__main__":
    main()
