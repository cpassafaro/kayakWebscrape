import requests
import re
from bs4 import BeautifulSoup

boatlist = [] 
tester = []
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


def getBoats():
    # gettign boats for next adventure site
    allBoats = getBoatsFromNextAdventure(4)
    return allBoats
   

def getBoatsFromNextAdventure(pages):
    for x in range(0, pages):
        url = 'https://www.nextadventure.net/shop/paddle/kayaks/whitewater-kayaks?p={page}'

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        boats = soup.find_all('div', {'class': 'product-item-info'})

        for item in boats:
            img = item.find('img', {'class': 'product-image-photo'})
            boat = {
            'title': item.find('a', {'class': 'product-item-link'}).text,
            'link': item.find('a', {'class': 'product-item-link'})['href'],
            'price': item.find('div', {'class': 'price-final_price'}).text if item.find('div', {'class': 'price-final_price'}) else '',
            'image': img['data-src'] if img['data-src'] else img['src'] 
            }
            boatlist.append(boat)
    return

def getBoatsFromColoradoKayak():
    url = 'https://coloradokayak.com/collections/whitewater-kayaks'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    mainboatarea = soup.find_all('div', {'class': 'card'})
    for pages in mainboatarea:
        header = pages.find('h1', {'class': 'heading'})
        # only shop all whitewater kayak is set up this way so we don't need more detailed statement
        if header:
            boats = pages.find_all('div', {'class': 'product-item'})
            for boat in boats:
                print(boat.find('button', {'class': 'product-item__action-button'}))
                boatObject = {
                    'title': boat.find('a', {'class': 'product-item__title'}).text,
                    'price': re.sub("\D", "", boat.find('span', {'class': 'price'}).text),
                    'url': url 
                }
                # print(boat)
                print('BREAK!!!')
    return

getBoatsFromColoradoKayak()
# getBoats()
# print(boatlist)

