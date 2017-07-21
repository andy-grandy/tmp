from bs4 import BeautifulSoup
from urllib import urlopen, urlretrieve
page=urlopen('https://2ch.hk/p/res/513768.html')

soup = BeautifulSoup(page, 'html.parser')

#print soup.prettify('utf-8')

for i in soup.find_all("div", class_='image-link'):
    url1 = "https://2ch.hk" + i.a["href"]
    urlretrieve(url=url1, filename = "./img/" + url1.split('/')[-1])
