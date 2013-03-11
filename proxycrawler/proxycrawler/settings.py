# Scrapy settings for proxycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'proxycrawler'

SPIDER_MODULES = ['proxycrawler.spiders']
NEWSPIDER_MODULE = 'proxycrawler.spiders'
ITEM_PIPELINES = ['proxycrawler.pipelines.ProxycrawlerPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'proxycrawler (+http://www.yourdomain.com)'
