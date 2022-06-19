from threadsnake.core import *

set_log_config(LogLevel.ALL)
badge_async('threadsnake 0.0.15', title='version')

app = Application(get_port(8088))

#Configuring top level middlewares
app.configure(static_files('static'))
app.configure(session(Session('threadsnake-session-id')))
app.configure(authorization)
app.configure(body_parser)
app.configure(multipart_form_data_parser('temp', 60))
app.configure(json_body_parser)
app.configure(cors)
app.configure(build_default_headers({"purpose":"test"}))
app.configure(identify_client)
app.configure(header_inspector("content-type", lambda a: print(a)))
app.configure(time_measure)
app.configure(uses_php('php'))
app.configure(serve_static_markdown('markdown'))

#Configuring routers
app.use_router(routes_to('router'), '/router/')

app.wait_exit()