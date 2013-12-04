from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

boxpv = display.getWidget("monitor_box_container").getPVByName("loc://monitor_box")
channelpv = widget.getPVByName("loc://monitor_channel(\"\")")

boxnumber = PVUtil.getLong(boxpv)
channel = PVUtil.getString(channelpv)

#macroInput.put("BOXNO", "%s" % boxnumber)
macroInput.put("BOX", "BOX:%s" % boxnumber)
macroInput.put("CHANNEL", "%s" % channel)
#macroInput.put("P", "CB:CB:HV")

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

