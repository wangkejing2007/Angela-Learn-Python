import lxml, requests
from bs4 import BeautifulSoup


result = requests.get("http://taipeischool.org/administration")
result.encoding = 'utf-8'
soup = BeautifulSoup(result.text, 'lxml')
titles = soup.find("td", align="left").getText()[2:200]

#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "SAmiSWLIWlezhlgouwhv6kP2gpFecWZhxSmtsvgsF09",
        "Content-Type": "application/x-www-form-urlencoded"
    } 
params = {"message": titles + "....." + "\n\n" + "<更多資訊> " + "http://taipeischool.org/administration"} 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200


#以下為flask程式
from flask import Flask
app = Flask(__name__)
@app.route('/index.html')
@app.route('/')

def index():
    return "定時查詢胡台校官網首頁公布資訊"
if __name__ == '__main__':
    app.run()