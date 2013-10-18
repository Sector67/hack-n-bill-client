from colorama import init

init()

from colorama import Fore, Style

import settings
import auth
import actions


def p_ok(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def p_fail(text):
    print(Fore.RED + text + Style.RESET_ALL)


def login():
    p_ok('Testing login')
    try:
        print auth.log_in(settings.servers['master'])
    except:
        p_fail('Login test failed!')

def get_users():
    p_ok('Testing GET users list')
    try:
        r = actions.get_users(settings.servers['master'])
        if not r.ok:
            p_fail('GET users failed!')
    except:
        p_fail('GET users failed!')

def run_tests():
    login()
    get_users()

if __name__ == "__main__":
    run_tests()

