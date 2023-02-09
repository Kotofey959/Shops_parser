import requests
from bs4 import BeautifulSoup
from appleperm.templates.main import user_agent

iphone_request_url = 'https://appleperm.ru/modules/addquantitybox/?id_product[]=441&id_product[]=440&id_product[]=439&id_product[]=437&id_product[]=394&id_product[]=393&id_product[]=392&id_product[]=391&id_product[]=390&id_product[]=389&id_product[]=388&id_product[]=384&id_product[]=383&id_product[]=381&id_product[]=380&id_product[]=372&id_product[]=371&id_product[]=370&id_product[]=366&'
ipad_request_url = 'https://appleperm.ru/modules/addquantitybox/?id_product[]=433&id_product[]=432&id_product[]=431&id_product[]=430&id_product[]=428&id_product[]=427&id_product[]=426&id_product[]=425&id_product[]=424&id_product[]=423&id_product[]=422&id_product[]=421&id_product[]=420&id_product[]=418&id_product[]=417&id_product[]=416&'
iphone_name_url = 'https://appleperm.ru/15_apple-iphone-perm'
ipad_name_url = 'https://appleperm.ru/19_apple-ipad-perm'


def get_id_memory_price(request_url, cookies, headers):

    response = requests.get(
        request_url,
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


def get_name(url):

    src = requests.get(url, headers=user_agent).text
    soup = BeautifulSoup(src, 'lxml')
    titles = soup.find_all('h3')
    names=[]
    for title in titles:
        names.append(title.find('a').get('title'))
    return names


