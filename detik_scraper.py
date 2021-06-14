import requests
from bs4 import BeautifulSoup


html_doc = requests.get("https://www.detik.com/terpopuler")
print('html_doc.text, html_doc.parser')


def page():
    pass


soup = BeautifulSoup(html_doc.text, 'html.parser')
populer_area = soup.find(attrs={'class': 'grid-row no-gutter flex-between'})

titles = populer_area.findAll(attrs={'class': 'box__title'})
images = populer_area.findAll(attrs={'class': 'box__title'})

for image in images:
    print(image.find('a').find('img')['title'] )
    print(image.find('img')['title'])
    print(populer_area)
    print(titles)
