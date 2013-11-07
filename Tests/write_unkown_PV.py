from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import FileUtil
import os

opifilepath = display.getModel().getOpiFilePath().toString()

workspacepath = FileUtil.workspacePathToSysPath("/")

path = workspacepath + opifilepath

path = path[::-1]

pathsplit = path.split("/",1)

folder = pathsplit[1]

configfilepath = folder[::-1]

configfile = configfilepath + "/cbhv_config.txt"

test = os.path.isfile(configfile)

print test