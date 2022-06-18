from threadsnake.core import *

app = Application(get_port(8088))

app.use_router(routes_to('router'), '/router/')
app.wait_exit()