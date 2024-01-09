import requests
from bs4 import BeautifulSoup

url = 'https://www.bmw.de/de/neufahrzeuge.html'  # Replace with the actual URL of the BMW page containing car information

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting car information
cars = soup.find_all('div', class_='car-info')  # Adjust 'div' and 'car-info' to match the relevant HTML structure

for car in cars:
    print(car.text)  # This would print the text content of each car information block
