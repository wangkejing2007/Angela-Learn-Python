# 此程式檔的修改說明，請參閱這篇留言：
# https://swf.com.tw/?p=1205&cpage=1#comment-985650

from tqdm import tqdm
import re
import requests as req
from selenium import webdriver
import time    # 新增引用此程式庫

driver_path = "C:\\webdriver\\chromedriver.exe"
url = 'http://pybook.epizy.com/files/'

option = webdriver.ChromeOptions()
# option.add_argument('headless')   # 隱藏瀏覽器
driver = webdriver.Chrome(driver_path, options=option)
driver.implicitly_wait(10)  # 隱性等待，最長10秒

driver.get(url)
links = driver.find_elements_by_xpath('//a')

file_set = set()
pattern = re.compile(r'[\w]+.r(?:ar|\d{1,3})$')

# def download(url):
#     filename = url.split('/')[-1]
#     r = req.get(url, stream=True)
#     with open(filename, 'wb') as f:
#         for data in tqdm(r.iter_content(1024)):
#             f.write(data)

#     return filename


for a in links:
    href = a.get_attribute("href")
    rar = pattern.search(href)

    if rar:
        filename = rar.group()       # 取出檔名
        if filename not in file_set:  # 如果此檔案沒有下載過…
            a.click()                # 點擊此超連結
            time.sleep(1)            # 暫停1秒鐘
            file_set.add(filename)   # 紀錄此檔案

# for rar in file_set:
#     link = url + rar
#     print(href)

#     h = req.head(link)
#     if h.status_code == 200:
#         filename = download(link)
#         print(filename + ' 檔案下載完畢！')

driver.quit()
