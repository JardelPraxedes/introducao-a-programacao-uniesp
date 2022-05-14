import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('ArtistasLetraJ.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 9): #buscar em 9 páginas 
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anJ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()
    nomes_artistas_list = soup.find(class_='BodyText')
    nomes_artistas_list_items = nomes_artistas_list.find_all('a')

    for nomes_artistas in nomes_artistas_list_items:
        names = nomes_artistas.contents[0]
        links = 'https://web.archive.org' + nomes_artistas.get('href')
        f.writerow([names, links])