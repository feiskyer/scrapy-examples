#coding=utf8
import web
DB = web.database(dbn='mysql', db='news', user='root', pw='feisky')
cache = False
perpage = 25
