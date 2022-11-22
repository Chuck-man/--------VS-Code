import os
import shutil

def copy(path: str, path_copier: str):

    if not os.path.exists("path_copier"):
        os.mkdir("path_copier")

    source = os.listdir(path + "/")

    for i in source:
        source_data = os.listdir(path + "/" + i)
        for j in source_data:
            shutil.copyfileobj(os.path.join(path + "/" + i, j), os.path.join(path_copier + "/", i + "__" + j))
