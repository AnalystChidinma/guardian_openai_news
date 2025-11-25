import logging
import os

import pandas as pd
import requests

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.INFO)

BASE_URL = "https://content.guardianapis.com/search"
API_KEY = os.getenv("GUARDIAN_API_KEY")
all_articles = []


def guardian_api():
    """
   The function fetches OpenAI news from The Guardian API,
    handles pagination, normalizes JSON, and returns a DataFrame.
    """
    page = 1

    if API_KEY is None:
        raise ValueError("ERROR: GUARDIAN_API_KEY is missing")

    params = {
        "api-key": API_KEY,
        "q": "OpenAI",
        "page-size": 50,
        "from-date": "2025-01-01",
        "to-date": "2025-01-30",
        "page": page
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")

    raw_response = response.json()
    total_pages = raw_response["response"].get("pages", 1)

    logging.info(f"Total pages found: {total_pages}")
    while page <= total_pages:
        logging.info(f"Fetching page {page}...")
        params["page"] = page
        response = requests.get(BASE_URL, params=params)

        data = response.json()
        results = data["response"]["results"]
        all_articles.extend(results)
        page += 1

    logging.info(f"Finished! Total articles fetched: {len(all_articles)}")

    df = pd.json_normalize(all_articles)
    df.to_json("guardian_openai_news.json", orient="records", indent=4)
    logging.info("Normalized dataset saved as guardian_openai_news.json")

    return df


if __name__ == "__main__":

    guardian_api()
