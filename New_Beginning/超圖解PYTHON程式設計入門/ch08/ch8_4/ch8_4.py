from datetime import datetime
from selenium import webdriver
from model import sheet 
from urllib import parse

gs = sheet.GoogleSheet('谷歌試算表','網拍價格')
gs.resize()
raw_key='神臂鬥士'
FETCH_LIMIT = 5

def open_page(driver, url, title_path ,price_path, link_path):
    driver.get(url)    # 連結到網拍    

    titles= driver.find_elements_by_xpath(title_path)
    prices= driver.find_elements_by_xpath(price_path)
    links= driver.find_elements_by_xpath(link_path)
    
    return (titles, prices, links)

def save_data(titles, prices, links):
    total = len(titles)
    size = FETCH_LIMIT if total>=FETCH_LIMIT else total

    for _, title, price, link in zip(range(size), titles, prices, links):
        dt = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        _title = title.get_attribute('textContent')
        _price = price.text
        _link = link.get_attribute('href')

        gs.append_row([dt, _title, _price, _link])

def main():
    search_key=parse.quote(raw_key)
    sites=[
        {
            'url':"https://tw.bid.yahoo.com/search/auction/"
                "product?kw={key}&p={key}&sort=-ptime",
            # 商品標題XPath
            'title_path':"//span[contains(@class, 'BaseGridItem__title')]",
            # 價格XPath
            'price_path':"//span[contains(@class, 'BaseGridItem__price')]/em",
            # 商品超連結XPath
            'link_path':"//ul[@class='gridList']/li/a"
        },
        {
            'url':'https://find.ruten.com.tw/s/?q={key}&sort=new%2Fdc',
            'title_path':"//dl[@class='search_form s_grid']//h5",
            'price_path':"//ul[@class='price_box']//span[@class='price']",
            'link_path':"//div[@class='prod_img_wrap']/a[1]"
        },
        {
            'url':'https://shopee.tw/search?keyword={key}&page=0&sortBy=ctime',
            'title_path':"//div[contains(@class,'shopee-search-item-result__item')]"
                        "/div/a/div/div[2]/div[1]/div",
            'price_path':"//div[contains(@class,'shopee-search-item-result__item')]"
                        "/div/a/div/div[2]/div[2]/div[1]",
            'link_path':"//div[contains(@class,'shopee-search-item-result__item')]"
                        "/div/a"
        }
    ]

    driver_path = "C:\\webdriver\\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(10)  # 等待網頁載入

    for s in sites:
        url = s['url'].format(key=search_key)
        title_path = s['title_path']
        price_path = s['price_path']
        link_path = s['link_path']

        titles, prices, links = open_page(driver, url, 
                                          title_path, price_path, link_path)
        save_data(titles, prices, links)

    driver.quit()  # 關閉瀏覽器
    
if __name__ == "__main__":
    main()