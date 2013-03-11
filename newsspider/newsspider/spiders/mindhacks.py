from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from newsspider.items import NewsspiderItem

class MindhacksSpider(CrawlSpider):
    name = 'mindhacks'
    allowed_domains = ['mindhacks.cn']
    start_urls = ['http://www.mindhacks.cn/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//h3/a/@href')

        for url in sites:
            yield self.make_requests_from_url(url.extract()).replace(callback=self.parse_post)

        # process next page
        page_links=hxs.select('//div[@class="wp-pagenavi"]/a[not(@title)]')
        for link in page_links:
            if link.select('text()').extract()[0] == u'\xbb':
                url = link.select('@href').extract()[0]
                yield self.make_requests_from_url(url)

    def parse_post(self, response):
        hxs = HtmlXPathSelector(response)
        title = hxs.select('//h1/a/text()').extract()[0]
        url = hxs.select('//h1/a/@href').extract()[0]
        created = hxs.select('//*[@class="published"]/@title').extract()[0]

        if len(title) >0 and len(url) > 0:
            item = NewsspiderItem()
            item['url'] = url
            item['title'] = title
            item['created'] = created
            item['site']= MindhacksSpider.name
            yield item
