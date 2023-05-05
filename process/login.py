import subprocess
import json
import os
from process.configUser import readUserConfig


def login():
    print('startLogin')
    user = readUserConfig()

    if user != None:

        command = "oc login " + user.url + " -u " + \
            user.username + " -p " + user.password

        result = os.system(command)
        print(result)


def loginApp():
    login()
