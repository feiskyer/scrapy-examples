from scrapy.contrib.spiders import XMLFeedSpider
from newsspider.items import NewsspiderItem
from scrapy import log

class FeedSpider(XMLFeedSpider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://feed.cnblogs.com/blog/u/53116/rss']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly
    #namespaces = [ ('content', 'http://purl.org/rss/1.0/modules/content'),
    #        ('dc', 'http://purl.org/dc/elements/1.1/') ]

    def parse_node(self, response, selector):
        #for prefix, uri in self.namespaces:
        #    selector.register_namespace (prefix, uri)

        item = NewsspiderItem()
        item['url'] = selector.select('id/text()').extract()[0]
        item['title'] = selector.select('title/text()').extract()[0]
        item['created'] = selector.select('published/text()').extract()[0]
        item['abstract'] = selector.select('summary/text()').extract()[0]
        item['site']= FeedSpider.name
        return item
