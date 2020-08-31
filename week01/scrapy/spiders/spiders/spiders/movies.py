import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector
import re
import csv

# 爬取的网页地址
url_local = 'file:///D:/python_learn/geek_github/Python003-003/week01/scrapy/spiders/maoyan.html'

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = [url_local]
    start_urls = [url_local]
    #获取网页内容
    def start_requests(self):
        yield scrapy.Request(url=url_local, callback=self.parse)
    def parse(self, response):
        # pass
        # print(response.text)
        # print(response)
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl')
        # print(movies.extract())
        items = []
        movie_name = movies.xpath(\
            './/dd/div/div/a/div/div/span[contains(@class,"name")]/text()').extract()  # @class="name"//comment()
        # print(movie_name)
        #following-sibling获取span标签外的内容
        movie_type = movies.xpath(\
            './/dd/div/div/a/div/div/span[contains(@class,"hover-tag") and contains(text(),"类型:")]/following-sibling::text()').extract()
        movie_type_list = [re.sub(r'\s+', '', tag) for tag in movie_type]
        # print(movie_type_list)
        # movie_time = movies.xpath(\
        #     './/dd/div/div/a/div/div/span[contains(@class,"hover-tag") and contains(text(),"上映时间:")]/following-sibling::text()').extract()
        movie_time = movies.xpath( \
            './/dd/div/div/a/div/div/span[contains(@class,"hover-tag") and \
            contains(text(),"上映时间:")]/following-sibling::text()').extract()
        #替换换行符和空格等多余格式符
        movie_time_list = [re.sub(r'\s+', '', tag) for tag in movie_time]
        # print(movie_time_list)
        outlist = list(zip(movie_name, movie_type_list, movie_time_list))
        print(outlist)
        outlist_10 = outlist[0:10]
        with open('maoyan_movie.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            head = ['Name', 'Type', 'Date']
            writer.writerow(head)
            for data in outlist_10:
                writer.writerow(data)

