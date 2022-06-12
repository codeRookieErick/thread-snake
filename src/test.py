from threadsnake.core import *

app = build_application(8080, [], {})
@app.get('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Done!')
    
try:
    app.start()
    input('makemake')
except:
    print('something happened')
finally:
    app.stop()