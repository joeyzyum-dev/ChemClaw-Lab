from pathlib import Path
from chemclaw_lab.db import init_db, connect
from chemclaw_lab.seed import seed_from_json


def test_seed_smoke(tmp_path: Path):
    db_path = tmp_path / "lab.db"
    seed_path = Path("demo_data/lab_seed.json")

    init_db(db_path)
    seed_from_json(db_path, seed_path)

    conn = connect(db_path)
    try:
        chemical_count = conn.execute("SELECT COUNT(*) FROM chemicals").fetchone()[0]
        booking_count = conn.execute("SELECT COUNT(*) FROM bookings").fetchone()[0]
    finally:
        conn.close()

    assert chemical_count >= 3
    assert booking_count >= 2
