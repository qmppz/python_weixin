# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from utils_parseString import parseAndSaveString
from class_weixinText import WechatString
from class_splitwords import SplitWords
from class_words import Words
from utils_mysql import *
import MySQLdb

import jieba as jb
import jieba.posseg as jb_pssg 
import datetime

a = input("id_min:")
b = input("id_max:")


starttime = datetime.datetime.now()

SQL_SELECT_STRING = "SELECT * "+\
	" FROM view_norepeat WHERE id >= %d AND id < %d; "%(a,b)

# 打开数据库连接
#db = MySQLdb.connect(host="localhost",user="root",passwd="",db="db_weixin",port=3306,charset='utf8')
db = cnnctMysql()

# 使用cursor()方法获取操作游标 
#cursor = db.cursor()


# 使用execute方法执行SQL语句
#cursor.execute("SELECT * FROM view_norepeat WHERE id <= 2 ;")
cursor = executeMysqlSttmnt(db,SQL_SELECT_STRING)

tmp = jb.cut("string",cut_all=True)
# 使用 fetchone() 方法获取一条数据库。
datas = cursor.fetchall()
i=a
myException("--Begin %d - %d"%(a,b),"","")	
for data in datas:

	c_wechat = WechatString(data)
	parseAndSaveString(c_wechat.title,"title",c_wechat.id,db) #'title' is 1; 'summary' is 2
	parseAndSaveString(c_wechat.summary,"summary",c_wechat.id,db)
	if i % 5 == 0 :
		endtime = datetime.datetime.now()
		duringtime = (endtime - starttime).seconds
		speed = float(i)/duringtime
		timeleft = float(float(b-i)/speed)
		myException("--No. %-6d String "%(i),"duringtime:%-6d"%(duringtime),"Speed:%-8.2fitem/sec    Time-left:%-8.2f sec" \
			%(speed,timeleft))	
	i +=1
	#c_wechat.debugPrint()


myException("--End","","")	
outputfile.close()
# 关闭数据库连接
db.close()

	