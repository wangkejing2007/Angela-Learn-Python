import hashlib,os,requests,lxml,schedule,time
from bs4 import BeautifulSoup

while True:
    url = "http://taipeischool.org/administration"
    # 讀取網頁原始碼
    html=requests.get(url).text.encode('utf-8-sig')
    
    md5 = hashlib.md5(html).hexdigest()
    # 判斷網頁是否更新
    if os.path.exists('old_md5.txt'):
        with open('old_md5.txt', 'r') as f:
            old_md5 = f.read()
        with open('old_md5.txt', 'w') as f:
            f.write(md5)
    else:
        with open('old_md5.txt', 'w') as f:
            f.write(md5)

    # 判斷網頁是否更新後的動作
    if md5 != old_md5:
        result = requests.get("http://taipeischool.org/administration");
        result.encoding = 'utf-8'
        soup = BeautifulSoup(result.text, 'lxml')
        titles = soup.find("td", align="left").getText()[2:]
        print('資料已更新，爬蟲標題如下：') 
        print(titles)
    else:
        print('網頁資料尚未更新！')

    time.sleep(30) 