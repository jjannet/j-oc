import json
import os
from models.user import User
from enums.colors import bcolors
from enums.paths import paths


def initUserFileConfig():
    
    isExisting = os.path.exists(paths.user)

    if isExisting == False:
        user = User("", "", "")
        userJson = json.dumps(user.__dict__)

        os.makedirs(os.path.dirname(paths.user), exist_ok=True)

        with open(paths.user, "w") as f:
            f.write(userJson)


def readUserConfig():
    user = User("", "", "")
    isExisting = os.path.exists(paths.user)

    if isExisting == True:
        f = open(paths.user, "r")
        uerJson = f.read()
        userDict = json.loads(uerJson)

        user.username = userDict["username"]
        user.password = userDict["password"]
        user.url = userDict["url"]

        return user
    else:
        print('file not found')
        return None


def writeUserConfig(user):
    userJson = json.dumps(user.__dict__)

    f = open(paths.user, "w")
    f.write(userJson)
    f.close()

    print("save user config !")


def readUserConfigFromConsole():
    user = User("", "", "")

    print(bcolors.WARNING + "User configuration ---------------" + bcolors.ENDC)
    print()
    user.username = input("Username: " + bcolors.OKCYAN)
    user.password = input(bcolors.ENDC + "Password: " + bcolors.OKCYAN)
    user.url = input(bcolors.ENDC + "oc url: " + bcolors.OKCYAN)
    print(bcolors.ENDC)

    return user


def readUserData():
    user = readUserConfig()

    print(bcolors.WARNING + "User data ---------------" + bcolors.ENDC)
    print("username: " + bcolors.OKCYAN + user.username + bcolors.ENDC)
    print("password: " + bcolors.OKCYAN + user.password + bcolors.ENDC)
    print("oc url: " + bcolors.OKCYAN + user.url + bcolors.ENDC)
    print()


def configUserData():
    readUserData()

    user = readUserConfigFromConsole()
    writeUserConfig(user)


def userApp(args):

    if len(args) > 2:
        command = args[2]

        if command == "config":
            configUserData()
    else:
        readUserData()
