# concert Table
CREATE TABLE concert (
    event_id TEXT PRIMARY KEY,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    venue TEXT NOT NULL,
    city TEXT NOT NULL,
    url TEXT NOT NULL,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);