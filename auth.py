import requests


'''

Takes a dict that describes a server, returns a bound 'requests'
session object. See local_settings-template.py for example server configs.

'''
def log_in(server):
    login_url = server['url'] + server['login']['uri']
    data = {
        server['login']['username_form_key']: server['login']['username'],
        server['login']['password_form_key']: server['login']['password'],
        'form_id': server['login']['login_form_id'],
    }
    s = requests.session()
    r = s.post(login_url, data=data)
    return s


