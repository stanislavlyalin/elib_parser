# elib_parser
Скрипт сбора данных с сайта elibrary.ru

Скрипт **links.py** позволяет получить список ссылок на публикации авторов ВятГУ за указанный год. Результат работы скрипта - файл links.txt. При запуске необходимо указать параметры: **SCookieID**, **SUserID**, **year**. Первые два параметра можно узнать так:
1. открыть в браузере сайт eLibrary.ru
2. очистить cookies для сайта
3. открыть инструменты разработчика - мониторинг сетевых запросов
4. выполнить любой поисковый запрос. Искомые значения можно найти в поле **Cookies**.

Скрипт **doi_page_downloader.py** позволяет скачать по сформированным ранее ссылкам html-страницы, содержащие DOI.
