import lxml, requests
from bs4 import BeautifulSoup
import googletrans

result = requests.get("http://taipeischool.org/administration")
result.encoding = 'utf-8'

soup = BeautifulSoup(result.text, 'lxml')

titles = soup.find("td", align="left").getText()[3:120]

translator = googletrans.Translator()
titlesvn = translator.translate(titles, src='zh-CN', dest='vi')

#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "SAmiSWLIWlezhlgouwhv6kP2gpFecWZhxSmtsvgsF09",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": "\n" + titles + "....." + "(more↓)" + "\n\n" + "【越南語/Tiếng Việt】" + "\n" + titlesvn.text + "....." + "(more↓)" + "\n\n" + "<<校網連結>> " + "http://taipeischool.org/administration"}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200