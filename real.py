from urllib import urlopen
from sys import exit
from bs4 import BeautifulSoup
page = urlopen('http://www.realmadrid.com/en/tickets')
soup = BeautifulSoup(page, 'html.parser')
for i in soup.find_all('td', class_='m_match_aditional_info'):
    if i.text == 'Matchday 15':
        exit(1)
