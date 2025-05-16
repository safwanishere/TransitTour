import csv
import os

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