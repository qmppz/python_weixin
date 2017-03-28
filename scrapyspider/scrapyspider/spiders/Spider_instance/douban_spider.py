# -*- coding: utf-8 -*-
# @Time     : 2017/1/7 17:04
# @Author   : woodenrobot


from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem
global  pageKind 
global  pageNum 
pageKind = 0
pageNum = 0

class DoubanMovieTop250Spider(Spider):
    name = 'weixin.sogou'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://weixin.sogou.com/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ul[@class="news-list"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/h3/a/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/p/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class =\"s-p\"]/a/text()').extract()[0]
            item['score_num'] = ["null"]
            yield item



     
        global  pageKind
        global  pageNum 
        
        if pageKind < 19  :
            if pageNum < 10:
                url_next= 'http://weixin.sogou.com/pcindex/pc/pc_%d/%d.html' %(pageKind,(pageNum+1))
                pageNum +=1
            else:
                pageKind +=1
                pageNum = 0
                url_next ='http://weixin.sogou.com/pcindex/pc/pc_%d/pc_%d.html'%(pageKind,pageKind)

            print '###pageKind=%d url=%s'%(pageKind,url_next)

        next_url = url_next
        if next_url:
            yield Request(next_url, headers=self.headers)

