# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SplitWords(object):

	def __init__(self,tuple_data):
		
		self.list_data = list(tuple_data)

		self.id = list_data[0]
		self.value = list_data[1]
		self.f_stringId = list_data[2]
		self.indexOfString = list_data[3]
		self.titleOrSummary = list_data[4]
		self.partOfSpeech = list_data[5]

	def debugPrint(self):

		print self.id,self.value,self.f_stringId,self.indexOfString,\
		self.titleOrSummary,self.titleOrSummary