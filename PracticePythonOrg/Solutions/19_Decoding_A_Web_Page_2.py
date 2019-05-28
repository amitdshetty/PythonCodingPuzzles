from bs4 import BeautifulSoup
import requests

def main():
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    #print(soup)
    for text in soup.find_all('p'):
        print(str(text.getText()))

if __name__ == '__main__':
    main()