# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/new100.html']
    #第一个被获取到的页面，后续的url则从出事的url获取到的数据中提取。

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = TutorialItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            #item['URL'] = ?
            yield item
#parse（）是spider的一个方法。被调用时，每个初始URL完成下载后生成的Response对象将会作为唯一
#的参数传递给该函数。该方法负责解析返回的数据，提取数据（生成item）以及生成需要进一步处理的URL
#的request对象
