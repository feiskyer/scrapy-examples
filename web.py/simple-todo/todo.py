import web
import model

urls=(
        '/', 'Index',
        '/del/(\d+)', 'Delete'
        )

render = web.template.render('templates', base='base')

class Index:
    form=web.form.Form(
            web.form.Textbox('title', web.form.notnull,
                description='I need to:'),
            web.form.Button('Add todo'),
    )

    def GET(self):
        todos=model.get_todos()
        form=self.form()
        return render.index(todos, form)

    def POST(self):
        form=self.form()
        if not form.validates():
            todos=model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')

class Delete:
    def POST(self, id):
        id=int(id)
        model.del_todo(id)
        raise web.seeother('/')

if __name__=='__main__':
    app=web.application(urls, globals())
    app.run()
