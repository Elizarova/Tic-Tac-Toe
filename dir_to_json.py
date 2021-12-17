# -*- coding: utf-8 -*-
import os


def path_to_dict(path):
    d = ""
    if os.path.isdir(path):
        print ("\"", os.path.basename(path), "\"", ";", "\"", " | ".join([path_to_dict(
            os.path.join(path, x)) for x in os.listdir(path)]), "\"")
    else:
        d = "https://vinchecking.ru/wp-content/uploads/2021/11" + \
            os.path.basename(path)
    return d


path_to_dict('/home/kim/Desktop/data')
