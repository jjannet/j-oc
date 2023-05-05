from process.login import loginApp
from process.configUser import userApp
from process.project import projectApp
from process.pod import podApp
from process.forwardPort import forwardPortApp


def startProcess(command, args):
    if command == "user":
        userApp(args)
    if command == "login":
        loginApp()
    if command == "project":
        projectApp(args)
    if command == "pod":
        podApp(args)
    if command == "start":
        forwardPortApp(args)
