import lxml, requests
from bs4 import BeautifulSoup

result = requests.get("http://taipeischool.org/administration")
result.encoding = 'utf-8'

soup = BeautifulSoup(result.text, 'lxml')

titles = soup.find("td", align="left").getText()[1:150]

#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "SAmiSWLIWlezhlgouwhv6kP2gpFecWZhxSmtsvgsF09",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": titles + "....." + "\n\n" + "<更多資訊> " + "http://taipeischool.org/administration"}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200