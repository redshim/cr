from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request

driver = webdriver.Chrome('D:\Webdriver\chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')
# ID/Password 접근
driver.find_element_by_name('id').send_keys('sredmous')
driver.find_element_by_name('pw').send_keys('dhzpqkfl')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# Naver 사이트 로그인
driver.get('http://cafe.naver.com/ArticleList.nhn?search.clubid=20586673&search.menuid=77')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#soup = BeautifulSoup(urllib.reqeust.urlopen(targetUrl).read()) #해당 웹주소 열고 뷰티풀수프로 긁어온 다음 soup라는 변수에 넣는다.

#notices = soup.select('div.p_inr > div.p_info > a > span')

soup.find_all()
table = soup.find(id="board-box")

#a = table.tbody.findAll('tr')
#print(a)

soup.find_all(attrs={"class": "aaa"})

import re
soup.find(string=re.compile("sisters"))

for n in notices:
    print(n.text.strip())


soup.find_all('span',{'class':'aaa'})
soup.select('span.aaa')



