from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil


name_string = widget.getPropertyValue("name")
name_array = name_string.split("_")
numberofboxes = 20
box = name_array[2]
display.getWidget("text_box").getPV().setValue(box)
display.getWidget("tabbed_container").setActiveTabIndex(0)
display.getWidget("led_set_active").setPropertyValue("pv_name", "CB:HV:BOX:%s:is_active" % box)

count = 1

while count <= numberofboxes:

    display.getWidget("box_led_%d" % count).setPropertyValue("border_width", "0")
    count = count + 1

widget.setPropertyValue("border_width", "4")

level = 0

while level < 5:
    
    channel = 0
    
    while channel < 8:
        
        print channel
        
        pvname = "CB:HV:BOX:%s:%s:%s:volt_variance" % (box, level, channel)
        widgetname = "mon_led_%s_%s" % (level, channel)
        print display.getWidget("engage").getPVByName(pvname)
        
        if display.getWidget("engage").getPVByName(pvname) == None:
            
            display.getWidget(widgetname).setPropertyValue("enabled", False)
            display.getWidget(widgetname).setPropertyValue("pv_name", "")
            display.getWidget(widgetname).setPropertyValue("off_color", ColorFontUtil.PURPLE)
            
        else:
            
            display.getWidget(widgetname).setPropertyValue("enabled", True)
            display.getWidget(widgetname).setPropertyValue("pv_name", pvname)
            
        channel = channel + 1
        
    level = level + 1
    