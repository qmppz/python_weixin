# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from genWordCloud import *
from utils_mysql import *

SQL_SELECT_STRING = "SELECT * FROM simpleview_splitwords "\
					"WHERE frequency > 40;"
print '连接数据库中'
db = cnnctMysql()
cursor = executeMysqlSttmnt(db,SQL_SELECT_STRING)
datas = cursor.fetchall()
dict_data = {}
print '获取数据中'
for data in datas:
	dict_data[data[1].decode("utf-8")] = data[2]

print '生成词云中'
genWordCloud(dict_data)

print '结束'


