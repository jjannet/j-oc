
import os
import subprocess

from enums.colors import bcolors


def getProjectList():
    projects = []
    progs = subprocess.run(
        ['oc', 'get', 'project'], capture_output=True).stdout.splitlines()

    progs = progs[1:]

    for p in progs:
        pName = p.decode("utf-8").split(" ")[0]
        projects.append(pName)

    return projects


def viewAllProject():
    projects = getProjectList()

    for p in projects:
        print("- " + p)


def selectProject(search):
    print('select proj -> ' + search)
    projects = getProjectList()

    filters = list(filter(lambda k: search in k, projects))

    if len(filters) > 0:
        projectName = filters[0]

        result = subprocess.run(
            ['oc', 'project', projectName], capture_output=True)

        if result.returncode == 0:
            print(bcolors.OKGREEN + "Now use project: " +
                  projectName + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Error with result: " +
                  result.stdout + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Not found project of " + search + bcolors.ENDC)
        print()


def projectApp(args):
    if len(args) > 2:
        project = args[2]
        selectProject(project)
    else:
        viewAllProject()
