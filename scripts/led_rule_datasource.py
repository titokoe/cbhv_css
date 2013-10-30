from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil

variance = widget.getPV().getValue()

led_name = widget.getPropertyValue("name")

widget.getPVByName("loc://%s" % led_name).setValue(variance)