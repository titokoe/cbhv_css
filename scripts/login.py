from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil
from org.csstudio.opibuilder.scriptUtil import GUIUtil

check = GUIUtil.openPasswordDialog("Password", "a2messung")

if (check == True):
    
    display.getWidget("tabbed_container").setPropertyValue("tab_1_enabled", True)
    display.getWidget("enable_controls").setPropertyValue("enabled", False)
    display.getWidget("tabbed_container").setActiveTabIndex(1)
    