import logging
import logging.handlers

class Logs():
    def __init__(self):
        #创建解释器
        self.logger = logging.getLogger('自动切割log文件')
        #定义解释器的等级
        self.logger.setLevel(logging.DEBUG)
        #格式化日志输出
        self.split_format = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-[line:%(lineno)d]-%(message)s')

    def get_log(self):
        #分割文件处理
        # fh = logging.handlers.RotatingFileHandler(filename='TestLog.txt',mode='a',maxBytes=50,backupCount=3,encoding='utf-8')
        #按照时间分割
        fh = logging.handlers.TimedRotatingFileHandler(filename='timeTestLog.txt',when='s',interval=2,backupCount=3)
        fh.setFormatter(self.split_format)
        self.logger.addHandler(fh)
        return self.logger


if __name__ == '__main__':
    sh = Logs()
    logger = sh.get_log()
    while True:
        logger.info('测试文件切割log')