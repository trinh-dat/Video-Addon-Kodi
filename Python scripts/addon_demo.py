# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup


url = "http://javmobile.net/?s=julia"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

imgs = soup.find_all("img" , {"class": "entry-thumb"})


images = []
titles = []
srcs = []

for img in imgs:
    images.append(img.get("src"))
    titles.append(img.get("title"))
    srcs.append(img.get("href"))

videos = []

for src in srcs:
    url2 = "http://javmobile.net/censored/oppai/pppd-524-spence-mammary-gland-development-clinic-special-julia.html"
    r2 = requests.get(url2)
    soup2 = BeautifulSoup(r2.content, "html.parser")


jsonList = {}
for i in range(0,len(images)):
    jsonList.append({"name" : titles[i], "thumb": images[i]})

print jsonList