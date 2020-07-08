 #ecoding:utf-8
import win32api
from ReplaceCfg import copyfile
'''
# 运行生成config配置文件,替换config配置文件脚本
win32api.ShellExecute(0, 'open', 'F:\\worksoace\\Test\\getTestcase.py', '','',1)
print "---- create config success ----"
# 运行替换config配置文件脚本
win32api.ShellExecute(0, 'open', 'F:\\worksoace\\Test\\ReplaceCfg.py', '','',1)
print "---- replace config success ----"
# 运行Piflow程序脚本
win32api.ShellExecute(0, 'open', 'F:\\worksoace\\Test\\runExe.py', '','',1)
print "---- run piflow success ----"
# 运行生成日志脚本
win32api.ShellExecute(0, 'open', 'F:\\worksoace\\Test\\runExe.py', '','',1)
print "---- creat log success ----"
'''
copyfile("F:/worksoace/Test/testcase/Octopus_03/config_yy.cfg","F:/test")
print "---- creat log success ----"

'''
import os.path, time
import exceptions
class TypeError (Exception):
  pass
if __name__ == '__main__':
 if (len(os.sys.argv) < 1):
   raise TypeError()
 else:
   print "os.sys.argv[0]: %s" % os.sys.argv[0]
   # os.sys.argv[0] is the current file, in this case, file_ctime.py
 f = os.sys.argv[0]
 mtime = time.ctime(os.path.getmtime(f))
 ctime = time.ctime(os.path.getctime(f))
 print "Last modified : %s, last created time: %s" % (mtime, ctime)

import pylab as pl
import numpy as np
import numpy
numpy.__version__
import matplotlib
matplotlib.__version__
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen

import win32api
 # 运行exe文件
win32api.ShellExecute(0, 'open', 'D:\\Navicat Lite\\navicat.exe', '','',1)
print "---- open navicat success ----"
win32api.ShellExecute(0, 'open', 'F:\\project\\test\Debug\\test.exe', '','',1)
print "---- open  success ----"
'''