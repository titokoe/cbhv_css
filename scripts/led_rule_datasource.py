from org.csstudio.opibuilder.scriptUtil import PVUtil

variance = widget.getPV().getValue()

#led_name = widget.getPropertyValue("name")

#widget.getPVByName("loc://%s" % led_name).setValue(variance)

if(variance >= 2 and pv0 < 5):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(255,255,0))
    
elif(variance <= -2 and pv0 > -5):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(255,255,0))
    
elif(variance >= 5 and pv0 < 10):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(255,0,0))
    
elif(variance <=  -5 and pv0 > -10):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(255,0,0))
    
elif(variance >= 10):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(0,0,0))
    
elif(variance <= -10):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(0,0,0))
    
elif(variance < 2 and pv0 > -2):
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(0,255,0))
    
else:
    
    widget.setPropertyValue("on_color",ColorFontUtil.getColorFromRGB(0,255,0));
