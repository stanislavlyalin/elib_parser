# coding': ' utf-8

# скрипт сбора ссылок на публикации ВятГУ в eLibrary.ru за указанный год
# результат работы - файл links.txt со ссылками на страницы публикаций

import requests
from bs4 import BeautifulSoup
from utils import unblocked_proxies_generator, response_to_html_file, safe_request

SCookieID = input('SCookieID: ')
SUserID = input('SUserID: ')
year = input('year: ')

url = 'https://elibrary.ru/org_items.asp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Cookie': 'SCookieID=%s;SUserID=%s' % (SCookieID, SUserID),
}

data = {
    'pagenum': '1',
    'orgsid': '4689',
    'show_refs': '1',
    'hide_doubles': '1',
    'orgdepid': '0',
    'rubric_order': '0',
    'title_order': '0',
    'org_order': '0',
    'author_order': '0',
    'year_order': '1',
    'years_%s' % year: 'on',
    'type_order': '0',
    'types_PRC': 'on',
    'types_RAR': 'on',
    'types_CLA': 'on',
    'types_CNF': 'on',
    'types_THS': 'on',
    'types_MIS': 'on',
    'types_SCO': 'on',
    'types_UNK': 'on',
    'types_BRV': 'on',
    'types_EDI': 'on',
    'role_order': '0',
    'show_option': '0',
    'show_sotr': '0',
    'check_show_refs': 'on',
    'check_hide_doubles': 'on',
    'sortorder': '0',
    'order': '1',
    'itemboxid': '0',
}

proxy_gen = unblocked_proxies_generator()

# поисковый запрос с указанными параметрами
proxy = next(proxy_gen)
response, proxy = safe_request(url, headers, data, proxy, proxy_gen)

# получение числа ссылок и страниц выдачи
soup = BeautifulSoup(response.content, 'html.parser')
link_count = int(soup.select_one('td.redref b font').text)
pages_count = link_count // 100 + 1  # 100 ссылок на странице
print('Found %d links' % link_count)

links = []

for page_num in range(1, pages_count + 1):

    # запрос для заданной страницы
    data['pagenum'] = str(page_num)
    response, proxy = safe_request(url, headers, data, proxy, proxy_gen)
    soup = BeautifulSoup(response.content, 'html.parser')

    # собираем ссылки
    page_links = soup.select('tr td a b')
    for link in page_links:
        links.append('https://elibrary.ru' + link.parent['href'])

    print('%d of %d. %d links found' % (page_num, pages_count, len(page_links)))

with open('links.txt', 'w', encoding='utf8') as f:
    for link in links:
        f.write('%s\n' % link)
