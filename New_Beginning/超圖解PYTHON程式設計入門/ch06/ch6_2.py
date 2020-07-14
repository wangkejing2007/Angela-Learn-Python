# 參閱6-29頁

from selenium import webdriver

driver_path = "C:\\webdriver\\chromedriver.exe"  # 請自行修改檔案路徑
driver = webdriver.Chrome(driver_path)

url = 'https://www.google.com.tw/'
driver.get(url)

search_field = driver.find_element_by_xpath("//input[@name='q']")
search_field.send_keys('超圖解Python物聯網')
search_btn = driver.find_element_by_xpath("//input[@type='submit']")
search_btn.click()
