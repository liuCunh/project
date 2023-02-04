import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def get_info(url):
    wb_data = requests.get(url, headers=header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select("div.pc_temp_songlist>ul>li>a")
    times = soup.select('span.pc_temp_tips_r>span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split("-")[0].strip(),
            'song': title.get_text().split("-")[1].strip(),
            'time': time.get_text().strip()
        }
        print(data)

if __name__ == '__main__':
    url = f"https://www.kugou.com/yy/rank/home/1-6666.html?from=rank"
    get_info(url)
