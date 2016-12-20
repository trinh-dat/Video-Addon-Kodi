from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import json

url = "http://javmobile.net/?s=julia"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

imgs = soup.find_all("img" , {"class": "entry-thumb"})

images = []
titles = []

for img in imgs:
    images.append(img.get("src"))
    titles.append(img.get("title"))

jsonList = []
for i in range(0,len(images)):
    jsonList.append({"name" : titles[i], "thumb": images[i]})

jsonList2 = json.dumps(jsonList, indent = 1)
print(jsonList2)