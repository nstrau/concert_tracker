# orchestrate the pipeline: fetch events, process them, and send notifications

# initialize logging
# initialize database connection
# fetch events from API
# compare against DB
# insert new events
# if new events exist, send email
# log summary metrics: total events fetched, new events count, runtime

from src.logger import setup_logger
from src.database import initialize_db, get_existing_event_ids, insert_new_event
from src.fetch_events import fetch_metal_events
from src.notifier import send_email

def run_pipeline():
    logger = setup_logger()

    logger.info("initializing database connection")
    initialize_db()
    
    logger.info("fetching events from API")
    events = fetch_metal_events()

    existing_ids = get_existing_event_ids()

    new_events = [e for e in events if e['event_id'] not in existing_ids]

    logger.info(f"New events found: {len(new_events)}")

    if new_events:
        insert_new_event(new_events)
        send_email(new_events)
        logger.info("Notification email sent")
    else:
        logger.info("No new events to notify")
