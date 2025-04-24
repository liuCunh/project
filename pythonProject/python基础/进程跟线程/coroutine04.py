import requests
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(url):
    response = urllib.request.urlopen(url)

    content = response.read()
    # print(f"{url} successful!")
    print('下载了{}得数据，长度{}'.format(url, len(content)))


if __name__ == '__main__':
    urls = ['http://www.baidu.com', 'http://www.163.com', 'http://www.qq.com']
    g1 = gevent.spawn(download, urls[0])
    g2 = gevent.spawn(download, urls[1])
    g3 = gevent.spawn(download, urls[2])

    g1.join()
    g2.join()
    g3.join()
    # gevent.joinall(g1, g2, g3)  # 全局阻塞类似于g1.join()
