# -*- coding: UTF-8 -*-

class WechatString(object):

	def __init__(self,tuple_data):

		list_data = list(tuple_data)
		self.repeatNum = list_data[0]
		self.id = list_data[1]
		self.classifyKind = list_data[2]
		self.date_scrapyCrawl = list_data[3]
		self.title = list_data[4] 
		self.name_GZH = list_data[5] 
		self.publishTime = list_data[6]
		self.summary = list_data[7] 
 
 	def debugPrint(self):
 		
		print self.repeatNum,self.id,  \
			self.classifyKind,self.date_scrapyCrawl,self.title,self.name_GZH , \
			self.publishTime,self.summary
