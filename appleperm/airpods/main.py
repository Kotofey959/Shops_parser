import requests
from bs4 import BeautifulSoup


def airpods_price():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1135 Yowser/2.5 Safari/537.36'
    }

    src = requests.get('https://appleperm.ru/76_apple-air-pods', headers=headers).text
    soup = BeautifulSoup(src, 'lxml')
    titles = soup.find_all('h3')
    titles_list = []
    for title in titles:
        titles_list.append(title.find('a').get('title'))

    coasts = soup.find_all('div', class_='content_price over')
    coasts_list = []
    for coast in coasts:
        coasts_list.append(coast.find('span', class_='price').get_text())

    res = dict(zip(titles_list, coasts_list))
    return res


airpods_price()