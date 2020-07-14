# 參閱6-20頁

from selenium import webdriver

driver_path = "C:\\webdriver\\chromedriver.exe"  # 請自行修改檔案路徑
driver = webdriver.Chrome(driver_path)

url = 'https://swf.com.tw/scrap/simple.html'
driver.get(url)
h1 = driver.find_element_by_xpath('//h1')
print('標題文字：', h1.text)
driver.quit()
