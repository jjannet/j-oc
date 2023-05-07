import subprocess
import json
import os
from process.configUser import readUserConfig
from enums.colors import bcolors


def login():
    user = readUserConfig()

    if user.username and user.password and user.url:

        command = "oc login " + user.url + " -u " + \
            user.username + " -p " + user.password + " --insecure-skip-tls-verify=true"

        result = os.system(command)
        print(result)
    else:
        print(bcolors.FAIL + "No config user." + bcolors.ENDC)


def loginApp():
    login()
