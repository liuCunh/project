import urllib.request
import urllib.parse
import requests
import json
import os
import re
import time


# r = requests.get("http://www.baidu.com")
# print(r.status_code)  # 状态码
# r.encoding = "utf-8"
# bd_data = r.text # 转为文本文件
#
# # 百度翻译
# url = "https://fanyi.baidu.com/sug/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# formData = {
#     "kw": "perfect"
# }
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request, urllib.parse.urlencode(formData).encode())
# responseData = json.loads(response.read().decode("unicode_escape"))
# showDatas = responseData.get("data")[0].get("v")
# print(showDatas)


# 爬取静态网页
# def img_download(path, title):
#     name = title.replace("/", "").strip()
#     try:
#         result = requests.get(path.strip())
#     except:
#         print(path, "Downlaod dailed")
#     else:
#         if result.status_code == 200:
#             with open(name + ".jpg", "wb") as f:
#                 f.write(result.content)
#
# def img_Url(url):
#     result = requests.get(url)
#     result.encoding = "gbk"
#     compile = re.compile(r'<img src="(.*?)" alt="(.*?)" />')
#     all = compile.findall(result.text)
#     for item in all:
#         print(item[0], item[1])
#         img_download(item[0], item[1])
#
# def main(url):
#     for i in range(1, 74):
#         if i == 1:
#             img_Url(url)
#         else:
#             img_Url(f"{url}/index_{i}.html")
#             time.sleep(2)  # 放过爬取过快被屏蔽
#
# if __name__ == '__main__':
#     url = r'http://www.netbian.com'
#     img_Url(url)

def exchange(a):
    a = 10

a = 1
exchange(a)
print(a)

