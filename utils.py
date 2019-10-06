# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup

# получение списка бесплатных https-прокси-серверов
def free_https_proxies():
    response = requests.get('https://free-proxy-list.net/')

    ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{2,6}', response.text)
    is_https = re.findall(r'<td class=\'hx\'>(yes|no)</td>', response.text)

    proxies = [ip.replace('</td><td>', ':') for ip in ips]
    https = [1 if 'yes' in p else 0 for p in is_https]

    return [proxies[i] for i in range(len(https)) if https[i] == 1]

# проверка, заблокирован ли IP сервером eLibrary, по ответу response
def is_elib_blocked(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    return True if soup.select_one('div#blockedip') else False

# генератор незаблокированных proxy-серверов
def unblocked_proxies_generator():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    
    for proxy in free_https_proxies():
        try:
            response = requests.get(
                url='https://elibrary.ru/item.asp?id=35022119',
                headers=headers,
                proxies={'https': proxy},
                timeout=10)
            
            if not is_elib_blocked(response):
                print('selected proxy: %s' % proxy)
                yield proxy
        except:
            pass

# безопасный запрос
# пытается выполнять запрос к url с разных proxy до тех пор, пока не будет получен ответ
# если исчерпали список proxy, вернёт пустой response
def safe_request(url, headers, data, proxy, proxies_gen):
    success = False
    while not success:
        try:
            response = requests.get(url,
                headers=headers,
                data=data,
                proxies={'https': proxy},
                timeout=10)

            if not is_elib_blocked(response):
                success = True
        except:
            try:
                proxy = next(proxies_gen)
            except StopIteration:
                return requests.models.Response(), proxy

    return response, proxy

# сохранение ответа в заданный файл
def response_to_html_file(response, filename):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(response.text)
