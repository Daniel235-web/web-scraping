import csv
import requests
from bs4 import BeautifulSoup

# URL of the product page you want to scrape
url = "https://lonon-china.en.alibaba.com/"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "lxml")

# Find the elements containing the product information
product_name_element = soup.find("span", class_="title-con")
price_element = soup.find("div", class_="price")
description_element = soup.find("div", class_="do-entry do-entry-separate")
variant_element = soup.find("div", class_="item-last item-size")
link_elements = soup.find_all("a", class_="product-image")

# Extract the text from the elements
product_name = product_name_element.text.strip() if product_name_element else "N/A"
price = price_element.text.strip() if price_element else "N/A"
description = description_element.text.strip() if description_element else "N/A"
variant = variant_element.text.strip() if variant_element else "N/A"
links = [link['href'] for link in link_elements] if link_elements else []

# Create a list of dictionaries to store the extracted information
product_data = [
    {"Product Name": product_name, "Price": price, "Description": description, "Variant": variant, "Links": links}
]

# Define the CSV file path
csv_file = "product_data.csv"

# Write the extracted information to the CSV file
with open(csv_file, "w", newline="") as file:
    fieldnames = ["Product Name", "Price", "Description", "Variant", "Links"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(product_data)

print("Data has been saved in", csv_file)
