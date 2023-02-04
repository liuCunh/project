# 我的第一个spider程序

import requests
import re

url = 'https://sc.chinaz.com/tupian/'
response = requests.get(url)
# print(response.status_code)    # 响应的http状态码
# print(response.content)        # 获取响应二进制内容
# print(response.text)           # 获取响应页面的文本
data = response.content.decode("utf8")
# print(data)
imgRule = '<img src="(.*?)" alt=".*">'  # 正则表达式：图片规则
imgName = 0  # 定义图片名字
lists = re.findall(r'<img src="(.*?)" alt=".*">', data)  # 通过规则获取条件数据

for imgUrl in lists:
    imgName += 1
    imgUrl = f'https:{imgUrl}'
    content = requests.get(imgUrl).content
    path = "./images/"+str(imgName)+".jpg"

    with open(f"./images/{imgName}.jpg", 'wb') as f:
        f.write(content)

    print(f"/images{imgUrl}.jpg\b下载成功！")


