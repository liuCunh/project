import requests
import re

url = 'http://47.119.115.25/'  # 网站
response = requests.get(url)  # 访问
data = response.content.decode('utf8')  # 解码
# print(response)
# print(response.status_code)
# print("response.content.decode=", response.content.decode('utf8'))
# 转换欸html文件
# with open('./HTML/阳哥的网站.html', 'w', encoding='utf8') as f:
#     f.write(data)
imgRule = '<img src="(.*?)" alt=".*">'  # 正则表达式：筛选图片规则
ruleEndImg = re.findall(imgRule, data)  # 利用规则对图片进行筛选

# 下载图片
for imgUrl in ruleEndImg:
    imgUrl = f'http://47.119.115.25/{imgUrl}'
    Url = requests.get(imgUrl)
    imgCode = Url.content  # 对图片进行二进制编码
    # 判断文件后缀名
    imgEnd = '.png'  # 文件后缀名
    position = imgUrl.rfind('/')  # 查找文件名前的/
    fileName = imgUrl[position+1:-4]  # 文件名
    if imgUrl[position+1:].endswith('.jpg'):
        imgEnd = '.jpg'

    # 对文件进行下载
    with open(f'./images/{fileName}{imgEnd}', 'wb') as f:
        f.write(imgCode)

    print(f'{fileName}{imgEnd}\t下载成功！')





