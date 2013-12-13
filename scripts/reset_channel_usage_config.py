from org.csstudio.opibuilder.scriptUtil import PVUtil

box = 1

while box < 20:
    
    level = 0
    
    while level < 5:
        
        channel = 0
    
        while channel < 8:          

            getpv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:WriteInUse" % (box, level, channel))
            newvalue = PVUtil.getLong(getpv)
            print newvalue
            newvalue = int(newvalue)
            setpv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:InUse" % (box, level, channel))
            setpv.setValue(newvalue)
            
            channel+=1
            
        level+=1
        
    box+=1
            
            

