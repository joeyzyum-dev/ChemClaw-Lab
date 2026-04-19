SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chemicals (
    chemical_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    formula TEXT,
    location TEXT,
    amount REAL NOT NULL DEFAULT 0,
    unit TEXT NOT NULL,
    threshold REAL DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS instruments (
    instrument_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'available',
    location TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id TEXT PRIMARY KEY,
    instrument_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    project_id TEXT,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'confirmed',
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS inventory_transactions (
    transaction_id TEXT PRIMARY KEY,
    chemical_id TEXT NOT NULL,
    user_id TEXT,
    project_id TEXT,
    transaction_type TEXT NOT NULL,
    amount_delta REAL NOT NULL,
    unit TEXT NOT NULL,
    raw_text TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chemical_id) REFERENCES chemicals(chemical_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS experiment_events (
    event_id TEXT PRIMARY KEY,
    project_id TEXT,
    user_id TEXT,
    event_type TEXT NOT NULL,
    title TEXT NOT NULL,
    details TEXT,
    source_text TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
"""
