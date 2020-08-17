import requests
from bs4 import BeautifulSoup
import googletrans
tl = googletrans.Translator()

#爬取自Zing News網站
zn = requests.get("https://zingnews.vn/")
zn.encoding = 'utf-8'
znsoup = BeautifulSoup(zn.text, 'html.parser')
#Zing News主標題
zntitle = znsoup.find_all("p", class_="article-title")
#Zing News主標題
znitem1 = zntitle[0].getText()[1:]
znitem1vn = tl.translate(znitem1, src='vi', dest='zh-TW').text
#Zing News第一副標題
znitem2 = zntitle[1].getText()[1:]
znitem2vn = tl.translate(znitem2, src='vi', dest='zh-TW').text

#爬取自Vietnam News網站
vn = requests.get("https://vietnamnews.vn/")
vn.encoding = 'utf-8'
vnsoup = BeautifulSoup(vn.text, 'html.parser')
#Vietnam News主標題
vntitle = vnsoup.find_all("p", class_="slide-text")
#Vietnam News主標題
vnitem1 = vntitle[0].getText()
vnitem1vn = tl.translate(vnitem1, src='en', dest='zh-TW').text
#Vietnam News第一副標題
vnitem2 = vntitle[1].getText()
vnitem2vn = tl.translate(vnitem2, src='en', dest='zh-TW').text


#爬取自VGP News網站
vgp = requests.get("http://baodientu.chinhphu.vn/")
vgp.encoding = 'utf-8'
vgpsoup = BeautifulSoup(vgp.text, 'html.parser')
#Báo Dân trí主標題
vgptitle = vgpsoup.find_all("h1", class_="title")
#第一主標題
vgpitem1 = vgptitle[0].getText()[31:]
vgpitem1vn = tl.translate(vgpitem1, src='vi', dest='zh-TW').text
#這裡第二主標題
vgpitem2 = vgptitle[1].getText()[31:]
vgpitem2vn = tl.translate(vgpitem2, src='vi', dest='zh-TW').text

#爬取自VietNamNet網站
vnn = requests.get("https://vietnamnet.vn/")
vnn.encoding = 'utf-8'
vnnsoup = BeautifulSoup(vnn.text, 'html.parser')
#VietNamNet主標題
vnntitle = vnnsoup.find("a", class_="title f-22 articletype_1 bold").getText()[:-4]
vnntitlevn = tl.translate(vnntitle, src='vi', dest='zh-TW').text
#VietNamNet第一副標題
vnntitle1 = vnnsoup.find("a", class_="title SubString55").getText()
vnntitle1vn = tl.translate(vnntitle1, src='vi', dest='zh-TW').text


#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "CkddxnWHY6oVsCF2yvfeUMnb0rIlLcUgnnCJL4m5NGL",
        "Content-Type": "application/x-www-form-urlencoded"
    }
params = {"message": 
"\n\n" + "❰Zing News 熱新聞❱" 
+ "\n" + "❶ " + znitem1 + "⤿ " + znitem1vn 
+ "\n" + "❷ " + znitem2 + "⤿ " + znitem2vn

+ "\n\n" + "❰Vietnam News 英文新聞❱"
+ "\n" + "❶ " + vnitem1 + "\n" + "⤿ " + vnitem1vn 
+ "\n" + "❷ " + vnitem2 + "\n" + "⤿ " + vnitem2vn

+ "\n\n" + "❰VGP News 政府電子報❱"
+ "\n" + "❶ " + vgpitem1 + "⤿ " + vgpitem1vn
+ "\n" + "❷ " + vgpitem2 + "⤿ " + vgpitem2vn

+ "\n\n" + "❰VietNamNet 網站❱"
+ "\n" + "❶ " + vnntitle + "\n" + "⤿ " + vnntitlevn
+ "\n" + "❷ " + vnntitle1 + "\n" + "⤿ " + vnntitle1vn
}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200