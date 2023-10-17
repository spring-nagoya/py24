import datetime
LOG_DEBUG = 0
LOG_INFO = 1
LOG_WARN = 2
LOG_ERROR = 3
LOG_NON = 4

# 外部にログを保存する為のクラス
class Logger:
    def __init__(self, log_path, log_level):
        self.log_level = log_level
        self.log_path = log_path
        self.log_file = open(self.log_path, 'w',encoding='utf-8')

    def __del__(self):
        self.log_file.close()
        
    def log(self, message):
        print(message)
        self.log_file.write(message + '\n')
    
    def DEBUG(self,message):
        if self.log_level > LOG_DEBUG:
            return
        self.log("{} [DEBUG] mes={}".format(self.timeFormat(),message))    
    
    def INFO(self,message:str):
        if self.log_level > LOG_INFO:
            return
        
        self.log("{} [INFO] mes={}".format(self.timeFormat(),message))    
    
    def WARN(self,message):
        if self.log_level > LOG_WARN:
            return
        self.log("{} [WARN] mes={}".format(self.timeFormat(),message))    
    
    def ERROR(self,message):
        if self.log_level > LOG_ERROR:
            return
        self.log("{} [ERROR] mes={}".format(self.timeFormat(),message))    
        
    def timeFormat(self):
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")