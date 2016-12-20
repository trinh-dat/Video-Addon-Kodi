from bs4 import BeautifulSoup
import requests

url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=lost+angeles"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

for link in links:
    print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

