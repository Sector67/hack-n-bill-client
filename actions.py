import requests

import auth
import settings


def get_users(server):
    s = auth.log_in(server)
    r = s.get(server['url'] + '/services/users/user')
    return r



