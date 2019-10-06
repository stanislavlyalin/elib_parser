# coding: utf-8

import numpy as np
import time
import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    # 'Cookie': 'SUserID=353259792; SCookieID=850404652;',
    # 'Cookie': 'SUserID=353259425; SCookieID=850402712;',
}

proxies = [
    '23.97.101.222:80',
    '183.111.25.67:8080',
    '51.158.113.142:8811',
    '157.245.0.181:3128',
    '198.98.58.178:8080',
    '118.163.96.167:3129',
    '51.79.141.93:8080',
    '147.139.132.52:3128',
    '139.180.144.37:8080',
    '139.99.218.212:8080',
    '49.49.17.245:8080',
    '1.245.107.123:3128',
    '146.185.192.26:3128',
    '51.79.25.12:8080',
    '177.130.143.22:8080',
    '139.255.89.91:3128',
    '18.228.88.101:8080',
    '157.230.45.105:8080',
    '51.79.29.44:8080',
    '125.165.118.69:8080',
    '163.172.189.32:8811',
    '139.99.217.114:8080',
    '187.109.122.109:53330',
    '116.90.229.186:52090',
    '201.236.237.55:45846',
    '85.175.226.106:41175',
    '212.90.168.150:52589',
    '118.27.5.147:3128',
]

# полный список ссылок
links = []
with open('links.txt') as f:
    for i, url in enumerate(f):
        links.append(url.strip())

# список посещённых ссылок
visited_links = []
with open('visited_links.txt') as f:
    for i, url in enumerate(f):
        visited_links.append(url.strip())

# список ссылок для посещения
unvisited_links = list(set(links) - set(visited_links))
np.random.shuffle(unvisited_links)

links_doi = []

for i, url in enumerate(unvisited_links):
    
    print('processing url %s (%d of %d)' % (url, i, len(unvisited_links)))

    np.random.shuffle(proxies)

    for proxy in proxies:
        try:
            # пауза от 2 до 10 секунд
            time.sleep(np.random.randint(2, 11))

            response = requests.get(url=url, headers=headers, proxies={'https': proxy}, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            if not soup.select_one('div#blockedip'):
                doi = soup.select_one('a[href*="doi.org"]')
                if doi:
                    print(url)

                    with open('links_doi.txt', 'a', encoding='utf8') as f:
                        f.write('%s\n' % url)

                    m = re.search('\d+', url)
                    if m:
                        q = open('page_%s.html' % (m.group(0)), 'w', encoding='utf8')
                        q.write(response.text)
                        q.close()

                with open('visited_links.txt', 'a', encoding='utf8') as f:
                    f.write('%s\n' % url)

                break
            else:
                print('proxy %s is blocked' % (proxy))

        except:
            pass

with open('links_doi.txt', 'w', encoding='utf8') as f:
    for link in links_doi:
        f.write('%s\n' % link)
