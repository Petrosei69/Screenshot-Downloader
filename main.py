import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs, BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
from tqdm import trange

# Загрузка файла с первоначальными ссылками для того чтобы их нарезать для имен скриншотов
file = open('links.txt', "r")
all_words = []
line = file.readline().split()
while line:
    all_words.extend(line)
    line = file.readline().split()

#print(all_words)
#print(len(all_words))

# Загрузка файла с чистыми ссылками на файлы
file = open('clearlinks.txt', "r")
links = []
line = file.readline().split()
while line:
    links.extend(line)
    line = file.readline().split()

#print(links)
#print(len(links))

# Создание папки для сохранения скриншотов
try:
    os.mkdir(os.path.join(os.getcwd(), 'screenshots'))
except:
    pass
os.chdir(os.path.join(os.getcwd(), 'screenshots'))


# Скачивание файлов
for i in trange(len(links)):

    filename = os.path.join(all_words[i].split("/")[-1])
    with open(filename + '.jpg', 'wb') as handle:
        response = requests.get(links[i], stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)