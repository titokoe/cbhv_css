from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil
from org.csstudio.opibuilder.scriptUtil import GUIUtil

check = GUIUtil.openPasswordDialog("Password", "a2messung")

if (check == True):
#    value = display.getWidget("tabbed_container").getWidget("Control").getPropertyValue("background_color")
    display.getWidget("Control").setPropertyValue("enabled", True)
    display.getWidget("enable_controls").setPropertyValue("enabled", False)
#    controltab = display.getWidget("tabbed_container").getChild("Control")
 #   test = controltab.setPropertyValue("enabled", True)
    