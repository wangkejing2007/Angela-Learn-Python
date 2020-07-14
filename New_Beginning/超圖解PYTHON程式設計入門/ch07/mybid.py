from selenium import webdriver
from urllib import parse

raw_key='神臂鬥士'
FETCH_LIMIT = 5 # 擷取資料筆數的上限，最多5筆
search_key=parse.quote(raw_key)   # 經過URL編碼的商品關鍵字

def open_page(driver, url, title_path ,price_path, link_path):
    driver.get(url)    # 連結到網拍    

    titles= driver.find_elements_by_xpath(title_path)   # 擷取商品標題
    prices= driver.find_elements_by_xpath(price_path)   # 擷取價格
    links= driver.find_elements_by_xpath(link_path)     # 擷取超連結
    
    return (titles, prices, links)

def print_data(titles, prices, links):
    total = len(titles)
    size = FETCH_LIMIT if total>=FETCH_LIMIT else total  # 最多列舉5個商品

    print('='*60)   # 網站的分隔線

    for _, title, price, link in zip(range(size), titles, prices, links):
        print(title.get_attribute('textContent') + "\n"
            + price.text + "\n"
            + link.get_attribute('href'))

        print('-'*60)

def main():
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
        print_data(titles, prices, links)

    driver.quit()  # 關閉瀏覽器

if __name__ == "__main__":
    main()

# for i in range(0, len(l), n):  
#     yield l[i:i + n] 

