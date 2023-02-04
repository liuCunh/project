from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def judge(driver, path):
    try:
        driver.find_element(By.CSS_SELECTOR, path)
        return True
    except:
        return False


""" ！！！！！这次只能抢页面里面的第一张票！！！！！"""

from_station = '长沙'# input('出发地点：')
to_station = '岳阳'# input("目的地点：")
date = '2022-09-08'# input('时间：')
driver = webdriver.Chrome()

# 解决特征识别
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
           {"source": """Object.defineProperty(navigator, "webdriver", {get: () => false,});"""})
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.find_element(By.ID, 'J-userName').send_keys('15082699769')
driver.find_element(By.ID, 'J-password').send_keys('wad2020520')
driver.find_element(By.ID, 'J-login').click()

# 滑动验证
# 等待2秒钟，不要点的太快，以免被识别或者以免网页加载跟不上。
time.sleep(2)

# 定位 滑块标签
span = driver.find_element(By.ID, 'nc_1_n1z')
actions = ActionChains(driver)  # 行为链实例化
time.sleep(2)  # 等待2秒钟

# 经截图测量，滑块需要滑过的距离为300像素
actions.click_and_hold(span).move_by_offset(300, 0).perform()  # 滑动

# 行为操作
driver.implicitly_wait(10)  # 隐式等待
driver.find_element(By.CSS_SELECTOR, '#link_for_ticket').send_keys(Keys.ENTER)  # 准备查票

# 出发地点
driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(Keys.ENTER)  # 点击去
driver.find_element(By.CSS_SELECTOR, '#fromStationText').clear()  # 清楚内容
driver.find_element(By.CSS_SELECTOR, '#fromStationText').click()  # 清楚内容
driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(from_station)  # 输入地点
driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(Keys.ENTER)  # 点击去

# 目的地点
driver.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(Keys.ENTER)  # 点击去
driver.find_element(By.CSS_SELECTOR, '#toStationText').clear()  # 清楚内容
driver.find_element(By.CSS_SELECTOR, '#toStationText').click()  # 清楚内容
driver.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(to_station)  # 输入地点
driver.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(Keys.ENTER)  # 回车

# 出发时间
driver.find_element(By.CSS_SELECTOR, '#train_date').send_keys(Keys.ENTER)  # 点击去
driver.find_element(By.CSS_SELECTOR, '#train_date').clear()  # 清楚内容
driver.find_element(By.CSS_SELECTOR, '#train_date').click()  # 清楚内容
driver.find_element(By.CSS_SELECTOR, '#train_date').send_keys(date)  # 输入地点
driver.find_element(By.CSS_SELECTOR, '#train_date').send_keys(Keys.ENTER)  # 点击去

# 查询
driver.find_element(By.CSS_SELECTOR, '#query_ticket').click()

# 购票在此加循环
ticket = '#queryLeftTable tr:nth-child(9) .btn72'
driver.find_element(By.CSS_SELECTOR, ticket).click()
# for i in range(300):
#     if judge(driver, ticket):
#         driver.find_element(By.CSS_SELECTOR, ticket).click()
#         break
#     driver.implicitly_wait(10)
#     driver.find_element(By.CSS_SELECTOR, '#query_ticket').click()

# 选择乘车人
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '#normalPassenger_0').click()

# 选座位
driver.find_element(By.CSS_SELECTOR, '#seatType_1').click()
driver.find_element(By.CSS_SELECTOR, '#seatType_1 > option:nth-child(3)').click()
driver.find_element(By.CSS_SELECTOR, '#seatType_1').click()
driver.find_element(By.CSS_SELECTOR, '#submitOrder_id').click()



