# 🎟 Ticketmaster Event Scraper

This is a Python project that scrapes event data from the Ticketmaster API. 
It allows users to search for upcoming events based on custom filters and save the results to CSV.

## 🚀 Features

- Interactive CLI for country, keyword, and result size.
- Integrates with Ticketmaster's Discovery API.
- Saves event data (name, date, time, venue, etc.) to CSV.
- Logging via Python's logging module.
- Exporter module for saving to disk.

## 🛠 Usage

1. **Install dependencies**

```bash
pip install -r req.txt
```

2. **Set up your Ticketmaster API Key**  
   Add your API key to `config.py`:

```python
API_KEY = 'your_api_key_here'
BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events.json'
```

3. **Run the scraper**

```bash
python main.py
```

Follow the CLI prompts to select country, keyword, and number of events to fetch.

## 📦 Output

Results will be saved to `data/ticketmaster_events.csv`.

## 📂 Project Structure

```
.
├── main.py
├── config.py
├── exporter.py
├── scraper/
│   └── scraper.py
├── data/
│   └── ticketmaster_events.csv
└── README.md
```

## 🧾 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
