import lxml, requests
from bs4 import BeautifulSoup
import schedule
import time
 
def job():
    result = requests.get("http://taipeischool.org/administration");
    result.encoding = 'utf-8'
    soup = BeautifulSoup(result.text, 'lxml')
    titles = soup.find("td", align="left").getText()
    print(titles)
 
schedule.every(1).minutes.do(job)       #部署每1分钟执行一次job()函数的任务
#schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
#schedule.every().day.at("15:24").do(job) #部署在每天的10:30执行job()函数的任务
#schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
#schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务
 
while True:
    schedule.run_pending()
    #time.sleep(1) 