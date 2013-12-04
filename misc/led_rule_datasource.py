from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil

pvname = widget.getPropertyValue("pv_name")

if pvname != "": 
    
    widget.setPropertyValue("off_color", ColorFontUtil.GREEN)
    
    pv = widget.getPV()
    
    variance = PVUtil.getDouble(pv)
    
    if variance < 2 and variance > -2:
        
        widget.setPropertyValue("on_color", ColorFontUtil.GREEN)
        
    elif variance >= 2 and variance < 5:
        
        widget.setPropertyValue("on_color", ColorFontUtil.YELLOW)
    
    elif variance <= -2 and variance > -5:
        
        widget.setPropertyValue("on_color", ColorFontUtil.YELLOW)
        
    elif variance >= 5 and variance < 10:
        
        widget.setPropertyValue("on_color", ColorFontUtil.ORANGE)
        
    elif variance <= -5 and variance > -10:
        
        widget.setPropertyValue("on_color", ColorFontUtil.ORANGE)
        
    elif variance >= 10:
        
        widget.setPropertyValue("on_color", ColorFontUtil.RED)
        
    elif variance <= -10:
        
        widget.setPropertyValue("on_color", ColorFontUtil.RED)
        

    