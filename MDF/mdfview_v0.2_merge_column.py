import pandas as pd
import numpy as np
from mdfreader import mdfreader

filePath = 'C:\mdf\\Normal\\DH_N16-04-143_BM-15C-0191_1937_4_20170320081602_CAN_20170320081229_71173_mdf.dat'
fileExportPath = filePath+'.csv'

filePath1 = 'C:\\mdf\\Normal\\DH_N13-10-264_BM-15C-0011_181_39_20161128180303_CAN_20161128165509_13766.dat'
filePath2 = 'C:\\mdf\\IG_N16-08-143_BM-15C-0048_2181_4_20170111154033_CAN_20170111042501_75701_mdf.dat'

directory = 'D:\\업무폴더\\02. 분석\\2-1. 센서데이터 분석\\02. 데이터\\1. 이상충격 데이터\\정상데이터\\KMHGN41EBHU162293\\'
fileName = 'DH_N16-04-143_BM-15C-0191_1937_4_20170320081602_CAN_20170320081229_71173_mdf.dat'
filePath = directory+fileName

###########################################################################
# loads whole mdf file content in yop mdf object
###########################################################################
yop=mdfreader.mdf(filePath) # loads whole mdf file content in yop mdf object
keydic = yop.keys() # list channels names


###########################################################################
# Extract certain Channel data using getChannelData
###########################################################################
vs = yop.getChannelData('VS').astype(int)
yop.exportToCSV(fileExportPath)


# Time Chaneel Get
#timeChannel = RJ.getChannelMaster('VS')



yop.masterChannelList # master channel list
yop.resample('0.1', 'TimeChannel_392')
yop.masterChannelList.get('TimeChannel_392')
yop.getChannelData('TQ_STND')

#put: `/home/6546788/MDF/FLEET/B3/export/IG_N16-08-143_BM-15C-0048_1585_1_20161013140504_CAN_20161013140046_75701_vs.csv': No such file or directory
#DEPRECATED: Use of this script to execute hdfs command is deprecated.
#Instead use the hdfs command for it.

#put: `/home/6546788/MDF/FLEET/B3/export/IG_N16-08-143_BM-15C-0048_1586_1_20161013153920_CAN_20161013153500_75701_vs.csv': No such file or directory
#DEPRECATED: Use of this script to execute hdfs command is deprecated.
#Instead use the hdfs command for it.

yop.masterChannelList.get('TimeChannel_408')
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
yop.getChannelMaster('VS')


#Get Channel Data
vs = yop.getChannelData('VS').astype(int)
ACC_REQ = yop.getChannelData('ACC_REQ').astype(int)

a1 = yop.getChannelData(yop.masterChannelList.get('TimeChannel_408')[1])
a2 = yop.getChannelData(yop.masterChannelList.get('TimeChannel_408')[2])



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
for i in yop.masterChannelList.get('TimeChannel_408'):
    mge_np[j] = yop.getChannelData(i)
    j = j+1
mge_np_trans  = np.transpose(mge_np)
df = pd.DataFrame(mge_np_trans, columns=channel_list)
df.to_csv('c:\export.csv', sep=',', encoding='utf-8')
##############################################################################

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
d = np.concatenate((c, a), axis=0)

np.transpose(mge_np)

df = pd.DataFrame(tmp, columns=['vs','takeover'] )
df.to_csv(fileExportPath+fileName, sep=',', encoding='utf-8')
