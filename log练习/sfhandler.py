'''
功能描述：实现控制台和文件同时记录日志的功能
实现逻辑：
1-配置日志记录器名称
2-配置日志级别
3-配置日志格式
4、创建并添加handler-控制台
5、创建并添加handler-文件
6、提供对外获取logger
'''
import logging
import sys

def log():
    #创建log解释器
    logger = logging.getLogger('test')
    #配置解释器的日志级别
    logger.setLevel(logging.INFO)
    #配置日志输出格式
    format = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-[line:%(lineno)d]-%(message)s')
    #创建并添加控制台handler
    #创建控制台处理器的实例对象
    sh = logging.StreamHandler()
    #设置控制台的数据输出格式
    sh.setFormatter(format)
    #添加处理器到解释器
    logger.addHandler(sh)
    #创建并添加文件handler
    fh = logging.FileHandler('test_log1.txt',encoding='utf-8')
    fh.setFormatter(format)
    logger.addHandler(fh)

    #解决打印内容重复问题，判断handler是否为空
    #方案二
    # if not logger.handlers:
    #     logger.addHandler(sh)
    #     logger.addHandler(fh)
    #返回解释器
    return logger

#方案一，解决打印内容重复问题
# logger = log()



#面向对象的方式
'''
类：输出日志
属性：解释器、日志等级、日志输出格式
方法：添加控制台handler，添加文件handler
'''
# class Logs():
#     def __init__(self):
#         #创建log解释器
#         self.logger = logging.getLogger('自定义log')
#         #设置log等级
#         self.logger.setLevel(logging.DEBUG)
#         #设置日志输出格式
#         self.format = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-[line:%(lineno)d]-%(message)s')
#
#     def __addStremHandler(self):
#         #创建handler对象
#         sh = logging.StreamHandler()
#         sh.setFormatter(self.format)
#         self.logger.addHandler(sh)
#
#     def __addFileHandler(self):
#         fh = logging.FileHandler('test_log2.txt',encoding='utf-8')
#         fh.setFormatter(self.format)
#         self.logger.addHandler(fh)
#
#     def getLogs(self):
#         self.__addStremHandler()
#         self.__addFileHandler()
#         return self.logger

if __name__ == '__main__':
    # logger = log()
    # logger.info('输出日志到控制台和文件的测试')
    # l = Logs()
    # logger = l.getLogs()
    # logger.info('test自定义log')
    pass