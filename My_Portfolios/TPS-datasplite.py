import requests
from bs4 import BeautifulSoup

result = requests.get("http://taipeischool.org/administration")
result.encoding = 'utf-8'
soup = BeautifulSoup(result.text, 'html.parser')
titles = soup.find_all("a", target="_blank")

top0 = titles[0].getText()[1:]
top00 = str(titles[0])[8:64]
top1 = titles[1].getText()[1:]
top11 = str(titles[1])[8:64]
top2 = titles[2].getText()[1:]
top22 = str(titles[2])[8:64]
top3 = titles[3].getText()[1:]
top33 = str(titles[3])[8:64]
top4 = titles[4].getText()[1:]
top44 = str(titles[4])[8:64]

#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "rKmAkxCxlA30ABzJLrnaNJZBf8DK6ulh77LqjcA10mc",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": "\n\n" + "✎ " + top0 
+ "\n" + top00 
+ "\n\n" + "✎ " + top1 
+ "\n" + top11 
+ "\n\n" + "✎ " + top2 
+ "\n" + top22
+ "\n\n" + "✎ " + top3 
+ "\n" + top33
+ "\n\n" + "✎ " + top4 
+ "\n" + top44}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)

print(r.status_code)  #200