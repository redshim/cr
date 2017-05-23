#-*- coding: utf-8 -*-  #한글을 쓸 때는 꼭 붙인다. 문자 인코딩을 UTF-8로 하겠다는 것이다. 인코딩은 앞으로 계속 속썩일 것이다.

import urllib.request #URL을 열고 HTML을 읽는 모듈, urllib을 불러온다
from bs4 import BeautifulSoup #bs4모듈에서 뷰티풀수프 함수를 불러옴
import re
import pandas as pd
import time
import math

# url search


#####################################################################################
# 전체 페이지 가져오기(Main)
#####################################################################################
main_url = 'https://e-report.hyundai.com/DBS/autocare/Inspect_list.aspx?'
# https: // e - report.hyundai.com / DBS / autocare / Inspect_list.aspx?p = 1
# https://e-report.hyundai.com/DBS/autocare/Inspect_list.aspx?p=2 2644
iteration_number = round(2644/30,0) + 1
i = 1
search_url=[]
#while(i<=iteration_number):   # 루프를 돌면서 받아옴


while(i<=iteration_number):
    s_tmp = main_url+'p='+ str(i)
    search_url.append(s_tmp)
    i=i+1

#####################################################################################
# 상세 링크 가져오기
#####################################################################################
page_list = []
head_final_list =[]
#search_url = ['https://e-report.hyundai.com/DBS/autocare/Inspect_list.aspx?p=89']
for url in search_url:
    main_page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(main_page, "lxml")
    head_info = 'https://e-report.hyundai.com/DBS/autocare/Inspect_DetailView.aspx?p='
    for x in soup.find_all('a'):  # will give you all a tag
        try:
            if re.match('window.open', x['onclick']):  # if onclick attribute exist, it will match for searchDB, if success will print
                #  print(x['onclick'])        # here you can do your stuff instead of print
                a = re.split(',', x['onclick'])
                tmp = "&" + re.sub("'", "", re.sub("window.open\\(\\'Inspect_DetailView.aspx\\?", "", a[0]))
                sub_url = head_info + tmp
                # sub page조회
                sub = urllib.request.urlopen(sub_url).read()
                sub_soup = BeautifulSoup(sub, "lxml")
                sub_cnt = sub_soup.find("span", id="lblTotalCount").getText()
                print(re.split(" : ", sub_cnt)[1])
                tmp_page_cnt = re.split(" : ", sub_cnt)[1]
                max_sub_url_cnt = math.ceil(int(tmp_page_cnt) / 18)
                print(max_sub_url_cnt)
                vin = x.getText()
                j = 1
                while (j <= max_sub_url_cnt):
                    tmpMge = head_info + str(j) + tmp
                    print(tmpMge)
                    page_list.append(tmpMge)
                    j = j + 1
        except: pass

    #차종 정보 가져오기
    table = soup.find("table", id = "lvHotlineReportList_lvHotlineReportListTable")
    #table = soup.find('table', {'class': 'stdTable_Type1'})
    rows = table.findAll('tr')
    data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

    for k in range(1, len(data)):
        vin_number = "".join(str(x) for x in data[k][1])
        vin_number = re.sub("  ", "", re.sub("\\r", "", re.sub("\\n", "", vin_number)))

        Area = "".join(str(x) for x in data[k][4])
        Area = re.sub("  ", "", re.sub("\\r", "", re.sub("\\n", "", Area)))

        VType = "".join(str(x) for x in data[k][3])
        Vtype = re.sub("  ", "", re.sub("\\r", "", re.sub("\\n", "", VType)))

        head_final = [vin_number, Area, Vtype]
        head_final_list.append(head_final)


#####################################################################################
# page_list에 상세 링크가 저장된다
#####################################################################################
final_list = []
#page_list = ['https://e-report.hyundai.com/DBS/autocare/Inspect_DetailView.aspx?p=1&idx=3717&vin=KMHG241DDHU029471','https://e-report.hyundai.com/DBS/autocare/Inspect_DetailView.aspx?idx=3613&vin=KMHG141DBHU028109']
#https://e-report.hyundai.com/DBS/autocare/Inspect_DetailView.aspx?p=5&idx=3717&vin=KMHG241DDHU029471

for page in page_list:
    #page = 'https://e-report.hyundai.com/DBS/autocare/Inspect_DetailView.aspx?idx=3664&vin=KMHG241DDGU015566'
    print(page)
    time.sleep(1)
    try:
        fb = urllib.request.urlopen(page).read()
        soup = BeautifulSoup(fb,"lxml")
        # header extraction # not working
        #table = soup.find('table', {'class': 'stdTable_Type1'})
        #rows = table.findAll('tr')
        #header_data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

        #  value extraction
        table = soup.find("table", id = "lvHotlineReportList_lvHotlineReportListTable")
        rows = table.findAll('tr')
        data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
        vin = re.findall('=(\w+)', page)[2]

        for k in range(1,len(data)):
            item_name_tmp = "".join(str(x) for x in data[k][0])
            item_name = re.sub("  ","",re.sub("\\r","",re.sub("\\n","",item_name_tmp)))

            result1 = "".join(str(x) for x in data[k][1])
            result1 = re.sub("  ","",re.sub("\\r","",re.sub("\\n","",result1)))

            value1 = "".join(str(x) for x in data[k][3])
            value1 = re.sub("  ","",re.sub("\\r","",re.sub("\\n","",value1)))

            MinVal = "".join(str(x) for x in data[k][5])
            MinVal = re.sub("  ","",re.sub("\\r","",re.sub("\\n","",MinVal)))

            MaxVal = "".join(str(x) for x in data[k][6])
            MaxVal = re.sub("  ","",re.sub("\\r","",re.sub("\\n","",MaxVal)))
            final = [vin, item_name, result1, value1, MinVal, MaxVal]
            final_list.append(final)
    except: pass


#######################################################################################################################
# Export Result to CSV
#######################################################################################################################
hdf = pd.DataFrame(head_final_list, columns=['vin','vtype','area'])
hdf.to_csv('C:\\gdsinside_header_20170309.csv', sep=',', encoding='utf-8')
df = pd.DataFrame(final_list, columns=['vin','testtype','result1','value1','MinVal','MaxVal'])
df.to_csv('C:\\gdsinside.csv_20170309', sep=',', encoding='utf-8')