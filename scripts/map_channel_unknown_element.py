from org.csstudio.opibuilder.scriptUtil import PVUtil

pv = widget.getPV().getValue()

print pv

if pv == None:
    
    display.getWidget("map_channel").setPropertyValue("visible", False)
    display.getWidget("map_channel_info").setPropertyValue("visible", True)
    
else:
    
    display.getWidget("map_channel").setPropertyValue("visible", True)
    display.getWidget("map_channel_info").setPropertyValue("visible", False)