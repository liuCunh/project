import requests
import prettytable as pt  # 表格格式化输出
import json
import 回家的诱惑


f = open('city.json', encoding='utf-8')
txt = f.read()
json_data = json.loads(txt)  # open函数打开默认为字符串需要用json模块转换为字典类型数据
from_station = input('请输入你出发的城市：')
to_station = input('请输入你出目的城市：')
date = input('请输入你要出发的日期(格式：2020-05-24)：')

# 发送请求
url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station' \
      f'={json_data[from_station]}&leftTicketDTO.to_station={json_data[to_station]}&purpose_codes=ADULT'

# 身份标识
headers = {
    'Cookie': 'JSESSIONID=47917791EED29DD3E5DCFE9F501EF3FA; tk=WYf8KWOBM3twu8nXj1L8M8BsizhtygvfvoFXMzzi5AclmD1D0; '
              'BIGipServerotn=1089470986.64545.0000; BIGipServerpool_passport=165937674.50215.0000; guidesStatus=off; '
              'highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1655754603336; '
              'RAIL_DEVICEID=B5b9BPVTpW1ktcxn8Q8asF9qz8EPQDud506_L03kzgCsh6A8p20HdFfSL'
              '-ZHMDDGeDNuUWrRvCef0TTHs9BUNj_HdWf2nzAuj9bxpDDQvfXOcrQhx4zfswr_L1zoa'
              '-274kFQdEEeWKOy0ayYHsCLrOMlJnaK9gXq; route=6f50b51faa11b987e576cdb301e545c4; '
              '_jc_save_fromStation=%u91CD%u5E86%2CCQW; _jc_save_toStation=%u5E7F%u5B89%u5357%2CVUW; '
              '_jc_save_toDate=2022-06-17; _jc_save_wfdc_flag=dc; current_captcha_type=Z; '
              'uKey=59e884c51b7332c4288897bda4c81b761ecd4d437950d72c000ffa4135283d64; _jc_save_fromDate=2022-06-22',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41 '
}

# 通过requests数据请求模块里面的get方法，对于url地址发送请求，并且携带上headers请求头伪装，最后用response接收返回数据
response = requests.get(url=url, headers=headers)   # <Response [200]> 请求成功，返回响应对象

# 2、获取数据
print(response.json())

# 3、解析数据，提取我们想要的内容
tb = pt.PrettyTable()
tb.field_names = [
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等',
    '二等',
    '软卧',
    '硬卧',
    '硬座',
    '无座',
]
page = 1  # 车次
for index in response.json()['data']['result']:  # 把列表中的元素一个一个提取出来，用for循环遍历
    # index.split('|')
    info = index.split('|')
    num = info[3]   # 车次
    start_time = info[8]    # 出发时间
    end_time = info[9]  # 到达时间
    use_time = info[10]  # 耗时
    topGrade = info[32]    # 特等座
    first_class = info[31]     # 一等
    second_class = info[30]    # 二等
    soft_sleeper = info[23]     # 软卧
    hard_seat = info[29]    # 硬座
    no_seat = info[26]  # 无座
    hard_sleeper = info[28]     # 硬卧
    # dit = {
    #     '车次': num,
    #     '出发时间': start_time,
    #     '到达时间': end_time,
    #     '耗时': use_time,
    #     '特等座': topGrade,
    #     '一等': first_class,
    #     '二等': second_class,
    #     '软卧': soft_sleeper,
    #     '硬卧': hard_sleeper,
    #     '硬座': hard_seat,
    #     '无座': no_seat,
    # }
    tb.add_row([
        page,
        num,
        start_time,
        end_time,
        use_time,
        topGrade,
        first_class,
        second_class,
        soft_sleeper,
        hard_sleeper,
        hard_seat,
        no_seat,
    ])
    page += 2

print(tb)

word = int(input('请输入你想要购买的车票：'))
回家的诱惑.get_train(word, from_station, to_station, date)








