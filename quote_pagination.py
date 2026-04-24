import requests
from bs4 import BeautifulSoup
import csv

rows = []
page_num = 1

while True:
    url = f"https://quotes.toscrape.com/page/{page_num}/"
    
    print(f"Current scraping URL: {url}")
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("div", class_="quote")
    
    if not quotes:
        print("No more quotes found.")
        print(f"Total pages scraped: {page_num-1}")
        break
    
    for tag in quotes:
        quote = tag.find(
            "span",
            class_="text"
        ).text.strip()
        
        author = tag.find(
            "small",
            class_="author"
        ).text.strip()
        
        tag_list = [
            t.text for t in tag.find_all(
                "a",
                class_="tag"
            )
        ]
        
        tags = ", ".join(tag_list)
        
        row = {
            "Quote": quote,
            "Author": author,
            "Tags": tags
        }
        
        rows.append(row)
    
    page_num += 1
    
print("Writing data to CSV file...")

with open(
    "quotes_pagination_data.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Quote",
            "Author",
            "Tags"
        ]
    )
    
    writer.writeheader()
    writer.writerows(rows)

print("CSV file has been written!")