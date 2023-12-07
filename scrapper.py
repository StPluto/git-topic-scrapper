import requests
import random
import json
from bs4 import BeautifulSoup
import re
baseurl = "https://github.com"
topic = random.choice(json.load(open('topics.json','r')))
pages = int(input("Enter number of pages: "))
def RecentlyUpdated():
    open('RecentlyUpdated.html', 'w').close()
    for i in range(0,pages):
        print(f"Page: {i + 1}")
        page = str(i)
        link = "https://github.com/topics/" + topic + "?o=desc&s=updated&page=" + page
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')

        posts = soup.find_all('div', 'd-flex flex-justify-between flex-items-start flex-wrap gap-2 my-3')
        ftest = open('test.html','w');
        ftest.write(posts)
        """ f1 = open('RecentlyUpdated.html', 'a', encoding="utf-8")
        for x in posts:
            star = re.search(r'title=\"([0-9, ,])+\"', str(x))
            star = re.sub(r'[title=[\"]', '', star[0])
            star = star.replace(',','')
            repo = re.search(r'href=\"(\/.*\/.*)\"', str(x))
            url = baseurl + repo[1]
            name = re.sub(r'\/.*\/','',repo[1])
            if int(star) > 50:
                f1.write("Repository: " + name + ", Stars - " + star + " Link: <a href=" + url +"> Ссылка </a><br>")
                f1.write('\n')
        f1.close() """
RecentlyUpdated()