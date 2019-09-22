# -*- coding: utf-8 -*-

import configparser
import os


class Config:
    # 读取配置文件类
    def __init__(self):
        self.cur_path = os.getcwd()
        self.config_dir = os.path.join(self.cur_path, 'config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(self.config_dir)

    # 获取配置文件的多个配置信息
    def sections(self):
        return self.cf.sections()

    # 获取指定配置的配置信息的所有的键
    def options_named(self, name):
        return self.cf.options(name)

    # 获取指定文件的全部键值对
    def items_named(self, name):
        return self.cf.items(name)

    # 获取指定文件指定的键的值
    def get_named_key(self, name, key):
        return self.cf.get(name, key)


if __name__ == '__main__':
    test = Config()
    t = test.get_named_key('Mysql-Database', 'host')
    print(t)
