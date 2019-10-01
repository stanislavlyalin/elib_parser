# coding': ' utf-8

import requests

url = 'https://elibrary.ru/org_items.asp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Cookie': 'SUserID=353259792; SCookieID=850404652;',
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

response = requests.post(url=url, headers=headers, data=data)

file = open('resp_text.html', mode='w', encoding='utf8')
file.write(response.text)
file.close()
