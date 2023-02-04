from bs4 import BeautifulSoup
import requests


def parseHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print('-------------')
    for index, li in enumerate(soup.select('.article li')):
        print(f'歌曲排行: {li.span.text}')
        print(f'歌曲名: {li.find(class_="icon-play").a.text}')
        print('演唱者/播放次数:' + li.find(class_="intro").p.text.split('/')[1].strip())
        print('上榜时间:' + li.find(class_="days").text.strip())


def main():
    url = r'https://music.douban.com/chart'
    parseHtml(url)


if __name__ == '__main__':
    main()
