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
NAB_Data = []
HDK_Data = []
mmm_Data = []
RGA_CUR_Data = []
NTU_Data = []
NMO_Data = []
vfz_Data = []
timeData = []

qt = sys.argv[1]

#filePath = "/home/6546788/MDF/ImgAna/uncaved.dat.csv"
filePath = qt
filepathToCsv = filePath+'.csv'

print (">>> start: " + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

# 파일 가져오기
#with open("/home/6546788/MDF/test2.txt", 'r') as file:
with open(filePath, 'r') as file:
    for line in file:
        fields = line.strip().split(',')
        if index == 0:
            column.append(fields.index('NAB'))
            column.append(fields.index('HDK'))
            column.append(fields.index('mmm'))
            column.append(fields.index('RGA_CUR'))
            column.append(fields.index('NTU'))
            column.append(fields.index('NMO'))
            column.append(fields.index('vfz'))

#hearder 부분 제거
        if index >= 2:
            #인덱스 위치로 데이터가져오기
            for i in column:
                tempData.append(fields[i])
            tempData.insert(0, index-1)
            NAB_Data.append(float(tempData[1]))
            HDK_Data.append(float(tempData[2]))
            mmm_Data.append(float(tempData[3]))
            RGA_CUR_Data.append(float(tempData[4]))
            NTU_Data.append(float(tempData[5]))
            NMO_Data.append(float(tempData[6]))
            vfz_Data.append(float(tempData[7]))
#시간정보
            timeData.append(tempData[0])

        tempData = []
        index += 1

df = pd.DataFrame({'time':timeData, 'NAB' : NAB_Data, 'HDK' : HDK_Data, 'mmm' : mmm_Data,'RGA_CUR' : RGA_CUR_Data,
                   'NTU' : NTU_Data, 'NMO' : NMO_Data,'vfz' : vfz_Data})

df.to_csv(filepathToCsv, sep=',', encoding='utf-8')

print (">>> end: " + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))