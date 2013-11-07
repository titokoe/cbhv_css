from org.csstudio.opibuilder.scriptUtil import PVUtil

g = open ("/home/epics/streamApp/Tito/cbhv_elements_channel_map.txt", "r")
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
    
f = open ("/home/epics/CSS-Workspaces/Tito/CBHV/cbhv.opi", "r")

content = f.read()

f.close()

before_delimiter = "widget_property_access_tests.py\" checkConnect=\"false\" sfe=\"true\" seoe=\"false\">^M\n\t\t<pv trig=\"true\">sim://delayedConnectionChannel(0,0)</pv>^M"

after_delimiter = "</path"

content_split1 = content.split("widget_property_access_tests.py",1)

before_string = content_split1[0] + before_delimiter

content_split2 = content_split1[1].split("path", 1)

after_string = after_delimiter + content_split2[1]
    
count2 = 0
        
while count2 < len(mapelementarray):
    
    add_string = "\t\t<pv trig=\"false\">CB:HV:BOX:%s:%s:%s:read_volt</pv>\n\t\t<pv trig=\"false\">CB:HV:BOX:%s:%s:%s:set_volt</pv>\n\t\t<pv trig=\"false\">CB:HV:BOX:%s:%s:%s:volt_variance</pv>\n\t\t<pv trig=\"false\">CB:HV:ELEMENT:%s:set_volt</pv>\n" % (mapboxarray[count2],maplevelarray[count2],mapchannelarray[count2],mapboxarray[count2],maplevelarray[count2],mapchannelarray[count2],mapboxarray[count2],maplevelarray[count2],mapchannelarray[count2],mapelementarray[count2])
    before_string = before_string + add_string
    count2 = count2 + 1
    
count3 = 0

while count3 < numberofboxes:
    
    boxnumber = count3 + 1
    
    box_used = boxnumber in mapboxarray
    
    if box_used == True:
        
        add_box_string = "\t\t<pv trig=\"false\">CB:HV:BOX:%s:is_active</pv>\n\t\t<pv trig=\"false\">CB:HV:BOX:%s:status</pv>\n" % (boxnumber, boxnumber)
        before_string = before_string + add_box_string


    count3 = count3 + 1
        
        
    
file_string = before_string + after_string

f = open ("/home/epics/CSS-Workspaces/Tito/CBHV/cbhv.opi", "w")
f.write(file_string)
f.close()
    

    

