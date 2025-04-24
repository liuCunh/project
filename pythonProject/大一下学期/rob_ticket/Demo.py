import time

from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.csdn.net/'
driver.get(url)
driver.maximize_window()  # 将窗口全屏化
time.sleep(10)  # 程序运行至此，停止10秒钟
driver.refresh()
