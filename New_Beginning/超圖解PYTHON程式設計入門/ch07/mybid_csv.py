import csv
from datetime import datetime
from selenium import webdriver
from urllib import parse

raw_key='神臂鬥士'
FETCH_LIMIT = 5
CSV_FILE_NAME = r'D:\bid.csv'  # 請自行修改檔名和路徑
write_header = True

def open_page(driver, url, title_path ,price_path, link_path):
    driver.get(url) 

    titles= driver.find_elements_by_xpath(title_path)
    prices= driver.find_elements_by_xpath(price_path)
    links= driver.find_elements_by_xpath(link_path)
    
    return (titles, prices, links)

def save_to_csv(titles, prices, links):
    log_data = ['日期時間', '商品標題', '價格', '網址'] # CSV標題列內容
    total = len(titles)
    size = FETCH_LIMIT if total>=FETCH_LIMIT else total

    with open(CSV_FILE_NAME, 'a', newline='', encoding='utf-8') as f:
        global write_header 
        w = csv.writer(f)

        if write_header:
            f.truncate(0)
            w.writerow(log_data)
            write_header = False

        for _, title, price, link in zip(range(size), titles, prices, links):
            log_data[0] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            log_data[1] = title.get_attribute('textContent')
            log_data[2] = price.text
            log_data[3] = link.get_attribute('href')

            w.writerow(log_data)  # 寫入一列


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
        save_to_csv(titles, prices, links)

    driver.quit()  # 關閉瀏覽器
    
if __name__ == "__main__":
    main()