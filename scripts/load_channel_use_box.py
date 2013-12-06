from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

pvvalue = widget.getPVByName("loc://channel_in_use")


boxnumber = PVUtil.getLong(pvvalue)

macroInput.put("BOXNO", "%s" % boxnumber)
macroInput.put("BOX", "BOX:%s" % boxnumber)
macroInput.put("P", "CB:CB:HV")

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

