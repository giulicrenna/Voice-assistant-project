from hashlib import new
import random
import os


path = os.getcwd()
directory = str("libs")
path = os.path.join(path, directory, "jks.txt")
empty_str = ""

def jokes(num):
    file = open(path, "rt", encoding="utf-8")
    text = file.readlines()
    new_text = empty_str.join(text[num])
    return new_text

