# -*- coding: utf-8 -*-
# @Time     : 2017/03/21 10:51
# @Author   : RenjiaLu


from scrapy import cmdline


name = 'weixin.sogou'
cmd = 'scrapy crawl {0} -o wxsg.csv'.format(name)
cmdline.execute(cmd.split())