from org.csstudio.opibuilder.scriptUtil import PVUtil

value = widget.getPropertyValue("pv_value")

if value == 1:
    
    widget.setPropertyValue("text", "setting channels")
    
else:
    
    widget.setPropertyValue("text", "")
