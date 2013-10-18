import requests

from settings import servers


master = servers['master']
master_login = master['login']


'''
Takes nothing, returns a bound requests session object
'''
def log_in():
    login_url = master['url'] + master['login']['uri']
    data = {
        master_login['username_form_key']: master_login['username'],
        master_login['password_form_key']: master_login['password'],
        'form_id': master_login['login_form_id'],
    }
    s = requests.session()
    r = s.post(login_url, data=data)
    return s


