#Лабораторная работа 1
import re
from bs4 import BeautifulSoup
import requests
import os
import time
import cv2

def scraping(url):

    if not os.path.isdir("dataset"): 
        os.mkdir("dataset")
    if not os.path.isdir("dataset" + url): 
        os.mkdir("dataset"+ url)
    url_full = "https://yandex.ru/images/search?text=" + url

    array = []
    