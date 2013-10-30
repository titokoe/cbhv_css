from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil

input = DataUtil.createMacrosInput(True)

input.put("pvinput", PVUtil.getString(pvArray[0]))

print input

display.getWidget("tabbed_container").setPropertyValue("macros", input)

display.getWidget("linking_container").setPropertyValue("opi_file", 
    display.getWidget("linking_container").getPropertyValue("opi_file"), True)