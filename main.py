import requests
from bs4 import BeautifulSoup


KEYWORDS = ['javascript', 'фото', 'web', 'python']
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
           'accept': '*/*'}


def get_articles_by_keywords():
    url = 'https://habr.com/ru/all/'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        hubs = article.find_all('a', class_="tm-article-snippet__title-link") + article.find_all('p')
        for hub in hubs:
            hub_lower = hub.text.lower()
            for key in KEYWORDS:
                if key in hub_lower:
                    date = article.find('time').text
                    title = article.find('a', class_="tm-article-snippet__title-link").text
                    href = url + article.find('a', class_="tm-article-snippet__title-link").get('href')
                    print(f'Дата размещения: {date}. Заголовок: {title}. Ссылка: {href}')



if __name__ == '__main__':
    get_articles_by_keywords()







