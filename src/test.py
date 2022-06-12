from threadsnake.core import *

app = build_application(8080, [], {})


@app.get('/{id:int}')
def test(app:Application, req:HttpRequest, res:HttpResponse):
    res.end(req.params['id'])

@app.get('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Done!')


app.wait_exit('')