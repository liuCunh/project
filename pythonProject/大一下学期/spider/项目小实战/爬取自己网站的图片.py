# 爬取自己网站的图片

import re

with open("../../../paris-clark/index.html", "r", encoding="utf8") as f:
    imgPath = f.read()
# print(imgPath)
imgRule = '<img src="(.*?)" alt=".*">'      # 正则规则
imgPath = re.findall(imgRule, imgPath)      # 正则规则筛选
# fileName = 0
for imgUrl in imgPath:
    # fileName += 1
    imgUrl = f'E:/paris-clark/{imgUrl}'     # 文件地址

    p = imgUrl.rfind("/")           # 切片文件名
    fileName = imgUrl[p+1:-4]         # 打印文件名
    fileFomate = "png"      # 文件后缀名
    # print(fileName, end="\t")
    if imgUrl[p+1:].endswith("jpg"):    # 判断文件后缀
        fileFomate = "jpg"

    with open(imgUrl, 'rb') as f:   # 二进制编码文件
        content = f.read()
    with open(f"./images/{fileName}.{fileFomate}", "wb") as f:      # 二进制解码文件
        f.write(content)
    print(f"{fileName}.jpg\t复制成功")      # 看看有没有成功







