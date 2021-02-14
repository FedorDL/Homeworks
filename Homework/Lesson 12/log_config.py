# <дата - время> Функция дринк водка вызвана из функции врепер

import logging
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO, filename='my_log.txt')
logging.info('Функция drink_vodka водка вызвана из функции wrapper')


def log(func):
    def wrapper():
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                            level=logging.INFO, filename='my_log.txt')
        func()
        logging.info('Функция drink_vodka водка вызвана из функции wrapper')
    return wrapper

