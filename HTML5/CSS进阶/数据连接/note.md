# 数据链接(data url)  
 定义：将目标文件的数据直接书写到路径位置

## 如何书写  
 data:MiME, 数据

## 意义  
 1. 优点：  
  - 减少了数据请求
  - 减少了请求中浪费的时间
  - 有利于动态生成数据

 2. 缺点  
  - 增加了资源的体积，导致传输内容增加，从而增加了单个资源的传输时间
  - 不利于浏览器的缓存，浏览器通常会缓存图片文件、css文件、js文件
  - 会增加原资源的体积到原来的4/3

3. 应用场景  
 - 当请求图片体积较小，并且该图片因为各种原因，不适合制作雪碧图，可以使用数据链接；
 - 图片由代码动态生成，并且图片较小，可以使用数据链接