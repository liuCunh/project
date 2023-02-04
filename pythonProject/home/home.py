import requests
import prettytable as pt
import json
from buy import get_train

with open('city.json', encoding='utf8') as f:
    text = f.read()
    json_data = json.loads(text)  # 将字符串转为json字典数据

# 时间跟地点
from_city = input("出发地点：")
to_city = input("目的地点：")
date = input('出发时间（格式：2022-01-01）：')


# 发送请求
url = 'https://kyfw.12306.cn/otn/leftTicket/query'

data = {
    'leftTicketDTO.train_date': date,
    'leftTicketDTO.from_station': json_data[from_city],
    'leftTicketDTO.to_station': json_data[to_city],
    'purpose_codes': 'ADULT',
}

headers = {
    # 用户信息，检查是否有登录账号
    'Cookie': '_uab_collina=166212604699282273469046; JSESSIONID=45460782256BDFF1589A7F8A211E87B4; BIGipServerotn=451412234.24610.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=870842634.50215.0000; RAIL_EXPIRATION=1662388902581; RAIL_DEVICEID=aIeQy7Ixj7Fj5Ik8m-4WVk1iu0kj9MjeANaTgMrjIUkHnj7JQmColWdHmh3KSrCsM_fFlGCdu9GLazmxg1Rbz8yMwGDu54qgRmz8rKaqgAoZpHH8sKe90uZ8MLY4AXH7MrqzrHPKfYnHLcSubx5L6BWF0te7vZ58; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u5CB3%u9633%2CYYQ; _jc_save_fromDate=2022-09-08; _jc_save_toDate=2022-09-02; _jc_save_wfdc_flag=dc; fo=7ig5dqmsgsrawib9sq2TUrT0ao0UDnnLkDjyRXUAIpVu1ajUhYxy1R3yWWvd_VVAdDOduLId_dm9hJMJECJYxnjmN94j3Bj-PLDE43OxQc2XzabNT5dre2dv55Yp0XMZNnime1CvkSRgzVRC77hLKMgxKUFDH6okVDIzKcLDRkog66GBJVami7igIuI',
    # 用户身份识别标识
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

# 发送参数
response = requests.get(url=url, params=data, headers=headers)

# 解析数据
result = response.json()['data']['result']
tb = pt.PrettyTable()  # 初始化表格

# 初始化表头
tb.field_names = [
    '车次’',
    '列车',
    '出发时间',
    '到达时间',
    '用时',
    '特等座',
    '一等座',
    '二等座',
    '硬卧',
    '硬座',
    '无座',
    '软卧',
]

# lis = []
page = 1

for ind in result:
    content_list = ind.split('|')

    # 车次信息
    num = content_list[3]  # 车次
    start_time = content_list[8]  # 出发
    end_time = content_list[9]  # 到达
    use_time = content_list[10]  # 用时
    topGrade = content_list[32]  # 特等座
    if not topGrade:
        topGrade = content_list[25]
    first_class = content_list[31]  # 一等座
    second_class = content_list[30]  # 二等座
    hard_sleeper = content_list[28]  # 硬卧
    hard_seat = content_list[29]  # 硬座
    no_seat = content_list[26]  # 无座
    soft_sleeper = content_list[23]  # 软卧
    # dit = {
    #     '车次': num,
    #     '出发时间': start_time,
    #     '到达时间': end_time,
    #     '用时': use_time,
    #     '特等座': topGrade,
    #     '一等座': first_class,
    #     '二等座': second_class,
    #     '硬卧': hard_sleeper,
    #     '硬座': hard_seat,
    #     '无座': no_seat,
    #     '软卧': soft_sleeper,
    # }
    # lis.append(dit)

    # 将元素填入表格
    tb.add_row([
        page,
        num,
        start_time,
        end_time,
        use_time,
        topGrade,
        first_class,
        second_class,
        hard_sleeper,
        hard_seat,
        no_seat,
        soft_sleeper
    ])
    page += 2
print(tb)


tmp = int(input('购买的车次：'))
get_train(tmp, from_city, to_city, date)
