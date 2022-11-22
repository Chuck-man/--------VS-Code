import os
import shutil
import random
import csv

def Randomizer(path: str, path_copier: str):

    if not os.path.exists("dataset_another"):
        os.mkdir("dataset_another")

    source = os.listdir(path + "/")
    data = []

    for i in source:
        source_data = os.listdir(path + "/" + i)
        for j in source_data:
            exist = True
            
            while(exist):
                rand = random.randint(0, 10000)
                value = str(rand)
                exist = os.path.exists(path_copier + "/" + value + ".jpg")
                
            shutil.copy(os.path.join(path + "/", i + "/" + j), os.path.join(path_copier + "/", value + ".jpg"))
            absolute = os.path.abspath(path + "/" + i + "/" + j)
            regarding = os.path.relpath(path + "/" + i + "/" + j)
            data.append([absolute, regarding, i])

    with open(path_copier + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

Randomizer("dataset", "dataset_another")
