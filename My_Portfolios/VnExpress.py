import requests
from bs4 import BeautifulSoup
import googletrans
tl = googletrans.Translator()


#爬取自VnExpress網站
vne = requests.get("https://vnexpress.net")
vne.encoding = 'utf-8'
vnesoup = BeautifulSoup(vne.text, 'html.parser')
#TT主標題
vnetitle = vnesoup.find_all("h3")
#TT主標說明
vnediscr = vnesoup.find_all("p", class_="description")
#VTV第一標題
vnetitle1 = vnetitle[0].getText()[1:]
vnediscr1 = vnediscr[0].getText()[:-7]
vnetitle1tw = tl.translate(vnetitle1, src='vi', dest='zh-TW').text
vnediscr1tw = tl.translate(vnediscr1, src='vi', dest='zh-TW').text
#VTV第二標題
vnetitle2 = vnetitle[1].getText()[2:]
vnediscr2 = vnediscr[2].getText()[1:-7]
vnetitle2tw = tl.translate(vnetitle2, src='vi', dest='zh-TW').text
vnediscr2tw = tl.translate(vnediscr2, src='vi', dest='zh-TW').text
#VTV第三標題
vnetitle3 = vnetitle[2].getText()[2:]
vnediscr3 = vnediscr[3].getText()[1:-7]
vnetitle3tw = tl.translate(vnetitle3, src='vi', dest='zh-TW').text
vnediscr3tw = tl.translate(vnediscr3, src='vi', dest='zh-TW').text
#VTV第四標題
vnetitle4 = vnetitle[3].getText()
vnediscr4 = vnediscr[4].getText()
vnetitle4tw = tl.translate(vnetitle4, src='vi', dest='zh-TW').text
vnediscr4tw = tl.translate(vnediscr4, src='vi', dest='zh-TW').text
#VTV第五標題
vnetitle5 = vnetitle[4].getText()[2:]
vnediscr5 = vnediscr[5].getText()[1:-7]
vnetitle5tw = tl.translate(vnetitle5, src='vi', dest='zh-TW').text
vnediscr5tw = tl.translate(vnediscr5, src='vi', dest='zh-TW').text


#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "CkddxnWHY6oVsCF2yvfeUMnb0rIlLcUgnnCJL4m5NGL",
        "Content-Type": "application/x-www-form-urlencoded"
    }
params = {"message": 
"\n" + "🕦第一則新聞" 
+ "\n" + "⇢" + vnetitle1 + "⇢" + vnetitle1tw 
+ "\n" + vnediscr1 + "\n" + vnediscr1tw
+ "\n\n" + "🕦第二則新聞" 
+ "\n" + "⇢" + vnetitle2 + "⇢" + vnetitle2tw 
+ "\n" + vnediscr2 + "\n" + vnediscr2tw
+ "\n\n" + "🕦第三則新聞" 
+ "\n" + "⇢" + vnetitle3 + "⇢" + vnetitle3tw 
+ "\n" + vnediscr3 + "\n" + vnediscr3tw
+ "\n\n" + "🕦第四則新聞" 
+ "\n" + "⇢" + vnetitle4 + "\n" + "⇢" + vnetitle4tw 
+ "\n" + vnediscr4 + "\n" + vnediscr4tw
+ "\n\n" + "🕦第五則新聞" 
+ "\n" + "⇢" + vnetitle5 + "⇢" + vnetitle5tw 
+ "\n" + vnediscr5 + "\n" + vnediscr5tw
}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200