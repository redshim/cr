#-*- coding: utf-8 -*-  #한글을 쓸 때는 꼭 붙인다. 문자 인코딩을 UTF-8로 하겠다는 것이다. 인코딩은 앞으로 계속 속썩일 것이다.

import urllib.request #URL을 열고 HTML을 읽는 모듈, urllib을 불러온다
from bs4 import BeautifulSoup #bs4모듈에서 뷰티풀수프 함수를 불러옴

site = 'http://k.autohome.com.cn/spec/26789/view_1468343_1.html?st=1&piap=0|163|0|0|1|0|0|0|0|0|1'

fb = urllib.request.urlopen(site).read()
soup = BeautifulSoup(fb,"lxml")
#soup = BeautifulSoup(urllib.reqeust.urlopen(targetUrl).read()) #해당 웹주소 열고 뷰티풀수프로 긁어온 다음 soup라는 변수에 넣는다.
#print(soup)
#soup.find_all()
#table = soup.find(id="realrank")
#print(table)
#a = table.tbody.findAll('tr')
#print(a)


soup = soup.prettify()


t = soup.find('div' ,attrs={'class':'text-con'})


head = soup.find('div' ,attrs={'class':'kou-tit'})
head.find('h3').text

print(type(head))

t = soup.find('div' ,attrs={'class':'text-con'})
print(type(t))

soup.find_all("div", "text-con")
l1 =  soup.find_all("div", "text-con")
len(l1)

htmls = '<span class="rcnt">8.668</span>'
soup = BeautifulSoup(htmls)
offers =  soup.find_all("span", "rcnt")

print(offers[0].string)           ## this one is better
print(offers[0].renderContents())

soup.find_all("div", class_="text-con")

soup = BeautifulSoup(data, 'html.parser')
for p in soup.find_all('p'):
    if 'style' in p.attrs:
        del p.attrs['style']


rows =soup.find_all('div',attrs={"class" : "text-con"})
print(rows)

for row in soup.find_all('div',attrs={"class" : "text-con"}):
    print(row.text)