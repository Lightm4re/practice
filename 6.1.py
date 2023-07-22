from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_top_songs(url):
    k=0
    response = urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    songsnames = soup.find_all(class_='d-track__name')
    if len(songsnames) > 0:
        for i in songsnames:
            print(i.text)
            k+=1
            if k==10:
                break
    else:
        print("На указанной странице отсутствует информация о песнях")
url = input("Введите ссылку на страницу исполнителя на Яндекс музыке: ")
get_top_songs(url)