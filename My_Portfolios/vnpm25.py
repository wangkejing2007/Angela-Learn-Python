import requests
from bs4 import BeautifulSoup
import googletrans
tl = googletrans.Translator()

#爬取自aqicn網站
#河內
hn = requests.get("https://aqicn.org/city/vietnam/hanoi/us-embassy/")
hn.encoding = 'utf-8'
hnsoup = BeautifulSoup(hn.text, 'html.parser')
#河內數據
hnpm25 = hnsoup.find("table", class_="api").getText()
hnpm25tw = tl.translate(hnpm25, src='en', dest='zh-TW').text

#胡志明市
hcm = requests.get("https://aqicn.org/city/vietnam/ho-chi-minh-city/us-consulate/")
hcm.encoding = 'utf-8'
hcmsoup = BeautifulSoup(hcm.text, 'html.parser')
#胡志明市數據
hcmpm25 = hcmsoup.find("table", class_="api").getText()
hcmpm25tw = tl.translate(hcmpm25, src='en', dest='zh-TW').text

'''
#承天順化
hue = requests.get("https://aqicn.org/city/vietnam/thua-thien-hue/83-hung-vuong/")
hue.encoding = 'utf-8'
huesoup = BeautifulSoup(hue.text, 'html.parser')
#承天順化數據
huepm25 = huesoup.find("table", class_="api").getText()
huepm25tw = tl.translate(huepm25, src='en', dest='zh-TW').text
'''

#爬取自駐越南台北經濟文化辦事處網站
#駐地新聞
tw = requests.get("https://www.taiwanembassy.org/vn/index.html")
tw.encoding = 'utf-8'
twsoup = BeautifulSoup(tw.text, 'html.parser')
#駐地頭條新聞
twtitle = twsoup.find("div", class_="list-column-content").getText()[1:]


#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "CkddxnWHY6oVsCF2yvfeUMnb0rIlLcUgnnCJL4m5NGL",
        "Content-Type": "application/x-www-form-urlencoded"
    }
params = {"message": 
"\n" + "[河內市空氣品質]" 
#+ "\n" + "PM2.5:" + hnpm25
+ "\n" + "PM2.5值 : " + hnpm25tw
+ "\n\n" + "[胡志明市空氣品質]" 
#+ "\n" + "PM2.5:" + hcmpm25
+ "\n" + "PM2.5值 : " + hcmpm25tw
+ "\n\n" + "[↓富美興空品測量站↓]" 
+ "\n" + "https://bit.ly/318VKE6"

+ "\n\n" + "[經辦處駐地新聞]" 
+ "\n" + twtitle
+ "\n" + "[↓駐越南台北經濟文化辦事處↓]" 
+ "\n" + "https://bit.ly/3fq8F9O"
}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200