import os
import subprocess

from process.pod import getPodConfigs
from process.pod import getAllPods
from models.pod import PodConfig
from process.project import selectProject
from process.login import login


def runForwarding(podConf: PodConfig):
    selectProject(podConf.projectName)
    allPods = getAllPods()

    filters = list(filter(lambda k: podConf.serviceName in k, allPods))

    if len(filters) > 0:
        serviceName = filters[0]
        process = subprocess.Popen(
            ['oc', 'port-forward', serviceName, podConf.port])
        process.wait()
    else:
        print("Not found service name: " + podConf.serviceName)

def start(podId: int):
    pods = getPodConfigs()

    runPods = list(
        filter(lambda x: x.id == podId, pods))

    if len(runPods) > 0:
        pod = runPods[0]
        runForwarding(pod)
    else:
        print("not found pod id -> " + str(podId))


def forwardPortApp(args):
    if len(args) > 2:
        podId = args[2]
        start(int(podId))
    else:
        print("not select start pod id")
