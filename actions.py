import requests

import auth
import settings


def get_users():
    s = auth.log_in()
    r = s.get(settings.servers['master']['url'] + '/services/users/user')
    return r.text

print get_users

