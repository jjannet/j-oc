from enums.colors import bcolors
from models.commandHelper import CommandHelper
from tabulate import tabulate
from enums.conf import Config


def getCommands():
    commands: list[CommandHelper] = []

    commands.append(CommandHelper(
        Config.appName + " user", "view user conofig"))
    commands.append(CommandHelper(
        Config.appName + " user config", "config user"))
    commands.append(CommandHelper(
        Config.appName + " login", "login openshift"))
    commands.append(CommandHelper(
        Config.appName + " project", "view all projects in openshift"))
    commands.append(CommandHelper(
        Config.appName + " project <project name>", "select project"))
    commands.append(CommandHelper(Config.appName +
                    " pod", "list all pod in openshift"))
    commands.append(CommandHelper(
        Config.appName + " pod config", "config pod"))
    commands.append(CommandHelper(Config.appName +
                    " pod read", "view all config pods"))
    commands.append(CommandHelper(Config.appName +
                    " pod remove", "remove pod config"))
    commands.append(CommandHelper(
        Config.appName + " start <pod id>", "start pod port forwarding"))

    return commands


def printHelp():
    commands = getCommands()
    datas = []

    for cmd in commands:
        datas.append([cmd.command, cmd.detail])

    print("Command helper")

    print(tabulate(datas,
          headers=['Command', 'Description'], tablefmt='orgtbl'))
