# Quotes Pagination Scraper

This project is a Python web scraping script that extracts quotes, authors, and tags from multiple pages of the website:

https://quotes.toscrape.com

The script automatically navigates through all available pages and collects data from each page.

---

## Features

- Pagination scraping
- Extracts quote text
- Extracts author names
- Extracts tags
- Automatically detects last page
- Saves all data into CSV format

---

## Tools Used

- Python
- Requests
- BeautifulSoup
- CSV Module

---

## Pagination Logic

The script automatically loops through pages:

Page 1 → Page 2 → Page 3 → ... → Last Page

It stops when no more quotes are found.

---

## Output

The script generates a CSV file:

quotes_pagination_data.csv

Example Output:

Quote | Author | Tags

"Life is what happens..." | John Lennon | life, inspiration

---

## How to Run

Install required libraries:

pip install requests beautifulsoup4

Run the script:

python quotes_pagination_scraper.py

---

## Project Purpose

This project was created to practice pagination scraping and structured data extraction using Python.

It demonstrates how to scrape data from multiple pages automatically.
