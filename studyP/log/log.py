#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a hello module '

import logging

import yaml
import logging.config
import os


def setup_logging(default_path='config.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def log():
    dict  = {'name':'ricky','age':15}
    logging.info(dict)
    logging.info('hah\n')
    logging.info('bbbbbbbbb')
    pass
    # logger = logging.getLogger(‘my_moudle’)  获取指定模块
    # logger.error('error.')
    # logger.info('哈哈哈哈')
    # logging.debug('Start')
    # logging.info('Exec')
    # logging.info('Finished')
    # logging.warning('warimg')
    # logging.error('error.....')


def foo(s):
    try:
        return 10 / int(s)
    except Exception as e:
        # print('Error:', e)
        logging.error('Error', exc_info=True)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        logging.error('Error', exc_info=True)
    finally:
        print('finally...')
if __name__ == '__main__':
    yaml_path = 'config.yaml'
    setup_logging(yaml_path)
    log()#
    # main()
    # core.run()