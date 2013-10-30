from org.csstudio.opibuilder.scriptUtil import PVUtil

value = display.getWidget("radio_source").getValue()

if value == "selected Value":
    
    display.getWidget("group_selected_voltage").setPropertyValue("enabled", True)
    display.getWidget("group_filepath").setPropertyValue("enabled", False)
    
else:
    
    display.getWidget("group_selected_voltage").setPropertyValue("enabled", False)
    display.getWidget("group_filepath").setPropertyValue("enabled", True)