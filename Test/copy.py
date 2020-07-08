#ecoding:utf-8
import  os
import shutil
def copyfile(sourceFile,targetDir):
    if os.path.exists(sourceFile):
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        shutil.copy(sourceFile, targetDir)
    else:
        print "待复制的文件不存在或路径错误"
            
#copyfile("F:/worksoace/Test/testcase/Octopus_03/config_yy.cfg","F:/test")