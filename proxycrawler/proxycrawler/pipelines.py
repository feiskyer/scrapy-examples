# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
#
# Reference: http://www.cnblogs.com/igloo1986/archive/2012/08/25/2655597.html

import urllib
from scrapy.exceptions import DropItem
import socket

class ProxycrawlerPipeline(object):
    def process_item(self, item, spider):
        protocol = item['protocol']
        address = item['address']
        port = item['port']
        proxies = {protocol:'%s:%s'% (address, port)}

        #check if proxy can be connected
        try:
            socket.setdefaulttimeout(3)
            data  = urllib.urlopen('http://ifconfig.me/ip', proxies=proxies).read()
        except:
            raise DropItem("curl download the proxy %s:%s is bad" % (address, port))

        if data:
            line = '%s\t%s\t%s\n' % (address, port, protocol)
            file('proxies.txt', 'a+').write(line)
            return item
        else:
            raise DropItem("Not valid proxy %s:%s" %(address, port))
