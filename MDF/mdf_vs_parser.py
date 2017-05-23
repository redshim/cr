# coding=UTF-8
import pandas as pd
import numpy as np
from mdfreader import mdfreader
import sys
import os


usage = "python mdfparser.py <file path name> <output directory>"
if(len(sys.argv)!=3):
        print usage
        sys.exit(2)

print sys.argv[1]
qt = sys.argv[1]
outputdir = sys.argv[2]

filePath = '%s' %qt

import re
filename=re.search('/([^/]*).mdf',filePath).group(1) #'IG_N16-08-143_BM-15C-0048_2181_4_20170111154033_CAN_20170111042501_75701'
fnameparts=filename.split('_') # ['IG', 'N16-08-143', 'BM-15C-0048', '2181', '4', '20170111154033', 'CAN', '20170111042501', '75701']

fileExportPath = outputdir+'/'+filename+'_vs.csv'

vtype = fnameparts[0] # 'IG'
#number = fnameparts[3] # '2181'
date = fnameparts[5] # '20170111154033'
testarea = filePath.split('/')[5]
#date = date[0:8]

###########################################################################
# loads whole mdf file content in yop mdf object
###########################################################################
yop=mdfreader.mdf(filePath) # loads whole mdf file content in yop mdf object
yop.keys() # list channels names

###########################################################################
# Extract certain Channel data using getChannelData
###########################################################################
vs = yop.getChannelData('VS').astype(int)

# Time Chaneel Get
timeChannel = yop.getChannelMaster('VS')
timeSeq = yop.getChannelData(timeChannel)


###########################################################################
# vehicle_type, time, date population
###########################################################################
vtype_list = []
date_list = []
time_list = []
testArea_list = []
filename_list = []

i = 0
initialTime = timeSeq[i]
for vs_item in vs:
	time_list.append(timeSeq[i] - initialTime)
	vtype_list.append(vtype)
	date_list.append(date)
	testArea_list.append(testarea)
	filename_list.append(filename)
	i = i + 1

#len(vtype_list)
#len(date_list)
#len(time_list)
tmp = zip(time_list,vtype_list,date_list,testArea_list,filename_list,vs)

###########################################################################
# Export to CSV File
###########################################################################

df = pd.DataFrame(tmp, columns=['time','vtype','date','testarea','filename','vs'] )
df.to_csv(fileExportPath, sep=',', encoding='utf-8')
