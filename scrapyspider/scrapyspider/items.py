# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

"""

class DoubanMovieItem(Item):
	# 排名
	ranking = Field()
	# 电影名称
	movie_name = Field()
	# 评分
	score = Field()
	# 评论人数
	score_num = Field()
"""

# weixin.sogou
class weixin_Text(Item):

	title = Field()
	summary = Field()
	name_GZH = Field()
	classifyKind = Field()  #属于哪个分类， 0开始计数  
	publishTime = Field()
	scrapyCrawl_Time = Field()

	def debugprint(self):
		print '\n[title]:'+self['title']+"\n[summary]:"+self['summary']+"\n[name_GZH]:"+self['name_GZH']+"\n[publishTime]:"+self['publishTime']+"\n[scrapyCrawl_Time]:"+self['scrapyCrawl_Time']+"\n"
