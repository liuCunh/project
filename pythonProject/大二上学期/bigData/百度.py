import requests
import json
import urllib.request
import urllib.parse

response = requests.get(r"http://www.baidu.com/")
print(response)
response.encoding = 'utf-8'
print(response.text)

print('-'*100)

url = "https://fanyi.baidu.com/sug/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
fromData = {
    "kw": "perfect"
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request, urllib.parse.urlencode(fromData).encode())
responseData = json.loads(response.read().decode("unicode_escape"))
showDatas = responseData.get("data")[0].get("v")
print(showDatas)