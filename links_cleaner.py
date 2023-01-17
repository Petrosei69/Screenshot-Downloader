import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
from tqdm import trange

file = open('links.txt', "r")
all_words = []
line = file.readline().split()
while line:
    all_words.extend(line)
    line = file.readline().split()

print(f"Total link(s):{len(all_words)}")

# Transformation initial links to links with absolute path to images
links = []

for i in trange(len(all_words)):
    r = requests.get(all_words[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img', {"src": True}, class_="can_zoom")
    for image in images:
        links.append(image['src'])
        links[i] = links[i][0:69]

#print(len(links))
#print(links)

with open('clearlinks.txt','w', encoding="utf-8") as tfile:
	tfile.write('\n'.join(links))