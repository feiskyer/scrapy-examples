from scrapy.contrib.spiders import XMLFeedSpider
from newsspider.items import NewsspiderItem
from scrapy import log

class FeedSpider(XMLFeedSpider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/feed/']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly
    namespaces = [ ('content', 'http://purl.org/rss/1.0/modules/content'),
            ('dc', 'http://purl.org/dc/elements/1.1/') ]

    def parse_node(self, response, selector):
        #for prefix, uri in self.namespaces:
        #    selector.register_namespace (prefix, uri)
        selector.remove_namespaces()
        item = NewsspiderItem()
        item['url'] = selector.select('link/text()').extract()[0]
        item['title'] = selector.select('title/text()').extract()[0]
        item['created'] = selector.select('pubDate/text()').extract()[0]
        item['abstract'] = selector.select('description/text()').extract()[0]
        item['site']= FeedSpider.name
        return item
