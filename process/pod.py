import subprocess
import os
import json
from enums.paths import paths
from models.pod import PodConfig
from enums.colors import bcolors
from tabulate import tabulate


def initPodConfig():
    isExisting = os.path.exists(paths.pod)
    if isExisting == False:
        podJson = "[]"
        os.makedirs(os.path.dirname(paths.pod), exist_ok=True)
        with open(paths.pod, "w") as f:
            f.write(podJson)


def getAllPods():
    pods = []
    pds = subprocess.run(
        ['oc', 'get', 'pods'], capture_output=True).stdout.splitlines()

    pds = pds[1:]

    for p in pds:
        pName = p.decode("utf-8").split(" ")[0]
        pods.append(pName)

    return pods


def listAllPods():
    pods = getAllPods()

    for pod in pods:
        print("- " + pod)


def getPodConfigs():
    pods: list[PodConfig] = []

    f = open(paths.pod, "r")
    podsJson = f.read()
    podsDict = json.loads(podsJson)

    for p in podsDict:
        pod = PodConfig(p["id"], p["projectName"], p["serviceName"], p["port"])
        pods.append(pod)

    return pods


def reGenId(pods: list[PodConfig]):
    pods = sorted(pods, key=lambda x: x.serviceName, reverse=False)

    id = 1

    for p in pods:
        p.id = id
        id += 1

    return pods


def writePodConfig(pod: PodConfig):
    pods = getPodConfigs()
    pods.append(pod)

    writeAllPodsConfig(pods)


def writeAllPodsConfig(pods: list[PodConfig]):
    pods = reGenId(pods)
    podJson = json.dumps([obj.__dict__ for obj in pods])

    f = open(paths.pod, "w")
    f.write(podJson)
    f.close()

    print(bcolors.OKGREEN + "save pod config !" + bcolors.ENDC)


def viewPodConfig():
    pods = getPodConfigs()
    pods = sorted(pods, key=lambda x: x.serviceName, reverse=False)

    datas = []

    for p in pods:
        datas.append([p.id, p.projectName, p.serviceName, p.port])

    print(tabulate(datas,
          headers=['Id', 'Project name', 'Service name', 'Port'], tablefmt='orgtbl'))

    print()


def inputPodConfig():
    pod = PodConfig(-1, "", "", "")

    print(bcolors.WARNING + "Pod configuration ---------------" + bcolors.ENDC)
    print()
    pod.projectName = input("Project name: " + bcolors.OKCYAN)
    pod.serviceName = input("Service name: " + bcolors.OKCYAN)
    pod.port = input("Port: " + bcolors.OKCYAN)
    print(bcolors.ENDC)

    return pod


def configPod():
    viewPodConfig()
    print()

    pod = inputPodConfig()

    writePodConfig(pod)


def removePodConfig():
    viewPodConfig()
    pods = getPodConfigs()

    id = input("Remove pod id: " + bcolors.OKCYAN)
    print(bcolors.ENDC)

    pods = list(filter(lambda x: x.id != int(id), pods))

    for p in pods:
        print(p.serviceName)


    writeAllPodsConfig(pods)


def podApp(args):
    if len(args) > 2:
        command = args[2]
        if command == "config":
            configPod()
        if command == "read":
            viewPodConfig()
        if command == "remove":
            removePodConfig()
    else:
        listAllPods()
