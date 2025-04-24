from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By


def get_train(num, from_station, to_station, date):
    driver = webdriver.Chrome()

    # 解决特征识别
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {"source": """Object.defineProperty(navigator, "webdriver", {get: () => false,});"""})

    # 账号密码输入
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    driver.find_element(By.ID, 'J-userName').send_keys('15082699769')  # 输入账号
    driver.find_element(By.ID, 'J-password').send_keys('wad2020520')  # 输入密码
    driver.find_element(By.ID, 'J-login').click()  # 点击登录

    # # 滑动验证
    # # 等待2秒钟，不要点的太快，以免被识别或者以免网页加载跟不上。
    # time.sleep(2)
    #
    # # 定位 滑块标签
    # span = driver.find_element_by_id('nc_1_n1z')
    # actions = ActionChains(driver) # 行为链实例化
    # time.sleep(2) # 等待2秒钟
    #
    # # 经截图测量，滑块需要滑过的距离为300像素
    # actions.click_and_hold(span).move_by_offset(300, 0).perform() # 滑动

    driver.implicitly_wait(10)  # 延时等待
    driver.find_element(By.CSS_SELECTOR, '.modal-ft .btn ').click()
    driver.find_element(By.CSS_SELECTOR, "#link_for_ticket").click()  # 点一下车票按钮

    # 出发地
    driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(Keys.ENTER)  # 再来回车一下
    driver.find_element(By.CSS_SELECTOR, '#fromStationText').clear()  # 清空内容
    driver.find_element(By.CSS_SELECTOR, '#fromStationText').click()  # 点击一下准备输入
    driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(from_station)  # 输入出发地
    driver.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(Keys.ENTER)  # 回车确定

    # 目的地
    driver.implicitly_wait(10)  # 延时等待
    driver.find_element(By.CSS_SELECTOR, '#toStationText').clear()  # 清空内容
    driver.find_element(By.CSS_SELECTOR, '#toStationText').click()  # 点击一下准备输入
    driver.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(to_station)  # 输入目的地
    driver.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(Keys.ENTER)  # 回车确定

    # 出发时间
    time.sleep(1)  # 等待
    driver.find_element(By.CSS_SELECTOR, '#train_date').clear()  # 清空内容
    driver.find_element(By.CSS_SELECTOR, '#train_date').click()  # 点击一下准备输入
    driver.find_element(By.CSS_SELECTOR, '#train_date').send_keys(date)  # 输入时间
    driver.find_element(By.CSS_SELECTOR, '#query_ticket').click()  # 点击确认

    # 买票
    """
    #queryLeftTable 标签的id名字
    tr 需要定位的标签
    :nth-child(3) 定位的地址有点像指针
    .btn72 按钮id
    """
    driver.find_element(By.CSS_SELECTOR, f'#queryLeftTable tr:nth-child({num}) .btn72').click()  # 点击买票
    driver.find_element(By.CSS_SELECTOR, '#normalPassenger_0').click()  # 点击乘车人
    driver.find_element(By.CSS_SELECTOR, '#submitOrder_id').click()  # 点击提交订单
    """
    #erdeng1 > 最外层的标签id
    ul:nth-child(4) 二层标签位置
    li:nth-child(2)三层标签的位置
    """
    # try:
    #     driver.find_element(By.CSS_SELECTOR, '#erdeng1 > ul:nth-child(4) li:nth-child(2)').click()  # 选位置
    # except Exception as err:
    #     print(err)
    time.sleep(9999)