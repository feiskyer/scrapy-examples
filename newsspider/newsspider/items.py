# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NewsspiderItem(Item):
    # define the fields for your item here like:
    title = Field()
    url = Field()
    site = Field()
    abstract = Field()
    created = Field()
