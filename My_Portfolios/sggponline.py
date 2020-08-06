import requests
from bs4 import BeautifulSoup

#西貢解放日報
result = requests.get("https://cn.sggp.org.vn/")
result.encoding = 'utf-8'
soup = BeautifulSoup(result.text, 'html.parser')
title0 = soup.find_all("h2", class_="title")
top0 = title0[0].getText()
top1 = title0[1].getText()
top2 = title0[2].getText()
top3 = title0[3].getText()
top4 = title0[4].getText()

#越南通訊社
zh = requests.get("https://zh.vietnamplus.vn/")
zh.encoding = 'utf-8'
zhsoup = BeautifulSoup(zh.text, 'html.parser')
#主標題
zhtitle = zhsoup.find("div", class_="summary").getText()[1:]
#次標題
zhsubtitle = zhsoup.find_all("h2")
top6 = zhsubtitle[0].getText()[1:]
top7 = zhsubtitle[1].getText()[1:]
top8 = zhsubtitle[2].getText()[1:]
top9 = zhsubtitle[3].getText()[1:]


#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "CkddxnWHY6oVsCF2yvfeUMnb0rIlLcUgnnCJL4m5NGL",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": 
"\n" + "[西貢解放日報]"
+"\n" + "❶ " + top0 
+ "\n" + "❷ " + top1 
+ "\n" + "❸ " + top2 
+ "\n" + "❹ " + top3 
+ "\n" + "❺ " + top4 
+ "\n\n" + "[越南通訊社]"
+ "\n" + "❶ " + zhtitle
+ "❷ " + top6 
+ "❸ " + top7
+ "❹ " + top8 
+ "❺ " + top9
+ "\n" + "西貢解放日報 ⋙ " + "https://cn.sggp.org.vn/"
+ "\n\n" + "越南通訊社⋙ " + "https://zh.vietnamplus.vn/"
}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)

print(r.status_code)  #200