from org.csstudio.opibuilder.scriptUtil import PVUtil

widgetname = widget.getPropertyValue("pv_name")
nameparts = widgetname.split(":")

pvname = "CB:CB:HV:BOX:%s:%s:%s:InUse" % (nameparts[4],nameparts[5],nameparts[6])

pv = widget.getPVByName("%s" % pvname)

newpvvalue = -1

pvvalue = PVUtil.getLong(pv)

if pvvalue == 0:
    
    newpvvalue = 1
    
elif pvvalue == 1:
    
    newpvvalue = 0

pv = widget.getPVByName("%s" % pvname)

print pv

pv.setValue(newpvvalue)