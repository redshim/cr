import numpy as np
from csv import reader
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

index = 0
column = []
tempData = []
VS_Data = []
YAW_RATE_Data = []
LAT_ACCEL_Data = []
TEMP_AT_Data = []
PV_AV_CAN_Data = []
CUR_GR_Data = []
N_Data = []
VB_Data = []
N_TC_Data = []
LONG_ACCEL_Data = []
time_Data = []



dirname = 'D:\\001. 업무폴더\\2017년 업무\\002. 분석 업무\\001. 센서데이터 분석(딥러닝)\\02. 데이터\\1. 이상충격 데이터\\업체제공데이터\\정상데이터\\'

#D:\001. 업무폴더\2017년 업무\002. 분석 업무\001. 센서데이터 분석(딥러닝)\02. 데이터\1. 이상충격 데이터\정상데이터\export
file = 'LF_N15-08-046_BM-15C-0012_1171_1_20170313061312_CAN_20170313060900_49376.csv'

filename = dirname + file


#VS
#YAW_RATE
## LAT_ACCEL
## TEMP_AT
# PV_AV_CAN
# CUR_GR
# N
# VB
# N_TC
# LONG_ACCEL
# TimeChannel_408



with open(filename, 'r') as file:
    for line in file:
        fields = line.strip().split(',')
        if index == 0:
                column.append(fields.index('VS'))
                column.append(fields.index('YAW_RATE'))
                column.append(fields.index('LAT_ACCEL'))
                column.append(fields.index('TEMP_AT'))
                column.append(fields.index('PV_AV_CAN'))
                column.append(fields.index('CUR_GR'))
                column.append(fields.index('N'))
                column.append(fields.index('VB'))
                column.append(fields.index('N_TC'))
                column.append(fields.index('LONG_ACCEL'))
                column.append(fields.index('TimeChannel_215'))

          #hearder 부분 제거
        if index >= 2:
            #인덱스 위치로 데이터가져오기
            for i in column:
                tempData.append(fields[i])
            tempData.insert(0, index-1)
            VS_Data.append(float(tempData[1]))
            YAW_RATE_Data.append(float(tempData[2]))
            LAT_ACCEL_Data.append(float(tempData[3]))
            TEMP_AT_Data.append(float(tempData[4]))
            PV_AV_CAN_Data.append(float(tempData[5]))
            CUR_GR_Data.append(float(tempData[6]))
            N_Data.append(float(tempData[7]))
            VB_Data.append(float(tempData[8]))
            N_TC_Data.append(float(tempData[9]))
            LONG_ACCEL_Data.append(float(tempData[10]))
            time_Data.append(float(tempData[11]))

        tempData = []
        index += 1

def on_draw(event):
   bboxes = []
   for label in labels:
       bbox = label.get_window_extent()
       # the figure transform goes from relative coords->pixels and we
       # want the inverse of that
       bboxi = bbox.inverse_transformed(fig.transFigure)
       bboxes.append(bboxi)

   # this is the bbox that bounds all the bboxes, again in relative
   # figure coords
   bbox = mtransforms.Bbox.union(bboxes)
   if fig.subplotpars.left < bbox.width:
       # we need to move it over
       fig.subplots_adjust(left=1.1*bbox.width) # pad a little
       fig.canvas.draw()
   return False


fig = plt.figure(figsize=(50, 50), dpi=100)
plt.subplot(321)
plt.plot(time_Data, VS_Data, 'b')
#plt.xlabel('time')
plt.ylabel('VS_Data')
plt.title('VS Signal')
plt.grid(True)

plt.subplot(322)
plt.plot(time_Data, LAT_ACCEL_Data, 'g')
#plt.xlabel('time')
plt.ylabel('LAT_ACCEL_Data')
plt.title('LAT ACCEL Signal')
plt.grid(True)

plt.subplot(323)
plt.plot(time_Data, N_Data, 'r')
#plt.xlabel('time')
plt.ylabel('N_Data')
plt.title('N SIgnal')
plt.grid(True)

plt.subplot(324)
plt.plot(time_Data, N_TC_Data, 'y')
#plt.xlabel('time')
plt.ylabel('N_TC')
plt.title('N_TC Signal')
plt.grid(True)
#fig.canvas.mpl_connect('draw_event', on_draw)


plt.subplot(325)
plt.plot(time_Data, PV_AV_CAN_Data, 'y')
plt.xlabel('time')
plt.ylabel('PV_AV_CAN_Data')
plt.title('PV_AV_CAN_Data Signal')
plt.grid(True)
#fig.canvas.mpl_connect('draw_event', on_draw)

plt.subplot(326)
plt.plot(time_Data, VB_Data, 'y')
plt.xlabel('time')
plt.ylabel('CUR_GR')
plt.title('CUR_GR Signal')
plt.grid(True)
#fig.canvas.mpl_connect('draw_event', on_draw)



plt.show()




