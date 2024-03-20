import requests
from bs4 import BeautifulSoup
import csv

file = open("Fake_Python_Job_Scrap.csv", "w", newline="\n", encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(["Title", "Subtitle"])

url = 'https://realpython.github.io/fake-jobs/'

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id='ResultsContainer')
job_elements = results.find_all('div', class_='card-content')

for job_element in job_elements:
    title = job_element.find('h2', class_='title is-5').text
    subtitle = job_element.find('h3', class_="subtitle is-6 company").text
    file.write(title + ',' + subtitle+','+'\n')