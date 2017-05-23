# -*- coding: utf-8 -*-
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import csv
import warnings
import numpy
import sys


index = 0
column = []         #header 정보
tempData = []
CF_Ems_IsgStat_Data = []
vehicle_type_list = []
save_date_list = []
filename_list = []
timeData = []


usage = "python mdfparser.py <file path name> <output directory>"
if(len(sys.argv)!=3):
        print usage
        sys.exit(2)

qt = sys.argv[1]
outputdir = sys.argv[2]


filePath = "C:\\mdf\\CB_N17-01-252_BM-16L-0073_553_1_20170418062659_CAN_20170417192329_95888_decoded.csv"
#
# filePath = '/home/6546788/MDF/KJH/CB_N17-01-252_BM-16L-0073_587_1_20170419195738_CAN_20170419195315_95888_decoded.csv'
filePath = qt

import re
filename=re.search('/([^/]*).csv',filePath).group(1) #'IG_N16-08-143_BM-15C-0048_2181_4_20170111154033_CAN_20170111042501_75701'
fnameparts=filename.split('_') # ['IG', 'N16-08-143', 'BM-15C-0048', '2181', '4', '20170111154033', 'CAN', '20170111042501', '75701']


filepathToCsv = outputdir+'/'+filename+'.csv'

print (">>> start: " + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

vehicle_type = fnameparts[0]
save_date = fnameparts[7]
#vehicle_type = 'CK'
#save_date = '20170101'
filename = filePath

# 파일 가져오기
#with open("/home/6546788/MDF/test2.txt", 'r') as file:
with open(filePath, 'r') as file:
    for line in file:
        fields = line.strip().split(',')
        if index == 0:
            column.append(fields.index('Time'))
            column.append(fields.index('CF_Ems_IsgStat'))

#hearder 부분 제거
        if index >= 2:
            #인덱스 위치로 데이터가져오기
            for i in column:
                tempData.append(fields[i])
            tempData.insert(0, index-1)
            timeData.append(tempData[1])
            CF_Ems_IsgStat_Data.append(float(tempData[2]))
#시간정보
            vehicle_type_list.append(vehicle_type)
            save_date_list.append(save_date)
            filename_list.append(filename)

        tempData = []
        index += 1


#tmp = zip(timeData,vehicle_type_list,save_date_list,CF_Ems_IsgStat_Data,filename_list)
#print(tmp)

df = pd.DataFrame({'time':timeData, 'vtype' : vehicle_type_list, 'save_date' : save_date_list, 'CF_Ems_IsgStat' : CF_Ems_IsgStat_Data,'filename' : filename_list})
cols = ['time', 'vtype','CF_Ems_IsgStat', 'filename', 'save_date']
df = df[cols]
df.to_csv(filepathToCsv, sep=',', encoding='utf-8')

print (">>> end: " + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
