from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil

display.getWidget("group_filepath").setPropertyValue("enabled", False)
display.getWidget("filepath").setPropertyValue("background_color", ColorFontUtil.GRAY)
display.getWidget("group_selected_voltage").setPropertyValue("enabled", False)
display.getWidget("group_channel").setPropertyValue("enabled", False)
display.getWidget("group_element").setPropertyValue("enabled", False)    
display.getWidget("group_box").setPropertyValue("enabled", False)
