from selenium import webdriver
from urllib import parse

search_key=parse.quote('神臂鬥士')    # 商品關鍵字
url=' https://tw.bid.yahoo.com/search/auction/product?kw={key}&p={key}&sort=-ptime'
url=url.format(key=search_key)  # Yahoo!拍賣網址

driver_path = "C:\\webdriver\\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('headless')   # 新增隱藏（無頭）參數
driver = webdriver.Chrome(driver_path, options=option)
driver.implicitly_wait(10)
driver.get(url)

title_path = "//span[contains(@class, 'BaseGridItem__title')] "
price_path = "//span[contains(@class, 'BaseGridItem__price')]/em"
link_path="//ul[@class='gridList']/li/a" 

titles= driver.find_elements_by_xpath(title_path)
prices= driver.find_elements_by_xpath(price_path)
links= driver.find_elements_by_xpath(link_path)

total = len(titles)
print('商品數量：', total)

print('='*60)   # 顯示商品和價格

size = 5 if total>=5 else total
index = 0

for title, price, link in zip(titles, prices, links):
    print(title.get_attribute('textContent') + "\n"
          + price.text + "\n"
          + link.get_attribute('href'))
    print('-'*60)

    index += 1
    if index == size:
        break

driver.quit()