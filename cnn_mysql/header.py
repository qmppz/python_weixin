# -*- coding: UTF-8 -*-

from header import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from utils_parseString import parseAndSaveString
from class_weixinText import WechatString
from class_splitwords import SplitWords
from class_words import Words
from utils_mysql import *
import MySQLdb

import jieba
import jieba.posseg  

