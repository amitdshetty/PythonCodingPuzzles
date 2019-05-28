import requests
from bs4 import BeautifulSoup
"""
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, 
use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.
"""

file_location = '/Users/amitshetty/Desktop/'

def writeThisToFile(text_to_write, file_name):
    f = open(file_location + file_name +'.txt','a')
    try:
        f.write(text_to_write)
        f.write("\n")
    except IOError as ie:
        print('There has been an exception :\n')
        print(ie)
    finally:
        f.close()

def main():
    url = 'https://www.marketwatch.com/'
    file_name = input('Enter the name of the file you would like to save the web page data\n') or 'Market_Watch_Data'
    crawl_the_page(url, file_name)


def crawl_the_page(url, file_name):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    all_symbols = soup.findAll("td", class_='table__cell symbol')
    all_prices = soup.findAll("td", class_='table__cell price')
    all_change = soup.findAll("td", class_='table__cell price')
    all_percent = soup.findAll("td", class_='table__cell change')
    for i in range(len(all_symbols)):
        writeThisToFile(str(all_symbols[i].text).strip() + " | " + str(all_prices[i].text).strip() + " | " + str(
            all_change[i].text).strip() + " | " + str(all_percent[i].text).strip(), file_name)
    print('File is available on {}/{}.txt'.format(file_location, file_name))


if __name__ == '__main__':
    main()