from bs4 import BeautifulSoup
import requests


def info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    msg = soup.select('div.list-con>ul>li>a')
    for title in msg:
        data = {
            'title': title.get_text()
        }
        print(data)


if __name__ == '__main__':
    url = "https://cd.focus.cn/"
    info(url)
