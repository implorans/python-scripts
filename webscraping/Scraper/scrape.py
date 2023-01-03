import requests
import os
from bs4 import BeautifulSoup

URL = "http://oraniakarnaval.co.za/karnaval-2013-2/"
getURL = requests.get(URL, headers={"User-Agent" : "Mozilla/5.0"})

soup = BeautifulSoup(getURL.text, "html.parser")

images = soup.find_all('img')

if not os.path.exists('images/2013'):
    os.makedirs('images/2013')

for image in images:
    image_url = image['src']
    response = requests.get(image_url)
    open(f'images/2013/{image_url.split("/")[-1]}', 'wb').write(response.content)

os.listdir('images/')
