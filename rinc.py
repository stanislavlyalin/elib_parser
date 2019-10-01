# coding': ' utf-8

import requests

# параметры запроса получены с помощью инструментов разработчика chrome
# url = 'https://elibrary.ru/org_items.asp?itembox_name=&pagenum=1&add_all=&paysum=&orgsid=4689&show_refs=1&hide_doubles=1&items_all=&orgdepid=0&rubric_order=0&title_order=0&org_order=0&author_order=0&year_order=1&years_2018=on&type_order=0&types_PRC=on&types_RAR=on&types_CLA=on&types_CNF=on&types_THS=on&types_MIS=on&types_UNK=on&types_BRV=on&types_EDI=on&role_order=0&show_option=0&show_sotr=0&check_show_refs=on&check_hide_doubles=on&sortorder=0&order=1&itemboxid=0'
# url = 'https://elibrary.ru/org_items.asp?pagenum=1&orgsid=4689&show_refs=1&hide_doubles=1&orgdepid=0&rubric_order=0&title_order=0&org_order=0&author_order=0&year_order=1&years_2018=on&type_order=0&types_PRC=on&types_RAR=on&types_CLA=on&types_CNF=on&types_THS=on&types_MIS=on&types_UNK=on&types_BRV=on&types_EDI=on&role_order=0&show_option=0&show_sotr=0&check_show_refs=on&check_hide_doubles=on&sortorder=0&order=1&itemboxid=0'
url = 'https://elibrary.ru/org_items.asp'

headers = {
    'Host': 'elibrary.ru',
    'Connection': 'keep-alive',
    'Content-Length': '348',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'https://elibrary.ru',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://elibrary.ru/org_items.asp?orgsid=4689',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'SUserID=353259792; SCookieID=850404652; _ym_undefined=156996437450412118; _ym_d=1569964374; __utma=216042306.1311932274.1569964374.1569964374.1569964374.1; __utmc=216042306; __utmz=216042306.1569964374.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _ym_isad=2; __utmb=216042306.3.10.1569964374',
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
    'years_2018': 'on',
    'type_order': '0',
    'types_PRC': 'on',
    'types_RAR': 'on',
    'types_CLA': 'on',
    'role_order': '0',
    'show_option': '0',
    'show_sotr': '0',
    'check_show_refs': 'on',
    'check_hide_doubles': 'on',
    'sortorder': '0',
    'order': '1',
    'itemboxid': '0',
}

response = requests.post(url=url, headers=headers, data=data)

file = open('resp_text.html', mode='w', encoding='utf8')
file.write(response.text)
file.close()
