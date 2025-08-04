import logging
from datetime import datetime
from config import API_KEY, BASE_URL
from scraper.scraper import get_event_info
from scraper.exporter import save_to_csv

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

now_iso = datetime.utcnow().isoformat(timespec='seconds') + 'Z'

if __name__ == '__main__':
    logging.info("Ticketmaster Event Search CLI")

    country = input("Enter country code (default 'US'): ") or 'US'
    size = input("Number of events to fetch (default 20): ")
    keyword = input("Search keyword (optional): ")

    params = {
        'apikey': API_KEY,
        'size': int(size) if size else 20,
        'countryCode': country,
        'sort': 'date,asc',
        'startDateTime': now_iso,
        'includeTest': 'no'
    }

    if keyword:
        params['keyword'] = keyword

    events = get_event_info(BASE_URL, params)

    if events:
        save_to_csv(events, filename="ticketmaster_events.csv")