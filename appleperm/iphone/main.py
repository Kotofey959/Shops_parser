from appleperm.templates.main import iphone_cookies, iphone_headers
from appleperm.templates.iphone_ipad import get_id_memory_price, get_name, iphone_request_url, iphone_name_url


def get_iphone_data():
    id_memory_price = get_id_memory_price(iphone_request_url, iphone_cookies, iphone_headers)
    names = get_name(iphone_name_url)
    res = dict(zip(names, id_memory_price))
    print(res)
