import logging

class Logs():
    def logs(self):
        logging.basicConfig(level=logging.INFO,filename='test_log.txt',format='%(name)s-%(asctime)s-%(levelname)s-[line:%(lineno)d]-%(message)s')
        logs = logging.getLogger('test_log')
        return logs

if __name__ == '__main__':
    mylog = Logs()
    logs = mylog.logs()
    logs.info('test')