# query Ticketmaster API for events in next 3 months
# query: classification: music, subgenre: rock and metal, location: DC and Baltimore, date: next 3 months
# extract event ID, event name, date, venue, city, and URL for each event

# build API query params
# make HTTP requests
# handle rate limits, non-200 responses, timeouts
# parse JSON response
# return list of events with relevant details

import requests
from datetime import datetime, timedelta
from src.config import Config

BASE_URL = "https://app.ticketmaster.com/discovery/v2/events.json"

def fetch_metal_events():
    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=Config.LOOKAHEAD_DAYS)

    params = {
        "apikey": Config.TICKETMASTER_API_KEY,
        "classificationName": "music",
        "keyword": Config.GENRE,
        "countryCode": Config.COUNTRY_CODE,
        "stateCode": ",".join(Config.STATE_FILTERS),
        "startDateTime": start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "endDateTime": end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "size": 100
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    events = []

    if "_embedded" not in data:
        return events
    
    for item in data["_embedded"]["events"]:
        events.append({
            "event_id": item["id"],
            "event_name": item["name"],
            "event_date": item["dates"]["start"].get("localDate", ""),
            "venue": item["_embedded"]["venues"][0]["name"],
            "city": item["_embedded"]["venues"][0]["city"]["name"],
            "url": item["url"]
        })

    return events
