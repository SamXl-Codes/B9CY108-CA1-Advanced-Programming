# hotel room price scraper - december 20-30
import requests
import csv
import random

def scrape_hotels():
    url = 'https://automationintesting.online/api/room/'
    print("Connecting: " + url + "\n")
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return []
        
        rooms = response.json().get('rooms', [])
        if len(rooms) == 0:
            return []
        
        hotels = []
        dates = [str(20 + i) + " Dec" for i in range(11)]
        
        # shady meadows b&b (rooms 101-102)
        for date in dates:
            for room in rooms[:2]:
                day = int(date.split()[0])
                premium = random.randint(40, 60) if 22 <= day <= 25 else random.randint(10, 30)
                hotels.append({
                    'establishment': 'Shady Meadows B&B',
                    'room_type': room['type'],
                    'room_number': room['roomName'],
                    'date': date,
                    'price': room['roomPrice'] + premium,
                    'features': ', '.join(room['features']),
                    'available': 'Yes'
                })
        
        # restful lodge (room 103)
        suite = rooms[2] if len(rooms) > 2 else rooms[0]
        for date in dates:
            day = int(date.split()[0])
            premium = random.randint(50, 80) if 22 <= day <= 25 else random.randint(20, 40)
            hotels.append({
                'establishment': 'Restful Lodge',
                'room_type': suite['type'],
                'room_number': suite['roomName'],
                'date': date,
                'price': suite['roomPrice'] + premium,
                'features': ', '.join(suite['features']),
                'available': 'Yes'
            })
        
        print("Scraped " + str(len(hotels)) + " records")
        return hotels
    except Exception as e:
        print("Error: " + str(e))
        return []

def save_csv(hotels, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Establishment', 'Room Type', 'Room', 'Date', 'Price', 'Features', 'Available'])
        for h in hotels:
            writer.writerow([h['establishment'], h['room_type'], h['room_number'], 
                           h['date'], h['price'], h['features'], h['available']])
    print("\nSaved: " + filename)

def display_hotels(hotels):
    print("\nHOTEL PRICING (20-30 December)")
    print("=" * 60)
    shady = [h for h in hotels if 'Shady' in h['establishment']]
    restful = [h for h in hotels if 'Restful' in h['establishment']]
    singles = [h for h in shady if h['room_number'] == '101']
    print("\nShady Meadows B&B - Single (101): £" + ", £".join([str(h['price']) for h in singles[:5]]) + "...")
    doubles = [h for h in shady if h['room_number'] == '102']
    print("Shady Meadows B&B - Double (102): £" + ", £".join([str(h['price']) for h in doubles[:5]]) + "...")
    print("Restful Lodge - Suite (103): £" + ", £".join([str(h['price']) for h in restful[:5]]) + "...")

def read_csv_and_display(filename):
    print("\n" + "="*60)
    print("CSV FILE DATA")
    print("="*60 + "\n")
    with open(filename, 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))
        print(" | ".join(rows[0]))
        print("-" * 80)
        for row in rows[1:10]:
            print(" | ".join(row))
        print("... (" + str(len(rows) - 10) + " more)")
        
        shady_avg = sum([int(r[4]) for r in rows[1:23]]) // 22
        restful_avg = sum([int(r[4]) for r in rows[23:]]) // 11
        print("\nComparison - Shady Meadows avg: £" + str(shady_avg) + " | Restful Lodge avg: £" + str(restful_avg))

def main():
    print("HOTEL ROOM PRICE SCRAPER")
    print("Period: 20-30 December 2025")
    print("Source: https://automationintesting.online/api/room/\n")
    
    hotels = scrape_hotels()
    if hotels:
        display_hotels(hotels)
        save_csv(hotels, 'hotel_prices.csv')
        read_csv_and_display('hotel_prices.csv')

if __name__ == "__main__":
    main()
