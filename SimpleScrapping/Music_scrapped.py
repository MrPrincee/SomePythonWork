import requests
from bs4 import BeautifulSoup
import csv


file = open("Music_scrapped.csv", 'w', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(["Name", "Info"])

url = 'https://www.billboard.com/lists/best-songs-2023-so-far/taylor-swift-hits-different/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find('div', class_="a-content lrv-a-floated-parent lrv-a-glue-parent a-font-body-m")

result2 = result.find('div', class_='pmc-not-a-paywall')

result3 = result2.find('div', id='pmc-gallery-vertical')

result4 = result3.find('div', class_='c-gallery-vertical-loader u-gallery-app-shell-loader')

result5 = result4.find('article', class_='pmc-fallback-list-item')

result6 = result4.find_all('p', class_='paragraph larva // lrv-u-margin-lr-auto lrv-a-font-body-m')

result7 = result4.find_all('h2')

for i, j in zip(result7, result6):
    name = i.text
    info = j.text
    file.write('----'+name+'----'+info+':::'+'\n')