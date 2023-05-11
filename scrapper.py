import requests
from bs4 import BeautifulSoup
import re
baseurl = "https://github.com"
topic = input("Enter the topic ('php','python','html','utilities' ,'chrome' ,'windows' ,'go'):")
pages = int(input("Enter number of pages: "))
mode = int(input("Enter the mode (MostStars = 1, RecentlyUpdated = 2):"))
def MostStars(pages):
    for i in range(0,pages):
        f = open('MostStars.txt', 'w', encoding="utf-8")
        f.write('')
        f.close()
        print(f"Page: {i}")
        page = str(i)
        link = "https://github.com/topics/" + topic + "?o=desc&s=stars&page=" + page
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')
        posts = soup.find_all('div', 'd-flex flex-justify-between flex-items-start flex-wrap gap-2 my-3')
        f = open('MostStars.txt', 'w', encoding="utf-8")
        for x in posts:
            star = re.search(r'title=\"([0-9, ,])+\"', str(x))
            star = re.sub(r'[title=[\"]', '', star[0])
            repo = re.search(r'href=\"(\/.*\/.*)\"', str(x))
            url = baseurl + repo[1]
            name = re.sub(r'\/.*\/','',repo[1])
            f.write("Repository: " + name + ", Stars - " + star + " Link: " + url)
            f.write('\n')
        f.close()

def RecentlyUpdated(pages):
    for i in range(0,pages):
        print(f"Page: {i}")
        page = str(i)
        link = "https://github.com/topics/" + topic + "?o=desc&s=updated&page=" + page
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')
        posts = soup.find_all('div', 'd-flex flex-justify-between flex-items-start flex-wrap gap-2 my-3')
        f1 = open('RecentlyUpdated.txt', 'a', encoding="utf-8")
        for x in posts:
            star = re.search(r'title=\"([0-9, ,])+\"', str(x))
            star = re.sub(r'[title=[\"]', '', star[0])
            star = star.replace(',','')
            repo = re.search(r'href=\"(\/.*\/.*)\"', str(x))
            url = baseurl + repo[1]
            name = re.sub(r'\/.*\/','',repo[1])
            if int(star) > 100:
                f1.write("Repository: " + name + ", Stars - " + star + " Link: " + url)
                f1.write('\n')
        f1.close()
if mode == 1:
    MostStars(pages)
else:
    RecentlyUpdated(pages)