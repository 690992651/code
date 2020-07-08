#ecoding:utf-8
#绘图
import re
import os
import sys
#创建一个空字典
result={}
varnum=0
variables=[]
Itelist=[]
f=open('result.txt')
lines=f.readlines()
f.close()

for lstr in lines:
    #read title
    if 'TITLE' in lstr.upper():
        dimension=re.findall(r"\d+.?\d*",lstr)
        title=re.findall(r"TITLE(.+?)\n",lstr.upper())
    #read variables
    if 'VARIABLES' in lstr.upper():
        variables=re.findall(r"\"(.+?)\"",lstr.upper())
        varnum=len(variables)
        print varnum
        #初始化列表
        for i in variables:
            result[i] = []
    #lstrl=list()
    lstrl=[i for i in re.split('\s+',lstr) if i not in (' ','')]
    if len(lstrl)==varnum:
        for i in range(0,varnum):
            result[variables[i]].append(lstrl[i])
for i in variables:        
    if "CL" in i:
        name="%s.plt"%i
        file = open(name,'w')
        title="TITLE="+"\""+i+"\"\n"
        file.write(title)
        variables="VARIABLES=Ite,%s\n"%i
        #print variables
        file.write(variables)
        zone=len(result[i])
        file.write("Zone I=%d F=point\n"%zone)
        for k in range (0,len(result[i])):
            file.write("%s %s"%(result["ITE"][k],result[i][k]))
            file.write("\n")  
    elif "CD" in i:    
        name="%s.plt"%i
        file = open(name,'w')
        title="TITLE="+"\""+i+"\"\n"
        file.write(title)
        variables="VARIABLES=Ite,%s\n"%i
        #print variables
        file.write(variables)
        zone=len(result[i])
        file.write("Zone I=%d F=point\n"%zone)
        for k in range (0,len(result[i])):
            file.write("%s %s"%(result["ITE"][k],result[i][k]))
            file.write("\n")   


def Draw(Itelist,datalist,name):
    
    filename=name+r".plt"
    print filename
    file = open(filename,'a')
    file.write('TITLE=+"\%s"',name)
    flie.write('VARIABLES=Ite,%s',name)
    for i in range(0,len(Itelist)):
        file.write(Itelist[i],datalist[i])               
                     
             
