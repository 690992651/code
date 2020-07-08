 #ecoding:utf-8
import logging  
import logging.handlers  
'''LOG_FILE ='/tst.log' 
# 实例化handler  
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) 
'''
# 实例化handler 
handler = logging.FileHandler('log.log', mode='w', encoding='UTF-8')
handler = logging.handlers.RotatingFileHandler('log.log', maxBytes = 1024*1024, backupCount = 5) 
handler.setLevel(logging.NOTSET)

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

print "logging success" 
