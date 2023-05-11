import requests
from bs4 import BeautifulSoup
import re
baseurl = "https://github.com"
topic = "python"
f1 = open('posts.txt', 'w', encoding="utf-8")
f1.write('')
f1.close()
for i in range(0,50):
    print(f"Страница: {i}")
    page = str(i)
    link = "https://github.com/topics/" + topic + "?o=desc&s=stars&page=" + page
    print(link)
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    posts = soup.find_all('div', 'd-flex flex-justify-between flex-items-start flex-wrap gap-2 my-3')
    f1 = open('posts.txt', 'a', encoding="utf-8")
    for x in posts:
        star = re.search(r'title=\"([0-9, ,])+\"', str(x))
        star = re.sub(r'[title=[\"]', '', star[0])
        repo = re.search(r'href=\"(\/.*\/.*)\"', str(x))
        url = baseurl + repo[1]
        name = re.sub(r'\/.*\/','',repo[1])
        f1.write("Репозиторий: " + name + ", Звёзд - " + star + " Ссылка: " + url)
        f1.write('\n')
    f1.close()