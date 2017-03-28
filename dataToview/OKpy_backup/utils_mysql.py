# -*- coding: UTF-8 -*-

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb

str = time.strftime('%Y_%m_%d__%H_%M_%S',time.localtime(time.time()))
outputfile = open("log/log_%s.txt"%str, "a+")

def cnnctMysql(pHost="localhost",pUser="root",pPasswd="",pDb="db_weixin",pPort=3306,pCharset='utf8'):
	"""连接 mysql 数据库"""
	try:
		db = MySQLdb.connect(host=pHost,user= pUser,passwd=pPasswd,db=pDb,port=pPort,charset=pCharset)
		db.autocommit(1)
		return db
	except Exception as e:
		myException("###连接数据库","",e)
	else:
		print '操作成功'
	finally:
		pass


def executeMysqlSttmnt(db,sqlSttmnt):
	"""执行 mysql 语句 
		返回 cursor
	"""
	try:
		cursor = db.cursor()
		cursor.execute(sqlSttmnt)	
		return cursor
	except Exception as e:
		myException("###执行Mysql语句",sqlSttmnt,e)
		db.rollback() # 回滚事件
	else:
		print '操作成功'
	finally:
		pass


def closeMysql(db):
	"""关闭数据库"""
	try:
		db.close()
	except Exception as e:
		myException("###关闭数据库","",e)

	else:
		print '操作成功'
	finally:
		pass

def myException(whichStep,log,e):
	str = "###myException whichstep:%s log:%s e:%s\n"%(whichStep,log,e)
	print str
	try:
		outputfile.write(str)
	except Exception as e:
		print e