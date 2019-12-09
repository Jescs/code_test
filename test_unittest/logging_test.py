
# Logger：日志，暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效。
#
# LogRecord ：日志记录器，将日志传到相应的处理器处理。
#
# Handler ：处理器, 将(日志记录器产生的)日志记录发送至合适的目的地。
#
# Filter ：过滤器, 提供了更好的粒度控制,它可以决定输出哪些日志记录。
#
# Formatter：格式化器, 指明了最终输出中日志记录的布局。

# logger流程：LogRecord->（Filter）判断->Handler->Filer(判断)logger->Filer(判断)—>输出Logger

# logging.basicConfig(level=logging.DEBUG, format = '%(levelno)s %(levelname)s %(pathname)s %(filename)s %(
# funcName)s' '%(lineno)d %(asctime)s %(thread)d %(threadName)s %(process)d %(message)s', datefmt='%a,
# %d %b %Y %H:%M:%S', filename='log.log')
#
# logging.basicConfig(level=logging.DEBUG, format='%(levelno)s %(levelname)s %(asctime)s %(message)s', filename='log.log', filemode='w')
# logging.debug('This is debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# import logging
#
# logging.basicConfig(filename="log.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     # 下面三种方式三选一，推荐使用第一种
#     logging.exception("Exception occurred")
#     logging.error("Exception occurred", exc_info=True)
#     logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)

import logging
import logging.handlers

logger = logging.getLogger('logger')

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename='log.log',encoding="utf-8",mode='w')

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s ")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)


logger.addHandler(handler1)
logger.addHandler(handler2)

logger.debug('This is debug message,这是debug信息')
logger.info('This is info message，这是info信息')
logger.warning('This is warning message,这是warning信息')
logger.error('This is error message')
logger.critical('This is critical message')