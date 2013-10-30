from org.csstudio.opibuilder.scriptUtil import PVUtil

display.getWidget("graph_current_channel").clearGraph()

name = widget.getPropertyValue("pv_name")


array = name.split(":")
box = array[3]
level = array[4]
channel = array[5]

display.getWidget("label_selected_channel").setPropertyValue("text", "CB:HV:BOX:%s:%s:%s" % (box, level, channel))
display.getWidget("current_voltage").setPropertyValue("pv_name", "CB:HV:BOX:%s:%s:%s:read_volt" % (box, level, channel))
display.getWidget("current_variance").setPropertyValue("pv_name", "CB:HV:BOX:%s:%s:%s:volt_variance" % (box, level, channel))
display.getWidget("graph_current_channel").setPropertyValue("trace_0_y_pv", "CB:HV:BOX:%s:%s:%s:read_volt" % (box, level, channel))