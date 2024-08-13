import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    # Define the URL of the website you want to scrape
    url = 'http://books.toscrape.com/'

    # Send a GET request to fetch the raw HTML content
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the book items on the page
        books = soup.find_all('article', class_='product_pod')

        # Check if books were found
        if books:
            # Create a CSV file to store the data
            with open('books.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(['Title', 'Price', 'Rating'])

                # Loop through each book and extract the title, price, and rating
                for book in books:
                    # Extract the title of the book
                    title = book.h3.a['title']

                    # Extract the price of the book
                    price = book.find('p', class_='price_color').text

                    # Extract the rating of the book
                    rating = book.p['class'][1]

                    # Write the data to the CSV file
                    writer.writerow([title, price, rating])

            print("Data has been successfully written to 'books.csv'.")
        else:
            print("No books found on the page.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

if __name__ == "__main__":
    scrape_books()