from org.csstudio.opibuilder.scriptUtil import PVUtil

display.getWidget("monitortabled00").setPropertyValue("pv_name", "CB:HV:BOX:18:0:0:read_volt.STAT")
display.getWidget("led18").setPropertyValue("border_style", 3)
display.getWidget("led19").setPropertyValue("border_style", 0)
test = display.getWidget("led18").getPropertyValue("border_style")
print test