#ecoding:utf8

import xlrd, os
import win32api
import logging  
import logging.handlers  
import shutil

import os.path, time
import exceptions

class TypeError (Exception):
    pass  

class MetaexcleTocfg:
    def run(self):
        res = self.readExcel()
        self.writeCfg(res)    
    def readExcel(self):
        pass 
    def writeCfg(self):
        pass     
              
class excleTocfg(MetaexcleTocfg):
        
    def __init__(self):
        self.testitem=[]
        
    def readExcel(self):
        '''
        @brief 获取测试用例数据
        '''
        workbook = xlrd.open_workbook('./testcase.xlsx')
        sheet = workbook.sheet_by_name('Octopus')
        _allcaselist = []
        ncols = sheet.ncols
        for col in range(ncols):
            if col == 0:
                self.testitem = sheet.col_values(col)[1:]
            else:
                case = sheet.col_values(col)
                caseid = case[0]
                casedata = case[1:]
                _testcasedic = self.testcasedic()
                _testcasedic['id'] = caseid
                
                for index, item in enumerate(self.testitem):
                   
                    _testcasedic['testdata'][item] = casedata[index]
                
                _allcaselist.append(_testcasedic)
        return _allcaselist
    
    #获得文件创建时间和修改时间
    def getTime(self,_filepath):
        if (len(os.sys.argv) < 1):
            raise TypeError()
        else:
            print ("os.sys.argv[0]: %s" % os.sys.argv[0])
        # os.sys.argv[0] is the current file, in this case, file_ctime.py
        f = os.sys.argv[0]
        file=_filepath+'/config_yy.cfg'
        mtime = time.ctime(os.path.getmtime(file))
        ctime = time.ctime(os.path.getctime(file))
        print ("Last modified : %s, last created time: %s" % (mtime, ctime))
               
    def writeCfg(self, _allcaselist):
        '''
        @brief 将测试用例数据转换成config_yy.cfg文件
        '''
        _filedir0 = os.path.join(os.getcwd(), 'testcase') 
        for _testcasedic in _allcaselist:

            id = _testcasedic['id']
            _filedir=os.path.join(_filedir0,id)
            print (id)
            if not os.path.exists(_filedir):
                os.makedirs(_filedir)
            _filepath = _filedir + '/config_yy.cfg'
            _testcasefile = open(_filepath, 'w')
            _testdata = _testcasedic.get('testdata', None)
            print ("create floder success")
            for key in self.testitem:
                value = self.datatrans(_testdata.get(key, None)) 
                explain = self.addexplain(key)
                writestr = key + '=' + value + '    '*4+'%' + explain + '\n'
                _testcasefile.write(writestr)
                
            print ("write config success")
            #获得文件创建时间和修改时间
            self.getTime(_filedir) 
            
            _testcasefile.close() 
             
            #将生成的config文件复制到指定文件夹
            self.copyfile(_filepath, "F:/test")

            
            #将piflow生成的log文件，拷贝到测试用例文件夹中
            #self.copyfile("F:/test/config_yy.cfg",_filepath)
            
            #合并piflow日志文件到测试用例日志中
            #self.copylog(self,piflow_log, test_log)
            
            '''#调用python脚本
            win32api.ShellExecute(0, 'open', 'F:\\worksoace\\case\\src\\test\\__init__.py', '','',1)
            print "---- open python success ----"
            '''
     
            #生成测试日志文件
            self.logging(_filedir)
            
    def datatrans(self, data):
        '''
        @brief 将数据类型转换成STR类型
        '''
        if isinstance(data, float):
            if int(data) == data:
                return str(int(data))
            else:
                return str(data)
        else:
            return str(data)
    
    def testcasedic(self):
        '''
        @brief 用例字典
        '''
        _testcase = {}
        _testcase['id'] = None
        _testcase['desc'] = None
        _testcase['testdata'] = {}
        _testcase['exc'] = None
        _testcase['act'] = None
        _testcase['state'] = None
        
        return _testcase
    
    def copyfile(self,sourceFile,targetDir):
        if os.path.exists(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            shutil.copy(sourceFile, targetDir)
        else:
            print ("待复制的文件不存在或路径错误")
     
    #生成日志文件    
    def logging(self,_filedir):
        LOG_FILE = _filedir+'/log.log' 
        # 实例化handler 
        handler = logging.FileHandler(LOG_FILE, mode='w', encoding='UTF-8') 
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) 
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
        # 实例化formatter
        formatter = logging.Formatter(fmt)
        # 为handler添加formatter     
        handler.setFormatter(formatter)        
        # 获取名为tst的logger 
        logger = logging.getLogger('log')  
        # 为logger添加handler    
        logger.addHandler(handler)            
        logger.setLevel(logging.DEBUG)  
  
        logger.info('first info message')  
        logger.debug('first debug message')
        logger.error('first error message') 
        print ("logging success")
    
    #合并piflow日志文件到测试用例日志中 
    def copylog(self,piflow_log,test_log):
       with open(piflow_log,'r') as flog: 
           with open(test_log,'w') as tlog: 
                 tlog.write(flog.read())
    
    #添加config内容           
    def addexplain(self, key):
        if key == 'PHYSICAL_PROBLEM':
            explain = 'Physical governing equations'
        elif key == 'RESTART_SOL':
            explain = 'Restart solution (N0,YES)'
        elif key == 'MACH_NUMBER':
            explain = 'Mach number (non-dimensional)'
        elif key == 'AOA':
            explain = 'Angle of attack (degrees)'
        elif key == 'AOS':
            explain = 'Angle of sideslip (degrees)'
        elif key == 'FREESTREAM_PRESSURE':
            explain = 'Free_stream pressure (101325.0 N/m^2 by default)'
        elif key == 'FREESTREAM_TEMPERATURE':
            explain = 'Free_stream temperature (273.15 K by default)'          
        elif key == 'GAMMA_VALUE':
            explain = 'Ratio of specific heats (1.4 (air))'
        elif key == 'GAS_CONSTANT':
            explain = 'Specific gas constant (287.87 J/kg*K (air))'   
        elif key == 'CFL_NUMBER':
            explain = 'Courant-Friendrichs-Lewy conditions'
        elif key == 'EXT_ITER':
            explain = 'Number of total iterations'
        elif key == 'START_CONVERGE_EVAITER':
            explain = 'Number of iterations before evaluating the convegence'
        elif key == 'MESH_FILENAME':
            explain = 'Mesh input file testNewSolverFile_pinban.bat testNewSolverFile.dat'
        elif key == 'RESTART_FILENAME':
            explain = 'Restart flow output file'
        elif key == 'RESIDUAL_MINVAL':
            explain = 'Min value of the residual (log10 of the residual)'
        elif key == '%SOLUTION_FLOW_FILENAME':
            explain = 'Restart flow input file'
        elif key == 'OUTPUT_FORMAT':
            explain = 'Output file format (TECPLOT,PARAVIEW,TECPLOT_BINARY)'
        elif key == 'NON_DIM_STRATEGY':
            explain = 'Flow non-dimensionalization (DIMENSIONAL,FREESTREAM_PRESS_EQ_ONE)'  
        elif key == 'DEBUG':
            explain = 'Is Debuging the Solver ?(NO,YES)'
        elif key == 'DEBUG_CELL_ID':
            explain = 'Which cell is going to be debugged?'
        elif key == 'SIMULATION_KIND':
            explain = 'simulation strategy (STEADY OR UNSTEADY)'
        elif key == 'LAMINAR_VISC_MODEL':
            explain = 'Laminar Viscosity model'
        elif key == 'SUTHERLAND_MU_REF':
            explain = 'Mu reference in Ns/m2'
        elif key == 'SUTHERLAND_T_REF':
            explain = 'T reference in K'
        elif key == 'SUTHERLAND_S_CONST':
            explain = 'sutherland const in K'    
        elif key == 'INlET_PRESSURE':
            explain = 'Inlet_stream pressure (101325.0 N/m^2 by default)' 
        elif key == 'INlET_TEMPERATURE':
            explain = 'Inlet_stream temperature (273.15 K by default)' 
        elif key == 'OUTlET_PRESSURE':
            explain = 'Outlet_stream pressure (101325.0 N/m^2 by default)' 
        elif key == 'OUTlET_TEMPERATURE':
            explain = 'Outlet_stream temperature (273.15 K by default)'           
        elif key == 'AUTO_SAVE_STEP':
            explain = 'Number of iterations intervals between two save actions'
        else:
            explain = ''

        return explain
        
    
if __name__ == '__main__':
  
    G = excleTocfg()
    G.run()
