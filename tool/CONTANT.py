# -*- coding: utf-8 -*-
"""
@File  : CONTANT.py
@Author: yintian
@Date  : 2021/3/31 17:42
@Desc  : 
"""
import os

PA = '爬'

RUMOR_PRICE = 5

CARD_PRICE = 3

HOUSE_PRICE = 5

RE_PRICE = {'N': 1, 'R': 3, 'SR': 7}

PROJECT_PATH = os.getcwd()

BOT_PATH = PROJECT_PATH[:PROJECT_PATH.find('bot') + 3]

SQL_PATH = BOT_PATH + r'\ignore\sql.json'

IMG_PATH = {
    'N': BOT_PATH + r'\json_data\N.json',
    'R': BOT_PATH + r'\json_data\R.json',
    'SR': BOT_PATH + r'\json_data\SR.json',
    'SSR': BOT_PATH + r'\json_data\SSR.json',
    'UR': BOT_PATH + r'\json_data\UR.json',
}

pa = '{"message": {"public": "爬", "private": ""}, "code": 0}'

if __name__ == '__main__':
    print()
