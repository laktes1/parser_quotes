import requests
from bs4 import BeautifulSoup
import time
import json


def get_headers():
    """Возвращает заголовки для имитации браузера."""
    return {
        "Accept": "text/html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    }


def parse_page(session, url='https://quotes.toscrape.com/page/1/'):
    """Парсит страницу с цитатами и возвращает список цитат с авторами и тегами."""
    try:
        response = session.get(url, headers=get_headers())
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при запросе {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'lxml')
    quotes = []

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            'Text': text,
            'Author': author,
            'Tags': tags
        })

    return quotes


def scrape_all_quotes(base_url='https://quotes.toscrape.com/page/', max_pages=100):
    """Собирает все цитаты подряд со всех страниц до конца или до max_pages."""
    all_quotes = []
    with requests.Session() as session:
        for i in range(1, max_pages + 1):
            url = f"{base_url}{i}/"
            page_quotes = parse_page(session, url)

            if not page_quotes:
                print(f"Цитаты закончились на странице {i}.")
                break

            all_quotes.extend(page_quotes)  # Добавляем все цитаты с текущей страницы в общий список
            time.sleep(1)  # Задержка для избежания блокировки

    return all_quotes

if __name__ == "__main__":
    # Запуск парсинга
    try:
        quotes_data = scrape_all_quotes(base_url='https://quotes.toscrape.com/page/')
    except Exception as e:
        print('Ошибка при парсинге: '+str(e))

    # Запись данных в файл в формате JSON
    try:
        with open('quotes2.json', 'w', encoding='utf-8') as json_file:
            json.dump(quotes_data, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print('Ошибка при сохранении: '+str(e))
    finally:
        print("Цитаты успешно сохранены в файл quotes2.json")