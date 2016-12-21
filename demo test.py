from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://news.ycombinator.com')
html = driver.page_source
soup = BeautifulSoup(html, "html-parser")

for tag in soup.find_all('title'):
    print tag.text
