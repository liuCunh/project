from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
def get_info(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.select('div.news_list-1dYUdgWQ>p>a')
    print(titles[0])
    for title in titles:
        data = {
            "标题": title.get_text()
        }
        print(data)
if __name__ == '__main__':
    url = r'https://www.ifeng.com/'
    get_info(url)
