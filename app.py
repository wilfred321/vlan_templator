from vlan_tmpl import create_app
app = create_app()
app.config['TEMPLATES_AUTO_RELOAD'] = True 
app.config['SECRET_KEY'] = 'Thisisaverysecretkey'

app.config['ALLOWED_EXTENSIONS'] = {'txt'}


