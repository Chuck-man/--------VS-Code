import os
import shutil
import random
import csv

def Randomizer(path, path_copier):
    if not os.path.exists("path_copier"):
        os.mkdir("path_copier")
    source = os.listdir(path + "/")
    data = []
    for i in source:
        source_data = os.listdir(path + "/" + i)
        for j in source_data:
            rand = random.randint(0, 10000)
            value = str(rand)
            shutil.copyfileobj(os.path.join(path, i + "/" + j), os.path.join(path_copier + "/", value + ".jpg"))

Randomizer("dataset")