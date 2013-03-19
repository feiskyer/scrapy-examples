from scrapy.selector import HtmlXPathSelector
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newsspider.items import NewsspiderItem
import time

class RedditSpider(CrawlSpider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['http://www.reddit.com/r/programming/','http://www.reddit.com/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # deal with next page
        nextlink = hxs.select('//p[@class="nextprev"]//a').select('@href').extract()[0]
        if len(nextlink)>0:
            yield self.make_requests_from_url(nextlink)

        links = hxs.select('//*[@id="siteTable"]//div//p[1]/a')
        for link in links:
            url = link.select('@href').extract()[0]
            title = link.select('text()').extract()[0]
            if len(url)>0 and len(title)>0:
                item = NewsspiderItem()
                item['title']=title 
                item['url']=url
                item['site']=RedditSpider.name
                yield item


