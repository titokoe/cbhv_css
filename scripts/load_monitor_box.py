from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

boxpv = widget.getPVByName("loc://monitor_box")

boxnumber = PVUtil.getLong(boxpv)

macroInput.put("BOXNO", "%s" % boxnumber)
macroInput.put("BOX", "BOX:%s" % boxnumber)
macroInput.put("P", "CB:CB:HV")

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

