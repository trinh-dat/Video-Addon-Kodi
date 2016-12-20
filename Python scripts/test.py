# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup

#url = "http://javmobile.net/censored/oppai/pppd-524-spence-mammary-gland-development-clinic-special-julia.html"
url = "http://javmobile.net/?s=julia"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

hrefs = soup.find_all("<a rel='bookmark'></a>")

hrefarray = []

for href in hrefs:
    print href