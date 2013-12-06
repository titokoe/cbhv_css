from org.csstudio.opibuilder.scriptUtil import PVUtil

value = widget.getValue()

#if value == "Box":
    
#    display.getWidget("group_box").setPropertyValue("enabled", True)
#    display.getWidget("group_channel").setPropertyValue("enabled", False)
#    display.getWidget("group_element").setPropertyValue("enabled", False)
    
#elif value == "Channel":
    
#    display.getWidget("group_box").setPropertyValue("enabled", False)
#    display.getWidget("group_channel").setPropertyValue("enabled", True)
#    display.getWidget("group_element").setPropertyValue("enabled", False)
    
#elif value == "Element":
    
#    display.getWidget("group_box").setPropertyValue("enabled", False)
#    display.getWidget("group_channel").setPropertyValue("enabled", False)
#    display.getWidget("group_element").setPropertyValue("enabled", True)
    
if value == "From file":
    
#    display.getWidget("group_box").setPropertyValue("enabled", False)
#    display.getWidget("group_channel").setPropertyValue("enabled", False)
#    display.getWidget("group_element").setPropertyValue("enabled", False)
    display.getWidget("radio_source").getPV().setValue("File")