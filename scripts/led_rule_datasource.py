from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil

active = widget.getPropertyValue("enabled")

led_name = widget.getPropertyValue("name")

if active == True:
    
    variance = widget.getPV().getValue()

    widget.getPVByName("loc://%s" % led_name).setValue(variance)
    
else:
    
    widget.getPVByName("loc://%s" % led_name).setValue(0)