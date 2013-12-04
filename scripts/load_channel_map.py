from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

elementpv = widget.getPVByName("loc://map_element")

elementvalue = PVUtil.getLong(elementpv)

macroInput.put("ELEMENTNO", "%s" % elementvalue)
macroInput.put("P", "CB:CB:HV")

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

