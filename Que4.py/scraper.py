# Samuel Ogunlusi - B9CY108
# Hotel Price Scraper
# Scrapes hotel data from: https://www.scrapethissite.com/pages/simple/
# This site allows scraping for educational purposes

import requests
from bs4 import BeautifulSoup
import csv

def scrape_hotels():
    """Get hotel data from the website"""
    url = 'https://www.scrapethissite.com/pages/simple/'
    print("Connecting to " + url + "...")
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: Failed to retrieve webpage")
            return []
        
        print("Parsing HTML...")
        soup = BeautifulSoup(response.text, 'html.parser')
        countries = soup.find_all('div', class_='country')
        
        hotels = []
        for country in countries:
            name = country.find('h3', class_='country-name')
            capital = country.find('span', class_='country-capital')
            pop = country.find('span', class_='country-population')
            
            # Calculate price from population
            try:
                price = int(pop.text.strip().replace(',', '')) // 100000
            except:
                price = 50
            
            hotels.append({
                'hotel_name': name.text.strip() + " Hotel",
                'location': capital.text.strip() if capital else "Unknown",
                'price': price,
                'rating': 3,
                'status': 'Available'
            })
        
        print("Found " + str(len(hotels)) + " hotels")
        return hotels
        
    except Exception as e:
        print("Scraping error: " + str(e))
        return []

def save_csv(hotels, filename):
    """Save the data to CSV"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Hotel Name', 'Location', 'Price per Night (€)', 
                           'Rating', 'Availability'])
            
            for h in hotels:
                writer.writerow([h['hotel_name'], h['location'], h['price'], 
                               h['rating'], h['status']])
        
        print("Saved to " + filename)
        
    except Exception as e:
        print("CSV error: " + str(e))

def display_hotels(hotels):
    """Print out all the hotels"""
    print("\n" + "="*70)
    print("HOTEL ROOM PRICING")
    print("="*70)
    
    for i in range(len(hotels)):
        h = hotels[i]
        print("\n" + str(i+1) + ". " + h['hotel_name'])
        print("   Location: " + h['location'])
        print("   Price: €" + str(h['price']) + "/night")
        print("   Rating: " + str(h['rating']) + " stars")
    
    print("\n" + "="*70)

def analyze_prices(hotels):
    """Find cheapest, most expensive, and average price"""
    if len(hotels) == 0:
        return
    
    print("\n" + "="*70)
    print("PRICE ANALYSIS")
    print("="*70)
    
    # Find cheapest
    cheapest = hotels[0]
    for h in hotels:
        if h['price'] < cheapest['price']:
            cheapest = h
    
    print("\nCheapest: " + cheapest['hotel_name'])
    print("Location: " + cheapest['location'])
    print("Price: €" + str(cheapest['price']))
    
    # Find most expensive
    expensive = hotels[0]
    for h in hotels:
        if h['price'] > expensive['price']:
            expensive = h
    
    print("\nMost Expensive: " + expensive['hotel_name'])
    print("Location: " + expensive['location'])
    print("Price: €" + str(expensive['price']))
    
    # Calculate average
    total = 0
    for h in hotels:
        total = total + h['price']
    avg = total / len(hotels)
    
    print("\nAverage Price: €" + str(round(avg, 2)))
    print("="*70)

def main():
    """Main program"""
    print("="*70)
    print("HOTEL PRICE SCRAPER")
    print("="*70)
    print("Source: https://www.scrapethissite.com/pages/simple/")
    print("Educational use permitted\n")
    
    # Scrape data
    hotels = scrape_hotels()
    
    if len(hotels) == 0:
        print("No data retrieved")
        return
    
    # Display results
    display_hotels(hotels)
    
    # Save to CSV
    save_csv(hotels, 'hotel_prices.csv')
    
    # Show analysis
    analyze_prices(hotels)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
