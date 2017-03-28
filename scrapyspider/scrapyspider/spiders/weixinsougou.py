
# -*- coding: utf-8 -*-
# @Time	 : 2017/03/21 10:54
# @Author   : RenjiaLu

import time
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapyspider.items  import weixin_Text

global	crawlNum	#爬取数量
global	outputfile
global	SQL_StmtFile
global  pageKind 
global  pageNum 


str = time.strftime('%Y_%m_%d__%H_%M_%S',time.localtime(time.time()))

crawlNum = 21
outputfile = open("log_%s.txt"%str, "a+")
SQL_StmtFile = open("SQLstmt_%s.txt"%str, "a+")
pageKind = 0
pageNum = 0

SQL_StmtFile.write("USE db_weixin;\n")

class weixin_TextSpider(Spider):

	name = 'weixin.sogou'
	handle_httpstatus_list = [404, 500]
	download_delay = 1
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}

	def start_requests(self):
		url = 'http://weixin.sogou.com/'
		#url="http://weixin.sogou.com/pcindex/pc/pc_3/15.html"
		yield Request(url, headers=self.headers)

	def parse(self, response):

		global crawlNum
		global outputfile
		global	SQL_StmtFile
		global pageKind
		global pageNum
		item = weixin_Text()

		try:
			if response.status in self.handle_httpstatus_list:
				outputfile.write(str(response.status))
				raise Exception(Exception,response.status)
	
			#outputfile.write(str(response.status))
			
			if pageNum == 0 :
				#第 0 页
				weixinSelector = response.xpath('//ul[@class="news-list"]/li')
			else:
				#第 1+ 页
				weixinSelector = response.xpath('//body//li')

			if weixinSelector:
				#获取到了 一个weeixin_Text的 List
				for weixin in weixinSelector:
					item['title'] = weixin.xpath(
						'.//div[@class="txt-box"]/h3/a/text()').extract()[0].encode("utf-8").replace(",", "，").replace("\"","“").replace("\'","‘")
					item['summary'] = weixin.xpath(
						'.//p/text()').extract()[0].encode("utf-8").replace(",", "，").replace("\"","“").replace("\'","‘")
					item['name_GZH'] = weixin.xpath('.//div[@class =\"s-p\"]/a/text()').extract()[0].encode("utf-8")
					item['classifyKind'] = pageKind
					item['publishTime'] = "-"
					item['scrapyCrawl_Time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

					SQL_StmtFile.write("INSERT INTO weixin_Text(id,classifyKind,scrapyCrawl_Time,title,name_GZH,publishTime,summary) "+\
						" VALUE(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");\n" 
						%("NULL",	item['classifyKind'],item['scrapyCrawl_Time'],item['title'],item['name_GZH'],item['publishTime'],item['summary']))
					yield item
			else:
				outputfile.write("###[LOG] 当前页面没有匹配到内容 pageKind=%d,pageNum=%d \n"%(pageKind,pageNum))
				pageNum = crawlNum
		except Exception as e:
			print e
			outputfile.write("###[LOG] 异常 e=%s\n\n"%e)
			pageNum = crawlNum
		else:
			outputfile.write("正常")
		finally:

			if pageKind < crawlNum  :
				if pageNum < crawlNum:
					pageNum +=1
					url_next= 'http://weixin.sogou.com/pcindex/pc/pc_%d/%d.html' %(pageKind,(pageNum))
				else:
					#一个分类栏的 第 0 页
					pageKind +=1
					pageNum = 0
					url_next ='http://weixin.sogou.com/pcindex/pc/pc_%d/pc_%d.html'%(pageKind,pageKind)

				outputfile.write("--下一个链接 pageKind=%d url=%s \n"%(pageKind,url_next))

		  	else:
		  		outputfile.write("爬取结束 pageKind=%d" %pageKind)
		  		outputfile.close()
		  		SQL_StmtFile.close()
			
			next_url = url_next
			if next_url:
				yield Request(next_url, headers=self.headers)



 