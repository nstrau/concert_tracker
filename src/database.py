# concert Table
# CREATE TABLE concert (
#     event_id TEXT PRIMARY KEY,
#     event_name TEXT NOT NULL,
#     event_date TEXT NOT NULL,
#     venue TEXT NOT NULL,
#     city TEXT NOT NULL,
#     price_range TEXT,
#     url TEXT NOT NULL,
#     first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# if event_id not in table, new concert, add into table
# if event_id in table, update last_seen timestamp

import sqlite3
from datetime import datetime
from src.config import Config

def initialize_db():
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            event_id TEXT PRIMARY KEY,
            event_name TEXT,
            event_date TEXT NOT NULL,
            venue TEXT,
            city TEXT,
            url TEXT,
            first_seen TEXT,
            last_checked TEXT
        )
    ''')

    conn.commit()
    conn.close()

def get_existing_event_ids():
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT event_id FROM concerts')
    rows = cursor.fetchall()

    conn.close()
    return set(row[0] for row in rows)


def insert_new_event(events):
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()

    now = datetime.utcnow().isoformat()
    for event in events:
        cursor.execute('''
            INSERT INTO concerts (
                event_id, event_name, event_date, venue, city, url, first_seen, last_checked
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            event['event_id'],
            event['event_name'],
            event['event_date'],
            event['venue'],
            event['city'],
            event['url'],
            now,
            now
        ))

    conn.commit()
    conn.close()

# def update_event_last_seen(event_id):
#     import sqlite3
#     conn = sqlite3.connect(Config.DB_PATH)
#     c = conn.cursor()
#     c.execute('''
#         UPDATE concert
#         SET last_seen = CURRENT_TIMESTAMP
#         WHERE event_id = ?
#     ''', (event_id,))
#     conn.commit()
#     conn.close()

# def get_new_events(event_ids):
#     existing_event_ids = get_existing_event_ids()
#     new_event_ids = set(event_ids) - existing_event_ids
#     return new_event_ids