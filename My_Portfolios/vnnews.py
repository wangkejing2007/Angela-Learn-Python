import requests
from bs4 import BeautifulSoup
import googletrans
tl = googletrans.Translator()

#爬取自VnExpress網站
vnexpr = requests.get("https://vnexpress.net/")
vnexpr.encoding = 'utf-8'
vnexprsoup = BeautifulSoup(vnexpr.text, 'html.parser')
#VnExpress主標題
vnexprtitle = vnexprsoup.find("h3", class_="title-news").getText()[1:]
vnexprtitlevn = tl.translate(vnexprtitle, src='vi', dest='zh-TW').text
#VnExpress副標題
vnexprsubtitle = vnexprsoup.find_all("h3", class_="title_news")
#VnExpress第一副標題
vnexpritem1 = vnexprsubtitle[0].getText()[2:]
vnexpritem1vn = tl.translate(vnexpritem1, src='vi', dest='zh-TW').text


#爬取自VTV NEWS網站
vtv = requests.get("https://vtv.vn/")
vtv.encoding = 'utf-8'
vtvsoup = BeautifulSoup(vtv.text, 'html.parser')
#VTV主標題
vtvtitle = vtvsoup.find("h2").getText()[1:-40]
vtvtitlevn = tl.translate(vtvtitle, src='vi', dest='zh-TW').text
#VTV副標題
vtvsubtitle = vtvsoup.find_all("h3")
#VTV第一副標題
vtvitem1 = vtvsubtitle[0].getText()
vtvitem1vn = tl.translate(vtvitem1, src='vi', dest='zh-TW').text


#爬取自Tuổi Trẻ網站
tt = requests.get("https://tuoitre.vn/")
tt.encoding = 'utf-8'
ttsoup = BeautifulSoup(tt.text, 'html.parser')
#TT主標題
tttitle = ttsoup.find("h2", class_="title-focus-title").getText()[1:]
tttitlevn = tl.translate(tttitle, src='vi', dest='zh-TW').text
#TT副標題
ttsubtitle = ttsoup.find_all("h2", class_="title-news-list-focus")
#VTV第一副標題
ttitem1 = ttsubtitle[0].getText()[1:]
ttitem1vn = tl.translate(ttitem1, src='vi', dest='zh-TW').text


#爬取自Thanh Niên網站
tn = requests.get("https://thanhnien.vn/")
tn.encoding = 'utf-8'
tnsoup = BeautifulSoup(tn.text, 'html.parser')
#TN主標題
tntitle = tnsoup.find("a", class_="story__title").getText()
tntitlevn = tl.translate(tntitle, src='vi', dest='zh-TW').text
#TN副標題
tnsubtitle = tnsoup.find_all("span", class_="shorten")
#TN第一副標題
tnitem1 = tnsubtitle[0].getText()
tnitem1vn = tl.translate(tnitem1, src='vi', dest='zh-TW').text


#以下為Line Notify程式
headers = {
        "Authorization": "Bearer " + "CkddxnWHY6oVsCF2yvfeUMnb0rIlLcUgnnCJL4m5NGL",
        "Content-Type": "application/x-www-form-urlencoded"
    }
params = {"message": 
"\n\n" + "❰VnExpress 越南快訊❱" 
+ "\n" + "❶ " + vnexprtitle + "⤿ " + vnexprtitlevn 
+ "\n" + "❷ " + vnexpritem1 + "⤿ " + vnexpritem1vn

+ "\n\n" + "❰VTV 越南電視新聞網❱"
+ "\n" + "❶ " + vtvtitle + "⤿ " + vtvtitlevn
+ "\n" + "❷ " + vtvitem1 + "\n" + "⤿ " + vtvitem1vn 

+ "\n\n" + "❰Tuổi Trẻ 越南年輕人報❱"
+ "\n" + "❶ " + tttitle + "⤿ " + tttitlevn 
+ "\n" + "❷ " + ttitem1 + "⤿ " + ttitem1vn

+ "\n\n" + "❰Thanh Niên 越南青年報❱"
+ "\n" + "❶ " + tntitle + "\n" + "⤿ " + tntitlevn
+ "\n" + "❷ " + tnitem1 + "\n" + "⤿ " + tnitem1vn 
}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200