import requests

import auth
import settings


def get_users(server):
    s = auth.log_in(server)
    r = s.get(server['url'] + '/temp_service.php?action=users_for_machine&machine_id=1')
    #r = s.get(server['url'] + '/services/users/user')
    return r



