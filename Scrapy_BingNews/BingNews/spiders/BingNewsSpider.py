# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:17:11 2019

@author: franc_000
"""
from BingNews.search_information import SearchInformation
from BingNews.items import BingnewsItem
import scrapy


class BingNewsSpider(scrapy.Spider):
    name="BingNewsCrawler"

    def start_requests(self):
        main_url='https://www.msn.com/en-us/news/'
        
        for category in SearchInformation.category_list :
            print(main_url+category)
            yield scrapy.Request(url=main_url+category, callback=self.parse,headers={'Content-Type':'text/html; charset=UTF-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'})
    
    def parse(self,response) :
        item=BingnewsItem()
        main_url='https://www.msn.com/en-us/news/'
        
        for tag in response.xpath('//*[@id="eventhubriversection1"]/div[@class="rc-container-js"]/div[@class="rc-item-js rc-item show"]') :
            post_url=tag.xpath('./a/@href').get()
            item['url']=main_url+post_url
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            yield item
            yield response.follow(post_url,callback=self.parse)