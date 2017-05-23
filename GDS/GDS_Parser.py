import os
import sys

usage = "python parse.py <fully qualified filename>"
if(len(sys.argv)!=2):
        print usage
        sys.exit(2)

file=sys.argv[1]
file='/home/6546788/GDS_Mobile/src/LF/20161117_141605_KMHE341CBFA076589.csv'


#/home/6546788/GDS_Mobile/src/test.csv
import re
filename=re.search('/([^/]*).csv',file).group(1)
print filename

#20161117_141605_KMHE341CBFA076589
fnameparts=filename.split('_')
file_ts=fnameparts[0]+fnameparts[1]

f=open(file,'r')
#Test Results
first=f.readline()

#20161027_1358
f.readline()

#Model : LF CAR
third=f.readline()
tparts=third.replace(" ","").split(":")
model=tparts[1].replace("\n","")
print(model)

#Vehicle Number :
f.readline()

#VIN : KMHC051HFHU000192
fifth=f.readline()
fparts=fifth.replace(" ","").split(":")
vin=fparts[1].replace("\n","")
print(vin)

#Engine : 2000 CC
sixth=f.readline()
parts6=sixth.replace(" ","").split(":")
engine=parts6[1].replace("\n","")

#Transmission : 6SP AUTO
seventh=f.readline()
parts7=seventh.replace(" ","").split(":")
transmission=parts7[1].replace("\n","")

#ODO
f.readline()

#Customer Name
f.readline()

#Inspection Serial No.
eightth=f.readline()
parts8=eightth.split(" ")
isn=parts8[3].replace("\n","")

f.readline()

##End Of Information


#Inspection Items,Result,1st Value,2nd Value,Min,Max,Comment
#전방 안개등_2.0MPI,0,5.60,,5.0,7.0,
count=0
for line in f:
    count+=1
    lparts=line.split(",")
    iitem=lparts[0]
    result=lparts[1]
    value1=lparts[2]
    value2=lparts[3]
    min=lparts[4]
    max=lparts[5]

    row = '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' %(file_ts,model,vin,engine,transmission,isn,iitem,result,value1,value2,min,max)

    print row
