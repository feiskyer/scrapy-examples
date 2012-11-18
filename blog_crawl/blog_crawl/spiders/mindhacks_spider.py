from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from blog_crawl.items import BlogCrawlItem
 
class MindhacksSpider(BaseSpider):
    name = "mindhacks.cn"
    allowed_domains = [ "mindhacks.cn"]
    start_urls = ["http://mindhacks.cn/"]
 
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//h3/a/@href')
        items = []
        # save all urls
        #for site in sites:
        #    item = BlogCrawlItem()
        #    item['url'] = site.extract()
        #    items.append(item)

        # process each post
        items.extend([self.make_requests_from_url(url.extract()).replace(callback=self.parse_post)
                  for url in sites])

        # process next page
        page_links=hxs.select('//div[@class="wp-pagenavi"]/a[not(@title)]')
        for link in page_links:
            if link.select('text()').extract()[0] == u'\xbb':
                url = link.select('@href').extract()[0]
                items.append(self.make_requests_from_url(url))
        return items

    def parse_post(self, response):
        item = BlogCrawlItem()
        item['url'] = unicode(response.url)
        item['raw'] = response.body_as_unicode()
        return [item]
