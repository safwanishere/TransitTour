import csv
import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_image_url(place):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.85 Safari/537.36"
        )
    }

    query = urllib.parse.quote_plus(place)
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Only find the first <img> tag
        first_img = soup.find("img")
        if first_img and first_img.get("src") and "http" in first_img["src"]:
            return first_img["src"]

    except Exception as e:
        print(f"Error fetching image for {place}: {e}")
        return None

print(get_image_url("charminar"))

def load_airports():
    airports = []
    csv_path = os.path.join(os.path.dirname(__file__), '../airports.csv')
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            airports.append({
                'iata': row['IATA'],
                'name': row['Name'],
                'Latitude': row['Latitude'],
                'Longitude': row['Longitude']
            })
    return airports



# def get_image_url(place_name):
#     url = "https://api.duckduckgo.com/"
#     params = {
#         "q": place_name,
#         "format": "json",
#         "t": "transittour",
#         "no_html": 1,
#         "skip_disambig": 1
#     }

#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         image_url = f"https://duckduckgo.com{data.get('Image')}"
#         return image_url if data.get('Image') else None
#     except Exception as e:
#         print(f"Error fetching image for {place_name}: {e}")
#         return None