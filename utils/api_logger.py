from logging.handlers import TimedRotatingFileHandler
import logging

class ApiLogger():
    def __init__(self,log_file:str="loggerArchi.log",log_level:int = logging.INFO):
        self.handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1,backupCount=7,encoding='utf-8')
        self.handler.setLevel(log_level)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.logger.addHandler(self.handler)
    def get_logger(self):
        return self.logger

def init():
    try:
        global apiLogger
        apiLogger = ApiLogger()
    except Exception as e:
        print(e)