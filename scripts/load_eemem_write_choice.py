from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil


macroInput = DataUtil.createMacrosInput(True)

pvname = widget.getPVByName("loc://SetEemem")
pvvalue = PVUtil.getString(pvname)

if pvvalue == "IP":
    
    pvvalue = "Ip"
    
elif pvvalue == "MAC":
    
    pvvalue = "Mac"    

macroInput.put("EEMEM_VALUE", "%s" % pvvalue)

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)