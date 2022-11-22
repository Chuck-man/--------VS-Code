import csv
import os

def creating_csv(path, path_to) -> None:
    data = []

    if not os.path.exists("path_to"):
        os.mkdir("path_to")
    
    source = os.listdir(path + "/")
    for i in source:
        source_info = os.listdir(path + "/" + i)
        for j in source_info:
            absolute = os.path.abspath(path + "/" + i + "/" + j)
            regarding = os.path.relpath(path + "/" + i + "/" + j)
            data.append([absolute, regarding, i])
    with open(path_to + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

creating_csv("dataset", "dataset_csv")
