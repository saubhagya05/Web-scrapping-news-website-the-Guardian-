# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import json  # Import for handling JSON files

# URL of the books website
URL = "http://books.toscrape.com/"

# Fetch the webpage content
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the books page!")
    html_content = response.text
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all book elements on the page
book_elements = soup.find_all('article', class_='product_pod')

# Extract details of each book
books = []
for book_element in book_elements:
    title = book_element.h3.a['title']  # Book title
    price = book_element.find('p', class_='price_color').text  # Price
    availability = book_element.find('p', class_='instock availability').text.strip()  # Availability
    
    # Append the extracted details to the list
    books.append({'Title': title, 'Price': price, 'Availability': availability})

# Display the extracted book details
print("\nBooks:")
for i, book in enumerate(books, start=1):
    print(f"{i}. {book['Title']} - Price: {book['Price']}, Availability: {book['Availability']}")

# Save the data into a .txt file
with open('books.txt', 'w', encoding='utf-8') as txt_file:
    for book in books:
        txt_file.write(f"Title: {book['Title']}\n")
        txt_file.write(f"Price: {book['Price']}\n")
        txt_file.write(f"Availability: {book['Availability']}\n")
        txt_file.write("\n")

print("\nData saved to 'books.txt'.")

# Save the data into a .json file
with open('books.json', 'w', encoding='utf-8') as json_file:
    json.dump(books, json_file, indent=4)
    
print("Data saved to 'books.json'.")
