#from scrapy.selector import HtmlXPathSelector
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newsspider.items import NewsspiderItem
from BeautifulSoup import BeautifulSoup
import time

class HackernewsSpider(CrawlSpider):
    name = 'hackernews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    #rules = (
    #    Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #)

    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        #i = NewsspiderItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        soup=BeautifulSoup(response.body)
        links=soup.findAll('td', {'class':'title'})
        for link in links:
            linkinfo = link.findChild()
            if not linkinfo: continue
            title = linkinfo.text
            url = linkinfo.get('href', '')
            if not url.startswith('http'):
                if url.startswith('/'):
                    url = 'http://news.ycombinator.com' + url
                else:
                    url = 'http://news.ycombinator.com/' + url

            # deal with next page
            if title == 'More' or title == 'next': # next page
                yield self.make_requests_from_url(url).replace(callback=self.parse)
            # get a new news item
            elif len(title)>0 and len(url)>0:
                item = NewsspiderItem()
                item['title']=title
                item['url']=url
                item['site']='hackernews'
                yield item

