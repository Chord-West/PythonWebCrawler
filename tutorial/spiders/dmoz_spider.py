import scrapy
from tutorial.items import DemozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains=["dmoz.org"]
    start_urls =[
        "https://dmoz-odp.org/Computers/Programming/Languages/Python/Books/"
    ]

    # def parse(self,response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename,'wb') as f:
    #         f.write(response.body)

    # def parse(self,response):
    #     for sel in response.xpath('//*[@id="site-list-content"]/div'):
    #         title = sel.xpath('div[3]/a/div/text()').extract()
    #         link = sel.xpath('div[3]/a/@href').extract()
    #         desc= sel.xpath('div[3]/div/text()').extract()
    #         print title,link,desc

    def parse(self, response):
        for sel in response.xpath('//*[@id="site-list-content"]/div'):
            item=DemozItem()
            item['title'] = sel.xpath('div[3]/a/div/text()').extract()
            item['link'] = sel.xpath('div[3]/a/@href').extract()
            item['desc'] = sel.xpath('div[3]/div/text()').extract()
            yield item