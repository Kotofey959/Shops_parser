import requests
from bs4 import BeautifulSoup
from appleperm.templates.main import user_agent


def airpods_price():

    src = requests.get('https://appleperm.ru/76_apple-air-pods', headers=user_agent).text
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
