#!/usr/bin/env python
#coding=utf8
import os, sys
import web
import view
import config
import db
from view import render

urls = (
    '/', 'index',
    '/page/(\d+)','index'
)

class index:
    def GET(self,page=1):
        page = int(page)
        limit=config.perpage
        offset = (page -1)*limit
        counting = db.counting()
        pages = counting / limit
        if counting % limit > 0:
            pages += 1
        if page > pages:
            raise web.seeother('/')
        else:
            return render.base(view.listing(offset=offset,limit=limit), 
                    pages=pages, curpage=page)

if __name__ == "__main__":
    if len(sys.argv)==1:
        port = os.environ.get("PORT", "8081")
        sys.argv.append(port)
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
