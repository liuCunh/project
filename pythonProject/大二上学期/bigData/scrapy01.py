from scrapy.selector import Selector
from lxml import etree
data = '''
<!DOCTYPE html>
<html>
	<head>
		<title>超链接网页</title>
	</head>
	<body>
		<h1>热门电影</h1>
		<a href="#">我和我的祖国</a>
		<a href="#">不见不散</a>
		<a href="#">少林寺</a>
		<a href="#">乘风破浪</a>
		<a href="#">朗读者</a>
	</body>
</html>
'''
selector = Selector(text=data)
print(selector.xpath('//html'))
print(selector.xpath('//head'))
print(selector.xpath('//title'))
print(selector.xpath('//body'))
print(selector.xpath('//a'))

html = etree.HTML(data)

res1 = html.xpath('//html')[0].text
print(res1)
res1 = html.xpath('//head')[0].text
print(res1)
res1 = html.xpath('//title')[0].text
print(res1)
res1 = html.xpath('//body')[0].text
print(res1)
res1 = html.xpath('//a')[0].text
print(res1)
