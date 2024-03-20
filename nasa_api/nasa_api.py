import requests
import datetime




api_key = '5Yq5hy5sRARatKySHcfqU8gtkeTPCi9zZWDY0got'

url = 'https://api.nasa.gov/planetary/apod'

date_string = str(datetime.datetime.now())


c_day = date_string[8:10]
c_day = int(c_day)

day = 1

def save_image_from_url(url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved as {filename}")
    else:
        print(f"Failed to fetch the image. Status code: {response.status_code}")


while day < c_day:
    if day < 10:
        current_day = f'0{day}'
    else:
        current_day = day
    date = f'2023-08-{str(current_day)}'
    param = {'api_key': api_key,'date':date}
    response = requests.get(url,params=param)
    photo_url = response.json()['hdurl']
    photo_responce = requests.get(photo_url)
    filename = f'photo_{current_day}.jpg'
    save_image_from_url(photo_url,filename)
    day += 1

print('Finished!')




