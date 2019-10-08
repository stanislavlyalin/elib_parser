# coding: utf-8

import os
import numpy as np
import requests
from utils import unblocked_proxies_generator, response_to_html_file, safe_request, is_elib_blocked
from bs4 import BeautifulSoup
import re
import logging

# инициализация логгера
fh = logging.FileHandler('links_doi.log')
fh.setLevel(logging.DEBUG)
logger = logging.getLogger('elib_parser')
logger.setLevel(logging.INFO)
logger.addHandler(fh)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}

# полный список ссылок
links = []
with open('links.txt') as f:
    for i, url in enumerate(f):
        links.append(url.strip())

logger.info('найдено %d ссылок' % len(links))

if not os.path.exists('visited_links.txt'):
    with open('visited_links.txt', 'w'): pass

# список посещённых ссылок
visited_links = []
with open('visited_links.txt') as f:
    for i, url in enumerate(f):
        visited_links.append(url.strip())

logger.info('просмотрено %d ссылок' % len(visited_links))

# список ссылок для посещения
unvisited_links = list(set(links) - set(visited_links))
np.random.shuffle(unvisited_links)

logger.info('необходимо просмотреть %d ссылок' % len(unvisited_links))

proxy_gen = unblocked_proxies_generator()
proxy = next(proxy_gen)

for i, url in enumerate(unvisited_links):
    print('processing url %s (%d of %d)' % (url, i + 1, len(unvisited_links)))

    response, proxy = safe_request(url, headers, {}, proxy, proxy_gen)

    if not is_elib_blocked(response):
        soup = BeautifulSoup(response.content, 'html.parser')
        doi = soup.select_one('a[href*="doi.org"]')

        if doi:
            # сохраним ссылку на страницу с DOI в файл
            with open('links_doi.txt', 'a', encoding='utf8') as f:
                f.write('%s\n' % url)
            
            logger.info('url %s содержит DOI' % url)

        with open('visited_links.txt', 'a', encoding='utf8') as f:
            f.write('%s\n' % url)
