import sys

import settings
import auth
import actions

from colorama import init

init()

from colorama import Fore, Style


failed = []
passed = []

# Colorized output plus counters
def p_ok(text):
    passed.append(text)
    print(Fore.GREEN + text + Style.RESET_ALL)

def p_fail(text):
    failed.append(text)
    print(Fore.RED + text + Style.RESET_ALL)

def wwn(text):
    sys.stdout.write(text)
    sys.stdout.flush()



def login():
    wwn('Testing login.. ')
    try:
        r = auth.log_in(settings.servers['master'])
        if not r.verify:
            p_fail('Login test failed!')
        else:
            p_ok('Login succeeded')
    except:
        p_fail('Login test failed!')

def get_users():
    wwn('Testing GET users list.. ')
    try:
        r = actions.get_users(settings.servers['master'])
        if not r.ok:
            p_fail('GET users failed!')
        else:
            p_ok('GET users list succeeded')
    except:
        p_fail('GET users failed!')


# Run all tests
def run_tests():
    login()
    get_users()

    print(Fore.GREEN + "Passed: " + str(len(passed)) + Style.RESET_ALL )
    print(Fore.RED + "Failed: " + str(len(failed)) + Style.RESET_ALL )

if __name__ == "__main__":
    run_tests()

