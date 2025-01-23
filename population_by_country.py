import requests
from bs4 import BeautifulSoup
import json

# URL of the World Population by Country page
URL = "https://www.worldometers.info/world-population/population-by-country/"

# Fetch the webpage content
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the population by country page!")
    html_content = response.text
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# List to store population data by country
population_data = []

# Find the table containing the population data
table = soup.find('table', id='example2')
if table:
    # Extract the table rows
    rows = table.find('tbody').find_all('tr')

    # Loop through each row and extract data
    for row in rows:
        columns = row.find_all('td')
        country_data = {
            'Country': columns[1].text.strip(),
            'Population': columns[2].text.strip(),
            'Yearly Change': columns[3].text.strip(),
            'Net Change': columns[4].text.strip(),
            'Density (P/Km²)': columns[5].text.strip(),
            'Land Area (Km²)': columns[6].text.strip(),
            'Migrants (net)': columns[7].text.strip(),
            'Fertility Rate': columns[8].text.strip(),
            'Median Age': columns[9].text.strip(),
            'Urban Pop %': columns[10].text.strip(),
            'World Share': columns[11].text.strip()
        }
        population_data.append(country_data)
else:
    print("Error: Could not find the population table.")

# Save the data to a JSON file
json_filename = 'population_by_country.json'
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(population_data, json_file, indent=4)
print(f"\nData saved to '{json_filename}'.")

# Save the data to a text file
text_filename = 'population_by_country.txt'
with open(text_filename, 'w', encoding='utf-8') as text_file:
    for country in population_data:
        text_file.write(f"Country: {country['Country']}\n")
        text_file.write(f"Population: {country['Population']}\n")
        text_file.write(f"Yearly Change: {country['Yearly Change']}\n")
        text_file.write(f"Net Change: {country['Net Change']}\n")
        text_file.write(f"Density (P/Km²): {country['Density (P/Km²)']}\n")
        text_file.write(f"Land Area (Km²): {country['Land Area (Km²)']}\n")
        text_file.write(f"Migrants (net): {country['Migrants (net)']}\n")
        text_file.write(f"Fertility Rate: {country['Fertility Rate']}\n")
        text_file.write(f"Median Age: {country['Median Age']}\n")
        text_file.write(f"Urban Pop %: {country['Urban Pop %']}\n")
        text_file.write(f"World Share: {country['World Share']}\n")
        text_file.write("\n")
print(f"Data saved to '{text_filename}'.")

# Print a sample of the scraped data
print("\nSample Data:")
for country in population_data[:5]:  # Print the first 5 countries
    print(country)
