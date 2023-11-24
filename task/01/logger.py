import datetime
import abc

LOG_DEBUG = 0
LOG_INFO = 1
LOG_WARN = 2
LOG_ERROR = 3
LOG_NON = 4

# ロガーのインターフェース
class LoggerBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def DEBUG(self, message):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def INFO(self, message):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def WARN(self, message):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def ERROR(self, message):
        raise NotImplementedError()

class Logger(LoggerBase):
    def __init__(self, log_path, log_level):
        self.log_level = log_level
        self.log_path = log_path
        self.log_message = ""
    
    def Write(self):
        with open(self.log_path, mode='a', encoding='utf-8') as f:
            f.write(self.log_message+'\n')
        
    def log(self):
        print(self.log_message)
        return self
    
    def DEBUG(self,message):
        if self.log_level > LOG_DEBUG:
            return
        
        self.log_message = "{} [DEBUG] mes={}".format(self.timeFormat(),message)
        return self.log()
    
    def INFO(self,message:str):
        if self.log_level > LOG_INFO:
            return
        
        self.log_message = "{} [INFO] mes={}".format(self.timeFormat(),message)
        return self.log()    
    
    def WARN(self,message):
        if self.log_level > LOG_WARN:
            return
        
        self.log_message = "{} [WARN] mes={}".format(self.timeFormat(),message)
        return self.log()
    
    def ERROR(self,message):
        if self.log_level > LOG_ERROR:
            return
        
        self.log_message = "{} [ERROR] mes={}".format(self.timeFormat(),message)
        return self.log()
        
    def timeFormat(self):
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")