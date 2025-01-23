import requests
from bs4 import BeautifulSoup
import json

def scrape_guardian_rss():
    # URL for The Guardian's main RSS feed
    url = "https://www.theguardian.com/uk/rss"
    
    # Send an HTTP GET request to fetch the RSS feed
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse the RSS feed
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')

    # List to store news data
    news_list = []

    # Loop through each <item> in the RSS feed
    for item in items:
        title = item.title.text  # Extract the headline
        link = item.link.text  # Extract the article link
        pub_date = item.pubDate.text  # Extract the publication date

        news_list.append({
            'Title': title,
            'Link': link,
            'Publication Date': pub_date
        })

    return news_list

def save_to_json(data, filename):
    # Save the scraped data to a JSON file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename} (JSON)")

def save_to_text(data, filename):
    # Save the scraped data to a plain text file
    with open(filename, 'w', encoding='utf-8') as file:
        for news in data:
            file.write(f"Title: {news['Title']}\n")
            file.write(f"Link: {news['Link']}\n")
            file.write(f"Publication Date: {news['Publication Date']}\n")
            file.write("\n")  # Add a blank line between news items
    print(f"Data saved to {filename} (Text)")

# Scrape The Guardian RSS feed
news_data = scrape_guardian_rss()

# Save the data to both JSON and text files
save_to_json(news_data, 'guardian_news.json')
save_to_text(news_data, 'guardian_news.txt')

# Print the first 5 news items as a sample
print("\nSample News:")
for news in news_data[:5]:
    print(f"Title: {news['Title']}\nLink: {news['Link']}\nPublication Date: {news['Publication Date']}\n")
