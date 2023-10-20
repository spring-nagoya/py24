import datetime

#const

LOG_DEBUG = 0
LOG_INFO = 1
LOG_WARN = 2
LOG_ERROR = 3
LOG_NONE = 4

class Logger:
    def __init__(self, log_path, log_level, is_print=True ,is_write=True):
        self.log_level = log_level
        self.log_path = log_path
        self.is_print = is_print
        self.is_write = is_write
        
        self.log_message = ""
        
    def write(self):
        with open(self.log_path, 'a',encoding='utf-8') as file:
            file.write(self.log_message + '\n')
            
    def log(self):
        if not self.is_print:
            return
        
        if self.is_write:
            self.write()
            
        print(self.log_message)
    
    def DEBUG(self,message):
        if self.log_level > LOG_DEBUG:
            return
        self.log_message = "{} [DEBUG] mes={}".format(self.timeFormat(),message)
        self.log()    
    
    def INFO(self,message:str):
        if self.log_level > LOG_INFO:
            return
        self.log_message = "{} [INFO] mes={}".format(self.timeFormat(),message)
        self.log()   
    
    def WARN(self,message):
        if self.log_level > LOG_WARN:
            return
        self.log_message = "{} [WARN] mes={}".format(self.timeFormat(),message)
        self.log()    
    
    def ERROR(self,message):
        if self.log_level > LOG_ERROR:
            return
        self.log_message = "{} [ERROR] mes={}".format(self.timeFormat(),message)
        self.log()    
        
    def timeFormat(self):
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")