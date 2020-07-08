 #ecoding:utf-8
def FtoC(F):
    C=(F-32)*5/9 
    print "C:%f"%C
    
def CtoF(C):
    F=C*9/5+32 
    print "F:%f"%F
def CtoK(C):
    K=C+273.16
    print "K:%f"%K  
def KtoC(K):
    C=K-273.16
    print "C:%f"%C           

k=300
KtoC(k)
c=25
CtoK(c)
