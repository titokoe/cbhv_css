from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

boxpv = widget.getPVByName("loc://map_box")
levelpv = widget.getPVByName("loc://map_level")
channelpv = widget.getPVByName("loc://map_channel")

boxvalue = PVUtil.getLong(boxpv)
levelvalue = PVUtil.getLong(levelpv)
channelvalue = PVUtil.getLong(channelpv)

macroInput.put("BOXNO", "%s" % boxvalue)
macroInput.put("LEVELNO", "%s" % levelvalue)
macroInput.put("CHANNELNO", "%s" % channelvalue)
macroInput.put("P", "CB:CB:HV")

print boxvalue

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

