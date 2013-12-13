from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

pvvalue = display.getWidget("eemem_read_box_combo").getValue()

pvname = int(pvvalue)

print pvname

macroInput.put("BOXNO", "%s" % pvname)

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

