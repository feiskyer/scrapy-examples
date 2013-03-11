# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
import time
import os
import uuid

class NewsspiderPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', 
                passwd='feisky', db='news', host='localhost', 
                charset="utf8", 
                use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        url = item.get('url', '')
        if len(url)==0:
            return item

        try:
            curdir = os.getcwdu()
            filename = "%s/pngs/%s.png" % (curdir, str(uuid.uuid1()))

            cmd = os.popen(u'''%s/webkit2png -x 1366 768 -F javascript "%s" -o "%s"''' % 
                        (curdir, url, filename))
            result = cmd.read()
            if 'Failed' in result:
                os.unlink(filename)
            cmd.close()

            if self.cursor.execute('''select * from news where url='%s' ''' % 
                    item.get('url', '')) == 0:
                self.cursor.execute(
                    """INSERT INTO news(title,url,site,abstract, created, file)  
                    VALUES (%s, %s, %s, %s, %s, %s)""", 
                    (   item.get('title','').encode('utf-8'), 
                        url,
                        item.get('site', ''),
                        item.get('abstract', '').encode('utf-8'),
                        item.get('created', time.strftime('%Y-%m-%d %H:%M:%S'),
                        filename)))
                self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item
    
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None

