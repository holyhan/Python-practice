import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    # 拼接路径为/Users/hanyang/test.log
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print('Logging to', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")


# 2018-06-01 11:32:04,673 : DEBUG : Start of the program
# 2018-06-01 11:32:04,673 : INFO : Doing something
# 2018-06-01 11:32:04,673 : WARNING : Dying now

# logging.basicConfig中的format字段的意义如下：
# %(asctime)s : 可读时间格式，比如："2018-06-01 11:32:04,673"，其中最后一项"673"为毫秒
# %(levelname)s : 文本打印级别，比如：('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
# %(message)s: 要打印的内容，比如：Start of the program
