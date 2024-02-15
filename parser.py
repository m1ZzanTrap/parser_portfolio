import requests as r
from bs4 import BeautifulSoup as bs
from lxml import etree as et
from time import sleep
from contextlib import redirect_stdout as rs
import urllib.request as ur



def get_url(req):
    p = 1
    url = r.get(f'https://lyzem.com/search?q={req}&f=groups&l=&p={p}&per-page=10')
    soup = bs(url.content, "html.parser")
    dom = et.HTML(str(soup))
    pages = int(dom.xpath('/html/body/div/div[1]/div[2]/ul/li[5]/a')[0].text)
    while p < pages:
        next_url = r.get(f'https://lyzem.com/search?q={req}&f=groups&l=&p={p}&per-page=10')
        soup = bs(next_url.content, "html.parser")
        dom = et.HTML(str(soup))
        for count in range(1, 10):
            try:
                if ur.urlopen(dom.xpath(f"/html/body/div/div[1]/div[1]/div[1]/ul/li[{count}]/div[2]/p[1]/a/@href")[0]).status == 200:
                    print(dom.xpath(f"/html/body/div/div[1]/div[1]/div[1]/ul/li[{count}]/div[2]/p[1]/a/@href")[0])
            except Exception as ex:
                pass
 
        p+=1


def main():
    reQuest = input("Введите запрос: ")
    print("Начинаю поиск...")
    sleep(5)
    print("Записываю в файл...")
    with open("parsed_chats.txt", "w", encoding="utf-8") as f:
        with rs(f):
            get_url(reQuest)
    print("Готово!")
    
    
if __name__=="__main__":
    main()