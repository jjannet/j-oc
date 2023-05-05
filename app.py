import sys
from start import startProcess
from enums.colors import bcolors
from process.configUser import initUserFileConfig
from process.pod import initPodConfig
from process.help import printHelp

initUserFileConfig()
initPodConfig()

if len(sys.argv) > 1:
    command = sys.argv[1]
    startProcess(command, sys.argv)
else:
    printHelp()