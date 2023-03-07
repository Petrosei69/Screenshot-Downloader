import requests
from bs4 import BeautifulSoup
import os
from tqdm import trange
import difflib
import socket

socket.setdefaulttimeout(120)

file = open('links.txt', "r")
all_words = []
line = file.readline().split()
while line:
    all_words.extend(line)
    line = file.readline().split()

print(f"Total link(s):{len(all_words)}")

# Transformation initial links to links with absolute path to images
links = []
clear = []
for i in trange(len(all_words)):
    r = requests.get(all_words[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img', {"src": True}, class_="can_zoom")
    for image in images:
        try:
            clear.append(all_words[i])
            links.append(image['src'])
            links[i] = links[i]
        except IndexError:
            pass

for i in trange(len(links)):
    links[i] = links[i][0:69]


with open('clearlinks.txt','w', encoding="utf-8") as tfile:
	tfile.write('\n'.join(links))

with open('correctlinks.txt','w', encoding="utf-8") as tfile:
	tfile.write('\n'.join(clear))


with open('links.txt', 'r') as file1, open('correctlinks.txt', 'r') as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

# Находим различия между файлами
differ = difflib.Differ()
diff = list(differ.compare(file1_lines, file2_lines))

# Ищем отличающиеся строки
results = []
for line in diff:
    if line.startswith('-') or line.startswith('+'):
        results.append(line.strip())

# Записываем результат в файл
with open('exceptions.txt', 'w') as result_file:
    for result in results:
        result_file.write(result + '\n')
#####################################################################
# part of download
#####################################################################
file = open('correctlinks.txt', "r")
all_words = []
line = file.readline().split()
while line:
    all_words.extend(line)
    line = file.readline().split()

# Import file with clear links with absolute path to image
file = open('clearlinks.txt', "r")
links = []
line = file.readline().split()
while line:
    links.extend(line)
    line = file.readline().split()

try:
    os.mkdir(os.path.join(os.getcwd(), 'screenshots'))
except:
    pass
os.chdir(os.path.join(os.getcwd(), 'screenshots'))


# Downloading files from urls
for i in trange(len(links)):

    try:
        filename = os.path.join(all_words[i].split("/")[-1])
    except IndexError:
        print("Ошибка: выход за границы списка!")

    with open(filename + '.jpg', 'wb') as handle:
        response = requests.get(links[i], stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


import difflib

# Открываем файлы и считываем содержимое
