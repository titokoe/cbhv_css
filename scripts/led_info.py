from org.csstudio.opibuilder.scriptUtil import PVUtil

display.getWidget("graph_current_channel").clearGraph()

name = widget.getPropertyValue("pv_name")


array = name.split(":")
box = array[4]
level = array[5]
channel = array[6]

display.getWidget("label_selected_channel").setPropertyValue("text", "CB:CB:HV:BOX:%s:%s:%s" % (box, level, channel))
display.getWidget("current_voltage").setPropertyValue("pv_name", "CB:CB:HV:BOX:%s:%s:%s:ReadVolt" % (box, level, channel))
display.getWidget("current_variance").setPropertyValue("pv_name", "CB:CB:HV:BOX:%s:%s:%s:VoltVariance" % (box, level, channel))
display.getWidget("graph_current_channel").setPropertyValue("trace_0_y_pv", "CB:CB:HV:BOX:%s:%s:%s:ReadVolt" % (box, level, channel))