from __future__ import annotations

import argparse
import json
from pathlib import Path

from .db import connect, init_db
from .seed import seed_from_json

DEFAULT_DB = Path("demo_data/chemclaw_lab.db")
DEFAULT_SEED = Path("demo_data/lab_seed.json")


def cmd_init(args: argparse.Namespace) -> None:
    init_db(args.db)
    print(f"Initialized database at {args.db}")


def cmd_seed(args: argparse.Namespace) -> None:
    init_db(args.db)
    seed_from_json(args.db, args.seed)
    print(f"Seeded database from {args.seed} into {args.db}")


def cmd_status(args: argparse.Namespace) -> None:
    conn = connect(args.db)
    try:
        tables = {
            "users": "SELECT COUNT(*) FROM users",
            "projects": "SELECT COUNT(*) FROM projects",
            "chemicals": "SELECT COUNT(*) FROM chemicals",
            "instruments": "SELECT COUNT(*) FROM instruments",
            "bookings": "SELECT COUNT(*) FROM bookings",
            "inventory_transactions": "SELECT COUNT(*) FROM inventory_transactions",
            "experiment_events": "SELECT COUNT(*) FROM experiment_events",
        }
        out = {}
        for name, sql in tables.items():
            out[name] = conn.execute(sql).fetchone()[0]
        print(json.dumps(out, indent=2))
    finally:
        conn.close()


def cmd_list_chemicals(args: argparse.Namespace) -> None:
    conn = connect(args.db)
    try:
        rows = conn.execute(
            "SELECT chemical_id, name, formula, location, amount, unit, threshold FROM chemicals ORDER BY name"
        ).fetchall()
        for row in rows:
            low = " [LOW]" if row["amount"] <= row["threshold"] else ""
            print(f'{row["name"]} ({row["formula"] or "-"}) | {row["amount"]} {row["unit"]} | {row["location"]}{low}')
    finally:
        conn.close()


def cmd_list_bookings(args: argparse.Namespace) -> None:
    conn = connect(args.db)
    try:
        rows = conn.execute(
            """
            SELECT b.booking_id, i.name AS instrument_name, u.name AS user_name, p.name AS project_name,
                   b.start_time, b.end_time, b.status
            FROM bookings b
            JOIN instruments i ON i.instrument_id = b.instrument_id
            JOIN users u ON u.user_id = b.user_id
            LEFT JOIN projects p ON p.project_id = b.project_id
            ORDER BY b.start_time
            """
        ).fetchall()
        for row in rows:
            print(
                f'{row["instrument_name"]} | {row["start_time"]} -> {row["end_time"]} | '
                f'{row["user_name"]} | {row["project_name"] or "-"} | {row["status"]}'
            )
    finally:
        conn.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="chemclaw", description="ChemClaw-Lab minimal prototype CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init-db", help="Initialize the SQLite database")
    p_init.add_argument("--db", type=Path, default=DEFAULT_DB)
    p_init.set_defaults(func=cmd_init)

    p_seed = sub.add_parser("seed-demo", help="Seed the database with demo lab data")
    p_seed.add_argument("--db", type=Path, default=DEFAULT_DB)
    p_seed.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    p_seed.set_defaults(func=cmd_seed)

    p_status = sub.add_parser("status", help="Show demo database object counts")
    p_status.add_argument("--db", type=Path, default=DEFAULT_DB)
    p_status.set_defaults(func=cmd_status)

    p_chem = sub.add_parser("list-chemicals", help="List demo chemicals")
    p_chem.add_argument("--db", type=Path, default=DEFAULT_DB)
    p_chem.set_defaults(func=cmd_list_chemicals)

    p_book = sub.add_parser("list-bookings", help="List demo instrument bookings")
    p_book.add_argument("--db", type=Path, default=DEFAULT_DB)
    p_book.set_defaults(func=cmd_list_bookings)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
