# Парсер
Этот проект представляет собой скрипт на Python для парсинга цитат с сайта quotes.toscrape.com. Скрипт загружает цитаты, авторов и теги с нескольких страниц и сохраняет их в JSON файл quotes2.json.

## Используемые библиотеки и модули
- requests: Для отправки HTTP-запросов и получения HTML страницы.
- BeautifulSoup из библиотеки bs4: Для извлечения данных из HTML.
- json: Для записи полученных данных в файл в формате JSON.
- time: Для добавления задержки между запросами, чтобы избежать блокировки.

## Используемые функции
- scrape_all_quotes(base_url, max_pages)
Проходит по страницам сайта, начиная с первой и до max_pages, и собирает цитаты. Если цитаты закончились до достижения max_pages, цикл прерывается. После парсинга всех доступных страниц функция возвращает список всех цитат.

```sh
def scrape_all_quotes(base_url='https://quotes.toscrape.com/page/', max_pages=100):
    # Логика сбора цитат с нескольких страниц
```

- parse_page(session, url) 
Функция принимает session (экземпляр requests.Session для повторного использования соединения) и url страницы. Возвращает список словарей с цитатами. Парсит страницу с цитатами и извлекает:
  - Текст цитаты.
  - Имя автора.
  - Теги цитаты.

```sh
def parse_page(session, url='https://quotes.toscrape.com/page/1/'):
    # Логика получения и обработки страницы

```

## License
**Free Software**