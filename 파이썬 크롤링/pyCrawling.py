import requests
from bs4 import BeautifulSoup

#webpage = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={}".format("가나다")).text
webpage = requests.get("https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EA%B0%80%EB%82%98%EB%8B%A4&c_id=&c_name=&sm=tab_pge&kin_start=1").text
soup = BeautifulSoup(webpage , "html.parser")
b = "dt.question"
for v in soup.select(b):
    print(v.a.text)
    #print(v.a)
