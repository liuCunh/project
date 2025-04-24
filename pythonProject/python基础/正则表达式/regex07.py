import re
msg = "abc123abc"

# 默认贪婪, 如果想将贪婪模式变成非贪婪模式，在量词后加？
result = re.match(r"abc(\d+?)", msg)
print(result)

path = '<img src="//scpic.chinaz.net/files/default/imgs/2022-09-26/dbe5e6fc967e606d_s.jpg" style="height: 299px; display: block;" data-original="//scpic.chinaz.net/files/default/imgs/2022-09-26/dbe5e6fc967e606d_s.jpg" class="lazy" alt="748人体艺术个人写真摄影图片">'

result = re.match(r'<img src="(.+?)"', path)
images_path = "https:"+result.group(1)

import requests
response = requests.get(images_path)
with open(r'aa.png', 'wb') as wstream:
    wstream.write(response.content)



