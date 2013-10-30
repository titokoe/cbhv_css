from org.csstudio.opibuilder.scriptUtil import PVUtil

numberofboxes = 20

count = 1

while count <= numberofboxes:
    
    display.getWidget("check_box%s" % count).setValue(False)
    count = count + 1
