import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
baseurl = "https://github.com"
topic = input("Enter the topic ('php','python','html','utilities' ,'chrome' ,'windows' ,'go'):")
pages = int(input("Enter number of pages: "))

async def RecentlyUpdated(pages):
    for i in range(0,pages):
        print(f"Page: {i}")
        page = i
        link = "https://github.com/topics/" + topic + "?o=desc&s=updated&page=" + page
        async with aiohttp.ClientSession() as session:
            response = await requests.get(link).text
            soup = BeautifulSoup(await response, 'lxml')
            posts = soup.find_all('div', 'd-flex flex-justify-between flex-items-start flex-wrap gap-2 my-3')
            tasks = []
        f1 = open('RecentlyUpdated.html', 'w', encoding="utf-8")
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
        f1.close()
RecentlyUpdated(pages)