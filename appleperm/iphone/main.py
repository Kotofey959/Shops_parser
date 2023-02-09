import requests
from bs4 import BeautifulSoup


def get_id_memory_price():
    cookies = {
        '_ym_uid': '1675675253798695215',
        '_ym_d': '1675675253',
        '_ga': 'GA1.2.375178525.1675675253',
        'tmr_lvid': 'e14e814b32f239f2e2b3ebc66d0e8b9c',
        'tmr_lvidTS': '1675675253250',
        '_gid': 'GA1.2.748022728.1675864123',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '5a2c67b4928ffe5745bb882ad7942d17': '4BjHEuVkhzEDenz5YbUXbGrXpK7MXPXdbKQxr97aeq26ORB7mxpq9yyLvfBXTGlEYZ3MtRFNlCE9ZCg36VrTSsRXtJSFF4Dg7l9fCUt724kx4vhXGxXsKS6muhC48jJGBeyuEuhmLghCdD1a0P3UTKb83MifSRS0DL9RMqUp4GqBaUxvjz5OwHAj%2FSv63t6GgLScF3mfN0kCjsoYwC%2B5LA%3D%3D000156',
        'tmr_detect': '0%7C1675870912474',
    }

    headers = {
        'authority': 'appleperm.ru',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9',
        # 'cookie': '_ym_uid=1675675253798695215; _ym_d=1675675253; _ga=GA1.2.375178525.1675675253; tmr_lvid=e14e814b32f239f2e2b3ebc66d0e8b9c; tmr_lvidTS=1675675253250; _gid=GA1.2.748022728.1675864123; _ym_isad=2; _ym_visorc=w; 5a2c67b4928ffe5745bb882ad7942d17=4BjHEuVkhzEDenz5YbUXbGrXpK7MXPXdbKQxr97aeq26ORB7mxpq9yyLvfBXTGlEYZ3MtRFNlCE9ZCg36VrTSsRXtJSFF4Dg7l9fCUt724kx4vhXGxXsKS6muhC48jJGBeyuEuhmLghCdD1a0P3UTKb83MifSRS0DL9RMqUp4GqBaUxvjz5OwHAj%2FSv63t6GgLScF3mfN0kCjsoYwC%2B5LA%3D%3D000156; tmr_detect=0%7C1675870912474',
        'referer': 'https://appleperm.ru/15_apple-iphone-perm',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1135 Yowser/2.5 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(
        'https://appleperm.ru/modules/addquantitybox/?id_product[]=441&id_product[]=440&id_product[]=439&id_product[]=437&id_product[]=394&id_product[]=393&id_product[]=392&id_product[]=391&id_product[]=390&id_product[]=389&id_product[]=388&id_product[]=384&id_product[]=383&id_product[]=381&id_product[]=380&id_product[]=372&id_product[]=371&id_product[]=370&id_product[]=366&',
        cookies=cookies,
        headers=headers,
    ).json()

    list_memory_price = []
    for item in response:
        value = response.get(item).get('a')
        memory_price_dict = {}
        for i in value:
            memory = i.get('attribute_name')
            price = i.get('price')
            memory_price_dict[memory] = price
        list_memory_price.append(memory_price_dict)

    return list_memory_price


def get_name():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1135 Yowser/2.5 Safari/537.36'
    }

    src = requests.get('https://appleperm.ru/15_apple-iphone-perm', headers=headers).text
    soup = BeautifulSoup(src, 'lxml')
    titles = soup.find_all('h3')
    names=[]
    for title in titles:
        names.append(title.find('a').get('title'))
    return names


def get_data():
    id_memory_price = get_id_memory_price()
    names = get_name()
    res = dict(zip(names, id_memory_price))
    print(res)





get_data()