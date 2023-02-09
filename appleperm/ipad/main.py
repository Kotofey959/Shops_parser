from appleperm.templates.main import ipad_cookies, ipad_headers
from appleperm.templates.iphone_ipad import ipad_request_url, ipad_name_url, get_name, get_id_memory_price


def get_ipad_data():
    id_memory_price = get_id_memory_price(ipad_request_url, ipad_cookies, ipad_headers)
    names = get_name(ipad_name_url)
    res = dict(zip(names, id_memory_price))
    print(res)

