# Screenshot-Downloader
Screenshot downloader from url

Use https://skr.sh/ as resourse of images



To use script add file .txt with links 
```shell
file = open('links.txt', "r")
```
p.s Downloading of large images often interrupted, so may better divide huge file with links to several files smaller (optimal = 100-150)


At first you need to start links_cleaner.py to convert initial links to directional links to .jpg files.
That script create file with directional links and this file uses in main.py to download images.
