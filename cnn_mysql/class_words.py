# -*- coding: UTF-8 -*-

class Words(object):
	
	def __init__(self, tuple_data):

		list_data = list(tuple_data)
		self.id = list_data[0]
		self.value = list_data[1]
		self.frequency = list_data[2]

	def debugPrint(self):
		print self.id,self.value,self.frequency
