from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import FileUtil
import os

# needs to be changed to a place where people can actually read the message when in configuration tab!

message = display.getWidget("message")

opifilepath = display.getModel().getOpiFilePath().toString()
workspacepath = FileUtil.workspacePathToSysPath("/")
                
path = workspacepath + opifilepath  

pathreverse = path[::-1] ############### reverse string to remove name of opi file #########

pathsplit = pathreverse.split("/",1)

folder = pathsplit[1]

configfilepath = folder[::-1]

configfile = configfilepath + "/cbhv_config.txt"

check_config = os.path.isfile(configfile)

check_mapfile = False

if check_config == True:
    
    h = open(configfile, "r")
    configdata = h.readlines()
    h.close()
    
    check_mapfile = os.path.isfile(configdata[0])
    
if check_config == False or check_mapfile == False:
    
    message.setPropertyValue("text", "Config- or/and mapfile is/are missing!")
    
else:

    g = open (configdata[0], "r")
    maplines = g.readlines()
    g.close()
    count2 = 0
    mapelementarray = []
    mapboxarray = []
    maplevelarray = []
    mapchannelarray = []
    maplinearray = []
    numberofboxes = 20
    
    count = 0
    
    while count < len(maplines):
        mapline = maplines[count].split()
        mapelementarray.append(int(mapline[0]))
        mapboxarray.append(int(mapline[1]))
        maplevelarray.append(int(mapline[2]))
        mapchannelarray.append(int(mapline[3]))
        string = "%s %s %s" % (int(mapline[1]), int(mapline[2]), int(mapline[3]))
        maplinearray.append(string)    
        count = count + 1
        
    f = open (path, "r")
    
    content = f.read()
    
    f.close()
    
    before_delimiter = "set_volt.py\" checkConnect=\"false\" sfe=\"true\" seoe=\"false\">^M\n\t\t<pv trig=\"true\">sim://delayedConnectionChannel(0,0)</pv>^M"
    
    after_delimiter = "</path"
    
    content_split1 = content.split("set_volt.py",1)
    
    before_string = content_split1[0] + before_delimiter
    
    print content_split1[1]
    
    content_split2 = content_split1[1].split("path", 1)
    
    after_string = after_delimiter + content_split2[1]
        
    count2 = 0
            
    while count2 < len(mapelementarray):
        
        add_string = "\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:ReadVolt</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:SetVolt</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:%s:%s:VoltVariance</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:ELEMENT:%s:SetVolt</pv>\n" % (mapboxarray[count2],maplevelarray[count2],mapchannelarray[count2],mapboxarray[count2],maplevelarray[count2],mapchannelarray[count2],mapboxarray[count2],maplevelarray[count2],mapchannelarray[count2],mapelementarray[count2])
        before_string = before_string + add_string
        count2 = count2 + 1
        
    count3 = 0
    
    while count3 < numberofboxes:
        
        boxnumber = count3 + 1
        
        box_used = boxnumber in mapboxarray
        
        if box_used == True:
            
            add_box_string = "\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:IsActive</pv>\n\t\t<pv trig=\"false\">CB:CB:HV:BOX:%s:Status</pv>\n" % (boxnumber, boxnumber)
            before_string = before_string + add_box_string
    
    
        count3 = count3 + 1
            
            
        
    file_string = before_string + after_string
    
    f = open (path, "w")
    f.write(file_string)
    f.close()
    

    

