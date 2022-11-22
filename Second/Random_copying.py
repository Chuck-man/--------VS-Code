import os
import shutil
import random
import csv

def Randomizer(path: str, path_copier: str):

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
            absolute = os.path.abspath(path + "/" + i + "/" + j)
            regarding = os.path.relpath(path + "/" + i + "/" + j)
            data.append([absolute, regarding, i])

    with open(path_copier + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

Randomizer("dataset/")
