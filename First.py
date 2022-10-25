#Лабораторная работа 1
import re
from bs4 import BeautifulSoup
import requests
import os
import time
import cv2

#dog_path = "C:/Users/User/dataset/dog"
#cat_path = "C:/Users/User/dataset/cat"

def scraping(typename):
    if not os.path.exists("dataset"):
        os.mkdir("dataset")
    if not os.path.exists("dataset" + typename):
        os.mkdir("dataset" + typename)

    count = 0

    if not typename == "cat":
        url = f"https://yandex.ru/images/search?p=&text=dog&uinfo=sw-1920-sh-1080-ww-912-wh-881-pd-1.100000023841858-wp-16x9_2560x1440&lr=51&rpt=image"
    else:
        url = f"https://yandex.ru/images/search?p=&text=cat&uinfo=sw-1920-sh-1080-ww-878-wh-924-pd-1-wp-16x9_1920x1080&lr=51&rpt=image"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    images = soup.find_all('img', class_="justifier__thumb")
    src_list = []
    for image in images:
        src_list.append(image.get("src"))
    for img in src_list:
        if img.find("n=13") != -1:
            try:
                source = "https:" + img
                picture = requests.get(source)

                name_file = str([count])

                out = open("dataset" + typename + "/" + name_file.zfill(4) + ".jpg", "wb")
                out.write(picture.content)
                out.close()

                time.sleep(0.25)

                count += 1

            except Exception as ex:
                print(ex)

scraping("cat")
            
