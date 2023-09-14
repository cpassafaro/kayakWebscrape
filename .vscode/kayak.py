import requests 
from bs4 import BeautifulSoup

boatlist = [] 

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


def getBoats():
    # gettign boats for next adventure site
    allBoats = getBoatsFromNextAdventure(4)
    return allBoats
   

def getBoatsFromNextAdventure(pages):
    for x in range(0, pages):
        # print(x)
        url = 'https://www.nextadventure.net/shop/paddle/kayaks/whitewater-kayaks?p={page}'

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        boats = soup.find_all('div', {'class': 'product-item-details'})

        for item in boats:
            print(item)
            boat = {
            'title': item.find('a', {'class': 'product-item-link'}).text,
            'link': item.find('a', {'class': 'product-item-link'})['href'],
            'price': item.find('div', {'class': 'price-final_price'}).text if item.find('div', {'class': 'price-final_price'}) else '',
            }
            boatlist.append(boat)
    return
# for()
getBoats()
print(boatlist)

