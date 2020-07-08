#ecoding:utf-8
import re 
from thread import *
def countK():
    file_object = open('judge.txt','r') 
    line = file_object.readline( )
    i=0   
    sum=0
    eva=0
    index=0
    Itelist=[]
    RMSlist=[]
    evalist=[]
    indexlist=[]
    klist=[]
    while line: 
    
        test=re.search(r'Ite:?\s+(\b[0-9]*\.*[0-9]+\b)\s+RMS:?\s+(\b[0-9]*\.*[0-9]+\b)', line)
        #print "------test : %s  %s"%(test.group(1),test.group(2))
        Itelist.append(test.group(1))
        RMSlist.append(test.group(2))

        #print "Ite : %s ,RMS : %s"%(Itelist[i],RMSlist[i])
        line = file_object.readline( )
        i=i+1
        #print "--------总行数len : %s"%len(RMSlist)
    for i in  (0,len(RMSlist)-1):
        sum+=float(RMSlist[i])
        i+=1
        if(i%5==0):
            eva=sum/5
            evalist.append(eva)
            index=i/2
            indexlist.append(index)  
            print i
            #i+=1
        else:
            continue 
    for a in evalist:
        print a
        
import numpy as np
 
x = np.arange(1, 17, 1)
y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
 
#第一个拟合，自由度为3
z1 = np.polyfit(x, y, 3)

print(z1)

