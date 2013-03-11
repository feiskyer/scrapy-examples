# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ProxycrawlerItem(Item):
     address   = Field()
     port      = Field()
     protocol  = Field()
     location  = Field()
 
     type      = Field() # 0: anonymity #1 nonanonymity
     delay     = Field() # in second
     timestamp = Field()
