# coding=UTF-8

import numpy as np
from csv import reader
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

index = 0
column = []
tempData = []
ACCEL_PEDAL_Data = []
ERPM_Data = []
TRPM_AT_Data = []
GEAR_LVL_Data = []
SPEED_Data = []
Time_Data = []

dirname = 'C:\\mdf\\'

#D:\001. 업무폴더\2017년 업무\002. 분석 업무\001. 센서데이터 분석(딥러닝)\02. 데이터\1. 이상충격 데이터\정상데이터\export
file = 'problem_Signal_2.csv'
filename = dirname + file
# 시간
# 악셀패달
# 엔진RPM
# 변속기RPM
# 기어단수
# 속도
#시간	악셀패달	엔진RPM	변속기RPM	기어단수	속도

with open(filename, 'r') as file:
    for line in file:
        fields = line.strip().split(',')

        if index >= 2:
            Time_Data.append(float(fields[0]))
            ACCEL_PEDAL_Data.append(float(fields[1]))
            ERPM_Data.append(float(fields[2]))
            TRPM_AT_Data.append(float(fields[3]))
            GEAR_LVL_Data.append(float(fields[4]))
            SPEED_Data.append(float(fields[5]))

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
plt.plot(Time_Data, ACCEL_PEDAL_Data, 'b')
#plt.xlabel('time')
plt.ylabel('ACCEL_PEDAL_Data')
plt.title('Accel Pedal')
plt.grid(True)

plt.subplot(322)
plt.plot(Time_Data, ERPM_Data, 'g')
#plt.xlabel('time')
plt.ylabel('ERPM_Data')
plt.title('Engine RPM')
plt.grid(True)

plt.subplot(323)
plt.plot(Time_Data, TRPM_AT_Data, 'r')
#plt.xlabel('time')
plt.ylabel('TRPM_AT_Data')
plt.title('Trasmission RPM')
plt.grid(True)

plt.subplot(324)
plt.plot(Time_Data, GEAR_LVL_Data, 'y')
#plt.xlabel('time')
plt.ylabel('GEAR_LVL_Data')
plt.title('GEAR Level')
plt.grid(True)
#fig.canvas.mpl_connect('draw_event', on_draw)


plt.subplot(325)
plt.plot(Time_Data, SPEED_Data, 'y')
plt.xlabel('time')
plt.ylabel('SPEED_Data')
plt.title('Velocity')
plt.grid(True)
#fig.canvas.mpl_connect('draw_event', on_draw)



plt.show()


Time_Data = Time_Data[500:1500]
TRPM_AT_Data = TRPM_AT_Data[500:1500]
ERPM_Data = ERPM_Data[500:1500]

fig = plt.figure(figsize=(50, 50), dpi=100)
plt.plot(Time_Data, TRPM_AT_Data, 'b')
plt.xlabel('time')

plt.plot(Time_Data, ERPM_Data, 'g')
plt.grid(True)
plt.ylabel('RPM Distribution')



