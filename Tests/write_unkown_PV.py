from org.csstudio.opibuilder.scriptUtil import PVUtil

level = 0

while level < 1:
    
    channel = 0
    
    while channel < 1:
    
        display.getWidget("rect").setPropertyValue("pv_name", "CB:HV:BOX:19:%s:%s:set_volt" % (level, channel))
        display.getWidget("rect1").getPVByName("loc://forward").setValue("1550")
        channel = channel + 1
        
    level = level + 1
