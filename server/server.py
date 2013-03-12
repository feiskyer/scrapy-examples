#!/usr/bin/env python
import web

class hello:
    def __init__(self):
        self.offset=0
        self.limit=1000
        self.db = web.database(dbn='mysql', user='root', 
                    pw='feisky', db='news')

    def GET(self):
        news=self.db.select('news', order="created DESC", offset=self.offset,
                limit=self.limit)
        if len(news)>0:
            self.offset=self.offset+len(news)
            render = web.template.render('templates/')
            return render.index(news)
        else:
            return 'Hello, world!'

if __name__ == "__main__":
    urls = ("/.*", "hello")
    app = web.application(urls, globals())
    app.run()
