import lxml, requests
from bs4 import BeautifulSoup

result = requests.get("http://taipeischool.org/administration")
result.encoding = 'utf-8'

soup = BeautifulSoup(result.text, 'lxml')
titles = soup.find("td", align="left").getText()
print(titles)