# PRODIGY_SD-05
 Task - 5

 Create a program that extracts product information, such as names, prices, and ratings, from an online e- commerce website and stores the data in a structured format like a CSV file.You are free to choose the website you scrape from.


What does this program do?
  Extracts product data from an e-commerce site(here books site),storing it in a CSV format.

How does this program work?
1. Sending a Request: The program sends an HTTP GET request to the specified URL of the e-commerce website using the requests library.

2. Parsing the HTML: The HTML content of the webpage is parsed using BeautifulSoup to extract product(books) information such as names, prices, and ratings.

3. Storing Data: The scraped product(books) information is stored in a list of dictionaries.

4. Saving Data to CSV: The list of dictionaries is written to a CSV file (books.csv) using the csv module.
