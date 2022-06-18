from threadsnake.core import *

@(export(__name__)).get('//mono')
def test(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Done!')