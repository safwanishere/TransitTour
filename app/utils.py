import csv

def load_airports():
    airports = {}
    with open('airports.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            airports[row['IATA'].upper()] = {
                'name': row['Name'],
                'lat': float(row['Latitude']),
                'lon': float(row['Longitude'])
            }
    return airports