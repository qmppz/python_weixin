# -*- coding:utf-8 -*-
from utils_mysql import *
import MySQLdb
db = cnnctMysql()
id=0
while id < 20 :

	num=10
	SQL_SELECT_STRING = "SELECT * FROM view_classifykind_word_fre "+\
		" WHERE classifykind_1 = %d ORDER BY ck_frequency DESC LIMIT %d "%(id,num)

	# 打开数据库连接
	#db = MySQLdb.connect(host="localhost",user="root",passwd="",db="db_weixin",port=3306,charset='utf8')

	list_All=[]

	cursor = executeMysqlSttmnt(db,SQL_SELECT_STRING)
	# 使用 fetchone() 方法获取一条数据库。
	datas = cursor.fetchall()
	print '数据获取完成'
	i=0

	sum=0
	list_value=[]
	list_fre=[]
	for data in datas:
		list_value.append(data[1])
		list_fre.append(data[2])
		i+=1

	print '#%s'%(id)
	print "[",
	for a in list_value:
		print a,",",
	print "]\n[",
	for b in list_fre:
		print b,",",

	print "]"
	print ""
	print '#END'
	id+=1