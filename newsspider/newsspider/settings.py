# Scrapy settings for newsspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Newsspider'
USER_AGENT = 'Newsspider+(+http://www.www.com/)'
# Baiduspider+(+http://www.baidu.com/search/spider.htm")
# Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
# Googlebot/2.1 (+http://www.googlebot.com/bot.html)
# Googlebot/2.1 (+http://www.google.com/bot.html)
# Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html")
# Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp")
# iaskspider/2.0(+http://iask.com/help/help_index.html")
# Mozilla/5.0 (compatible; iaskspider/1.0; MSIE 6.0)
# Sogou web spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07")
# Sogou Push Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07")
# Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/"; )
# msnbot/1.0 (+http://search.msn.com/msnbot.htm")

SPIDER_MODULES = ['newsspider.spiders']
NEWSPIDER_MODULE = 'newsspider.spiders'
COMMANDS_MODULE = 'newsspider.commands'
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
ITEM_PIPELINES = ['newsspider.pipelines.NewsspiderPipeline']
SCHEDULER = 'scrapy.core.scheduler.Scheduler'

DOWNLOADER_MIDDLEWARES = {   
        # 'newsspider.middlewares.ProxyMiddleware': 100, 
        'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110, 
        'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
        'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
        'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
        'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
        'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
        'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 800,
        'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
        'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
        'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
    }

CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN =8
# CONCURRENT_REQUESTS_PER_IP = 8
ROBOTSTXT_OBEY = False

DEPTH_LIMIT = 6
DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_TIMEOUT = 30
DNSCACHE_ENABLED = True


#LOG_FILE = ''
LOG_LEVEL = 'DEBUG'

PNG_PATH = '/var/scrapy'
DOWNLOAD_PREVIEW = False
