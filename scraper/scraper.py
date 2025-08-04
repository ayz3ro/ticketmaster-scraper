import requests
import logging


def get_event_info(base_url, params) -> list[dict]:
    logging.info("Sending request to Ticketmaster API...")

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        logging.error(f"API request failed: {response.status_code} - {response.text}")
        return []

    data = response.json()
    events = data.get('_embedded', {}).get('events', [])

    if not events:
        logging.warning("No events found for the given criteria.")
        return []

    results = []
    for event in events:
        event_data = {
            "event_name": event.get('name'),
            "event_date": event['dates']['start'].get('localDate'),
            "event_time": event['dates']['start'].get('localTime'),
            "status": event['dates']['status'].get('code'),
            "event_url": event.get('url'),
            "segment": None,
            "genre": None,
            "venue_name": None,
            "venue_city": None
        }

        classifications = event.get('classifications', [{}])[0]
        event_data["segment"] = classifications.get('segment', {}).get('name')
        event_data["genre"] = classifications.get('genre', {}).get('name')

        venues = event.get('_embedded', {}).get('venues', [])
        if venues:
            venue = venues[0]
            event_data["venue_name"] = venue.get('name')
            event_data["venue_city"] = venue.get('city', {}).get('name')

        results.append(event_data)

    logging.info(f"Parsed {len(results)} events.")
    return results