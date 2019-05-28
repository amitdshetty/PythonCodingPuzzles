import requests
from bs4 import BeautifulSoup
"""
Problem Statement (Web Scraping)
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage. (News website has become dynamic since problem creation.
Instead, creating a stock market ticker by pulling data from marketwatch(dot)com for the US market
"""
def main():
    url = 'https://www.marketwatch.com/'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,'html.parser')
    all_symbols = soup.findAll("td", class_='table__cell symbol')
    all_prices = soup.findAll("td", class_='table__cell price')
    all_change = soup.findAll("td", class_='table__cell price')
    all_percent = soup.findAll("td", class_='table__cell change')
    for i in range(len(all_symbols)):
        print(str(all_symbols[i].text).strip() + " | " + str(all_prices[i].text).strip() + " | " + str(all_change[i].text).strip() + " | " + str(all_percent[i].text).strip())

if __name__ == '__main__':
    main()
