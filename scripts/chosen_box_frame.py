from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil


box = widget.getPropertyValue("name")
box = int(box)
display.getWidget("tabbed_container").setActiveTabIndex(0)

numberofboxes = 19

count = 1

while count <= numberofboxes:

    display.getWidget("%d" % count).setPropertyValue("border_width", "0")
    count = count + 1

widget.setPropertyValue("border_width", "4")