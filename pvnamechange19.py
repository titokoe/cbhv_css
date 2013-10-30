from org.csstudio.opibuilder.scriptUtil import PVUtil

display.getWidget("monitortabled00").setPropertyValue("pv_name", "CB:HV:BOX:19:0:0:read_volt.STAT")
display.getWidget("led19").setPropertyValue("border_style", 3)
display.getWidget("led18").setPropertyValue("border_style", 0)

