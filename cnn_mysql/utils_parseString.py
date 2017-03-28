# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba
import jieba.posseg  
from utils_mysql import *

def parseAndSaveString(string,titleOrSummary,stringId,db):
	"""parse"""
	try:
		seg_list = jieba.cut(string,cut_all=True)
	except Exception as e:
		myException("###1全模式分词","stringId:%d titleOrSummary:%s string:%s"%(stringId,titleOrSummary,string),e)
		return 
	else:
		"""第一次分词成功"""
		for a_seg in seg_list:
			if '' == a_seg:
				continue
			try:
#			posseg_list	 = jieba.posseg.cut(a_seg)
			posseg_list = a_seg
			except Exception as e:
				myException("###2词性分词","stringId:%d titleOrSummary:%s string:%s a_seg:%s"%(stringId,titleOrSummary,string,a_seg),e)
				continue
			else:
				"""第二次分词成功"""
				for posseg_word in  posseg_list:
					if '' == posseg_word:
						continue
#					print posseg_word.word,posseg_word.flag
					print posseg_word

					try:
#						indexOfString = string.find(posseg_word.word)
#						partOfSpeech = posseg_word.flag
						indexOfString = string.find(posseg_word)
						partOfSpeech = "-"
						"""save"""
#						SQLsttmnt = "INSERT INTO t_splitwords VALUE (\'%s\',\'%s\',%d,%d,\'%s\',\'%s\') ;" \
#									%("NULL",posseg_word.word,stringId,indexOfString,titleOrSummary,partOfSpeech)
						SQLsttmnt = "INSERT INTO t_splitwords VALUE (\'%s\',\'%s\',%d,%d,\'%s\',\'%s\') ;" \
									%("NULL",posseg_word,stringId,indexOfString,titleOrSummary,partOfSpeech)
						cursor = executeMysqlSttmnt(db,SQLsttmnt)

					except Exception as e:
						myException("###构造数据并储存","stringId:%d titleOrSummary:%s string:%s posseg_word" \
									":%s"%(stringId,titleOrSummary,string,posseg_word),e)
						continue
					else:
						pass
					finally:
						pass
				  