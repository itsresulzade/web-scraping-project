```python
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.brainyquote.com/topics/scrape-quotes'

# Send HTTP request to the website
response = requests.get(url)

# If the page is successfully fetched
if response.status_code == 200:
    print("Page successfully fetched!")
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quotes on the page
    quotes = soup.find_all('span', class_='text')

    # Print the quotes
    print("\nQuotes:")
    for quote in quotes:
        print(f"- {quote.get_text()}")
else:
    print("Failed to fetch page. Error code:", response.status_code)
