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
        'tmr_detect': '0%7C1675937001258',
        '5a2c67b4928ffe5745bb882ad7942d17': '4BjHEuVkhzEDenz5YbUXbGrXpK7MXPXdbKQxr97aeq26ORB7mxpq9yyLvfBXTGlEYZ3MtRFNlCE9ZCg36VrTSlTj%2BF4SJmoHU%2Bo6HMtZLL0x4vhXGxXsKS6muhC48jJGBeyuEuhmLghCdD1a0P3UTKb83MifSRS0DL9RMqUp4GqBaUxvjz5OwHAj%2FSv63t6GYRLcGG7boEltH49651Ze%2BA%3D%3D000157',
    }

    headers = {
        'authority': 'appleperm.ru',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9',
        # 'cookie': '_ym_uid=1675675253798695215; _ym_d=1675675253; _ga=GA1.2.375178525.1675675253; tmr_lvid=e14e814b32f239f2e2b3ebc66d0e8b9c; tmr_lvidTS=1675675253250; _gid=GA1.2.748022728.1675864123; _ym_isad=2; tmr_detect=0%7C1675937001258; 5a2c67b4928ffe5745bb882ad7942d17=4BjHEuVkhzEDenz5YbUXbGrXpK7MXPXdbKQxr97aeq26ORB7mxpq9yyLvfBXTGlEYZ3MtRFNlCE9ZCg36VrTSlTj%2BF4SJmoHU%2Bo6HMtZLL0x4vhXGxXsKS6muhC48jJGBeyuEuhmLghCdD1a0P3UTKb83MifSRS0DL9RMqUp4GqBaUxvjz5OwHAj%2FSv63t6GYRLcGG7boEltH49651Ze%2BA%3D%3D000157',
        'referer': 'https://appleperm.ru/19_apple-ipad-perm',
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
        'https://appleperm.ru/modules/addquantitybox/?id_product[]=433&id_product[]=432&id_product[]=431&id_product[]=430&id_product[]=428&id_product[]=427&id_product[]=426&id_product[]=425&id_product[]=424&id_product[]=423&id_product[]=422&id_product[]=421&id_product[]=420&id_product[]=418&id_product[]=417&id_product[]=416&',
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

    src = requests.get('https://appleperm.ru/19_apple-ipad-perm', headers=headers).text
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