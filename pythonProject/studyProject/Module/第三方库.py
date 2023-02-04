# 第三方库
import requests

response = requests.get("http://www.12306.cn/")
print(response.text)



