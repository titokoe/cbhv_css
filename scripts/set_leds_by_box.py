from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil


name_string = widget.getPropertyValue("name")
name_array = name_string.split("_")
numberofboxes = 20
box = name_array[2]
box = int(box)
display.getWidget("text_box").getPV().setValue(box)
display.getWidget("tabbed_container").setActiveTabIndex(0)
display.getWidget("led_set_active").setPropertyValue("pv_name", "CB:CB:HV:BOX:%s:IsActive" % box)

count = 1

while count <= numberofboxes:

    display.getWidget("box_led_%d" % count).setPropertyValue("border_width", "0")
    count = count + 1

widget.setPropertyValue("border_width", "4")

check_box = display.getWidget("engage").getPVByName("CB:CB:HV:BOX:%s:Status" % box)

print check_box

if check_box != None:

    level = 0
    
    while level < 5:
        
        channel = 0
        
        while channel < 8:
            
            check_channel = display.getWidget("engage").getPVByName("CB:CB:HV:BOX:%s:%s:%s:VoltVariance" % (box, level, channel))
            
            if check_channel != None:
            
                widgetname = "mon_led_%s_%s" % (level, channel)
                pvname = "CB:CB:HV:BOX:%s:%s:%s:VoltVariance" % (box, level, channel)
                
                display.getWidget(widgetname).setPropertyValue("enabled", True)
                display.getWidget(widgetname).setPropertyValue("pv_name", pvname)
                display.getWidget(widgetname).setPropertyValue("off_color", ColorFontUtil.GREEN)
                
            else:
                
                widgetname = "mon_led_%s_%s" % (level, channel)
                display.getWidget(widgetname).setPropertyValue("enabled", False)
                display.getWidget(widgetname).setPropertyValue("pv_name", "")
                display.getWidget(widgetname).setPropertyValue("pv_value", "0")
                display.getWidget(widgetname).setPropertyValue("off_color", ColorFontUtil.BLACK)
                
            channel = channel + 1
            
        level = level + 1
        
else:
    
    level = 0
    
    while level < 5:
        
        channel = 0
        
        while channel < 8:
            
            widgetname = "mon_led_%s_%s" % (level, channel)
            display.getWidget(widgetname).setPropertyValue("enabled", False)
            display.getWidget(widgetname).setPropertyValue("pv_name", "")
            display.getWidget(widgetname).setPropertyValue("pv_value", "0")
            display.getWidget(widgetname).setPropertyValue("off_color", ColorFontUtil.PURPLE)
            
            channel = channel + 1
            
        level = level + 1