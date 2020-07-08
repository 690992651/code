#ecoding:utf8
import xlrd, os
import win32api
import logging  
import logging.handlers  
import shutil
import os.path, time
import exceptions          
              
class excleTochart():
        
    def __init__(self):
        
        self._allcaselist = []
        self.AOAlist=[]
        self.machlist=[]  
        self.mach_numlist=[]
          
    def readExcel(self):
        '''
        @brief 获取测试用例数据
        '''
        workbook = xlrd.open_workbook('./chart.xlsx')
        sheet = workbook.sheet_by_name('Octopus')
        ncols = sheet.ncols
        for col in range(ncols):  
            case = sheet.col_values(col)
            self._allcaselist.append(case)
                
    def writeCfg(self, _allcaselist):
        '''
        @brief 将数据转换成tecplot文件
        '''
        for _testcasedic in _allcaselist:
            _filepath = "%s.plt"%_testcasedic[0]
            _chartfile = open(_filepath, 'w')
            zone=len(_testcasedic)
            if "攻角" in _testcasedic[0]:
                for k in range (0,zone):
                    self.AOAlist.append(_testcasedic[k]) 
            if "马赫数" in _testcasedic[0]:
                for k in range (0,zone):
                    self.machlist.append(_testcasedic[k])      
                a = {}
                numlist=[]
                n=0
                for i in self.machlist:
                    try:
                        float(i)
                        if i not in a:
                            a[i] = self.machlist.count(i)       
                    except:
                        continue
                               
            if "升力系数" in _testcasedic[0]:
                title="TITLE=\"cl\"\n"
                _chartfile.write(title)
                variables="VARIABLES=AOA,cl\n"
                _chartfile.write(variables)
                for n in a:
                    _chartfile.write("Zone T=\"mach=%s\" I=%d F=point\n"%(n,a[n]))
                    num=1
                    for i in range(1,len(self.machlist)):
                        if n==self.machlist[i]:
                            _chartfile.write("%s %s\n"%(self.AOAlist[i],_testcasedic[i]))      
            if "阻力系数" in _testcasedic[0]:
                title="TITLE=\"cd\"\n"
                _chartfile.write(title)
                variables="VARIABLES=AOA,cd\n"
                _chartfile.write(variables)
                for n in a:
                    _chartfile.write("Zone T=\"mach=%s\" I=%d F=point\n"%(n,a[n]))
                    num=1
                    for i in range(1,len(self.machlist)):
                        if n==self.machlist[i]:
                            _chartfile.write("%s %s\n"%(self.AOAlist[i],_testcasedic[i]))
            if "轴向力系数" in _testcasedic[0]:
                title="TITLE=\"Xcp\"\n"
                _chartfile.write(title)
                variables="VARIABLES=AOA,Xcp\n"
                _chartfile.write(variables)
                for n in a:
                    _chartfile.write("Zone T=\"mach=%s\" I=%d F=point\n"%(n,a[n]))
                    num=1
                    for i in range(1,len(self.machlist)):
                        if n==self.machlist[i]:
                            _chartfile.write("%s %s\n"%(self.AOAlist[i],_testcasedic[i]))                            
            if "法向力系数" in _testcasedic[0]:
                title="TITLE=\"Ycp\"\n"
                _chartfile.write(title)
                variables="VARIABLES=AOA,Ycp\n"
                _chartfile.write(variables)
                for n in a:
                    _chartfile.write("Zone T=\"mach=%s\" I=%d F=point\n"%(n,a[n]))
                    num=1
                    for i in range(1,len(self.machlist)):
                        if n==self.machlist[i]:
                            _chartfile.write("%s %s\n"%(self.AOAlist[i],_testcasedic[i]))    
            if "俯仰力矩系数" in _testcasedic[0]:
                title="TITLE=\"Cpm\"\n"
                _chartfile.write(title)
                variables="VARIABLES=AOA,Cpm\n"
                _chartfile.write(variables)
                for n in a:
                    _chartfile.write("Zone T=\"mach=%s\" I=%d F=point\n"%(n,a[n]))
                    num=1
                    for i in range(1,len(self.machlist)):
                        if n==self.machlist[i]:
                            _chartfile.write("%s %s\n"%(self.AOAlist[i],_testcasedic[i]))
            if "升阻比" in _testcasedic[0]:
                title="TITLE=\"LD\"\n"
                _chartfile.write(title)
                variables="VARIABLES=AOA,LD\n"
                _chartfile.write(variables)
                for n in a:
                    _chartfile.write("Zone T=\"mach=%s\" I=%d F=point\n"%(n,a[n]))
                    num=1
                    for i in range(1,len(self.machlist)):
                        if n==self.machlist[i]:
                            _chartfile.write("%s %s\n"%(self.AOAlist[i],_testcasedic[i]))                
            print "creat %s chart success"%_testcasedic[0]    


    
    
if __name__ == '__main__':
    G = excleTochart()
    G.readExcel()
    G.writeCfg(G._allcaselist)
