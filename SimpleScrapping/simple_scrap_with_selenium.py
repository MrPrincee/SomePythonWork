from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.thesun.co.uk/sport/football/'

path = "C:/Users/User/Desktop/chromedriver.exe"

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')


for container in containers:
    title = container.find_element(by="xpath", value='./a/h3').text
    subtitle = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/p').text
    print('------------------------------------------')
    print(title)
    print('------------------------------------------')
    print(subtitle)
    print('------------------------------------------')

