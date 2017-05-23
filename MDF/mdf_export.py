# coding=UTF-8

import pandas as pd
import numpy as np
from mdfreader import mdfreader

###########################################################################
# Set the Actual Values
###########################################################################
#directory = 'D:\\001. 업무폴더\\2017년 업무\\002. 분석 업무\\001. 센서데이터 분석(딥러닝)\\02. 데이터\\1. 이상충격 데이터\정상데이터\\DH\\KMHGN41EBHU162293\\'
#fileName = 'DH_N16-04-143_BM-15C-0191_1937_4_20170320081602_CAN_20170320081229_71173_mdf.dat'

directory = "C:\\mdf\\"
fileName = "AEEV_T16-10-009_BM-15C-0028_1944_3_20170503150016_CAN_20170503145438_82884_mdf.dat"
filePath = directory+fileName
fileExportPath = filePath+'.csv'


#directory = 'D:\\001. 업무폴더\\2017년 업무\\002. 분석 업무\\001. 센서데이터 분석(딥러닝)\\02. 데이터\\1. 이상충격 데이터\\비정상데이터\\원본\\'
#fileName = '170331_HI_3.3TGDi_TMS_check.dat'
#filePath = directory+fileName
#fileExportPath = filePath+'.csv'




###########################################################################
# loads whole mdf file content in yop mdf object
###########################################################################
yop=mdfreader.mdf(filePath) # loads whole mdf file content in yop mdf object
keydic = yop.keys() # list channels names

# master channel list
MasterChannel=yop.masterChannelList


yop.getChannelDesc('TimeChannel_427')
yop.exportToCSV('3.3TGDi_problem.csv')


yop.getChannel('WHL_SPD_FL')
yop.getChannel('WHL_SPD_FL').get('unit')
#'km/h'
yop.getChannel('WHL_SPD_FL').get('data')
#array([ 14.4375, ...,   0.    ])

yop.getChannel('WHL_SPD_FL').get('description')
#'This signal is for the SCC system and higher reolution of wheel speed signal.'

cm_CUR_GR = yop.getChannelMaster('CUR_GR')
cm_N_TC = yop.getChannelMaster('N_TC')
cm_PV_AV_CAN = yop.getChannelMaster('PV_AV_CAN')
cm_N = yop.getChannelMaster('N')

#'CUR_GR','N_TC','PV_AV_CAN' ,'N','VS'



##################################################################
yop.keepChannels(['CUR_GR','N_TC','PV_AV_CAN' ,'N','VS','TEMP_AT','VB','YAW_RATE','LAT_ACCEL','LONG_ACCEL'])

yop.keepChannels(['TQI_ACC','BrakeLight'])

cm_VS = yop.getChannelMaster('TQI_ACC')
yop.resample('0.01',cm_VS)
print(yop.masterChannelList)

yop.getChannelData('CUR_GR')


master_Channel = yop.getChannelMaster('TQI_ACC')
#Gathering Master channel's Size
variable_size = len(yop.masterChannelList.get(master_Channel))
channel_list = yop.masterChannelList.get(master_Channel)




###########################################################################
# Extract certain Channel data using getChannelData
###########################################################################
vs = yop.getChannelData('VS').astype(int)
yop.exportToCSV(fileExportPath)

#yop.masterChannelList # master channel list 전체 채널
#yop.masterChannelList.get('TimeChannel_392')
#yop.resample('0.1', 'TimeChannel_392')
#yop.getChannelData('TQ_STND')

#['TimeChannel_408',
# 'SWI_IGK',
# 'F_N_ENG',
# 'ACK_TCS',
# 'PUC_STAT',
# 'TQ_COR_STAT',
# 'RLY_AC',
# 'F_SUB_TQI',
# 'TQI_ACOR',
# 'N',
# 'TQI_408',
# 'TQFR',
# 'VS',
# 'RATIO_TQI_BAS_MAX_STND']

##############################################################################
# Get Channel Master
##############################################################################
master_Channel = yop.getChannelMaster('VS')

#Gathering Master channel's Size
variable_size = len(yop.masterChannelList.get(master_Channel))
channel_list = yop.masterChannelList.get(master_Channel)

# Time Length
seq_length = len(yop.getChannelData(yop.masterChannelList.get(master_Channel)[0]))

# define create np array with zero values
mge_np = np.zeros((variable_size,seq_length))

##############################################################################
# creating np array
##############################################################################
j=0
for i in yop.masterChannelList.get(master_Channel):
    mge_np[j] = yop.getChannelData(i)
    j = j+1
mge_np_trans  = np.transpose(mge_np)
df = pd.DataFrame(mge_np_trans, columns=channel_list)
df.to_csv('c:\\export.csv', sep=',', encoding='utf-8')
##############################################################################

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
d = np.concatenate((c, a), axis=0)

np.transpose(mge_np)

df = pd.DataFrame(tmp, columns=['vs','takeover'] )
df.to_csv(fileExportPath+fileName, sep=',', encoding='utf-8')
