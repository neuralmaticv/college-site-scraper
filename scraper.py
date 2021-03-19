from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

URL = 'https://matinf.pmf.unibl.org/%d0%bd%d0%be%d0%b2%d0%be%d1%81%d1%82%d0%b8/?script=lat'

req = Request(URL, headers={'User-Agent': 'Mozilla/86.0.1'})
page = urlopen(req).read()

soup = BeautifulSoup(page, 'html.parser')
results = soup.find(id='main')
section = results.find_all('div', class_="post hentry ivycat-post")


keywords = ["prva", "prve", "informacione", "informacionih", "informatičkog", "programiranje", "tehnologije",
            "Dragan", "Matic", "Matica", "Matić", "Matića", "Milana", "Grbic", "Grbić", "konsultacije", "engleski"]


for news in section:
    title = (news.find('h2')).text
    article = (news.find('p')).text
    for i in keywords:
        if (i in title) or (i in article):
            print(">>>", title)
            print(article, end='\n' * 3)
            break
