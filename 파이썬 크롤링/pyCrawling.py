import requests
from bs4 import BeautifulSoup

arr = [];

for i in range(0, 1):
    text = "가나다" 
    webpage = requests.get("https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query={}&c_id=&c_name=&sm=tab_pge&kin_start={}".format(text,i)).text
    soup = BeautifulSoup(webpage , "html.parser")

    for v in soup.select("dt.question"):
        arr.append({'title': v.a.text, 'url': v.a.attrs['href']})

print(arr)
