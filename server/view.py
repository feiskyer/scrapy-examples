#coding=utf8
import web
import db
import config
import datetime

def datestr(x):
    """
    Can't seem to set mysql creation ddl to UTC, so we'll have to adjust the datestr
    function to localtime which we will assume is the same as your database server.
    """
    return web.datestr(x, datetime.datetime.now())

t_globals = dict(
  datestr=datestr,
)
render = web.template.render('templates/', cache=config.cache, 
    globals=t_globals)
render._keywords['globals']['render'] = render

def listing(**k):
    l = db.listing(**k)
    return render.listing(l)
