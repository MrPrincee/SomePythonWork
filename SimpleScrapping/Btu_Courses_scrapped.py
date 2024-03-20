import requests
from bs4 import BeautifulSoup
import csv

file = open('BTU_Courses.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['Undergrade', 'Master', 'PHD'])

url = 'https://btu.edu.ge/en/stsavla/programebi/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# undergrade programs

result = soup.find('div', class_='elementor-element elementor-element-0175b76'
                                 ' elementor-widget elementor-widget-text-editor')

result2 = result.find_all('div', class_='elementor-widget-container')

if result2:
    result3 = result2[0].find_all('h4')
else:
    result3 = None

# master program
result4 = soup.find('div',
                    class_='elementor-element elementor-element-b2c45ff elementor-widget elementor-widget-text-editor')

result5 = result4.find_all('div', class_='elementor-widget-container')

if result5:
    result6 = result5[0].find_all('h4')
else:
    result6 = None

result7 = soup.find('div',
                    class_='elementor-element elementor-element-f25f4b4 elementor-widget elementor-widget-text-editor')

result8 = result7.find_all('div', class_='elementor-widget-container')

if result8:
    result9 = result8[0].find_all('h4')
else:
    result9 = None

# phd program
result10 = soup.find('div', class_='elementor-element elementor-element-18ed3c0'
                                   ' elementor-widget elementor-widget-text-editor')

result11 = result10.find_all('div', class_='elementor-widget-container')

if result11:
    result12 = result11[0].find_all('h4')
else:
    result12 = None

result13 = soup.find('div', class_='elementor-element elementor-element-b961f5d'
                                   ' elementor-widget elementor-widget-text-editor')

result14 = result13.find_all('div', class_='elementor-widget-container')

if result14:
    result15 = result14[0].find_all('h4')
else:
    result15 = None

master = result6 + result9
phd = result12 + result15

for i, j, m in zip(result3, master, phd):
    undergrade_program = i.text
    master_program = j.text
    phd_program = m.text
    file.write(undergrade_program + ',' + master_program + ',' + phd_program + ',' + '\n')
