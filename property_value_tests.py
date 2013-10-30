from org.csstudio.opibuilder.scriptUtil import PVUtil
import time

#display.getWidget("spinner_element").setValue(-1)
checkpoint = display.getWidget("message")

voltage = display.getWidget("spinner_voltage").getValue()
display.getWidget("pv_input").setPropertyValue("pv_name", "CB:HV:BOX:19:0:0:set_volt")
display.getWidget("pv_input").setPropertyValue("pv_name", "CB:HV:BOX:19:0:0:set_volt")
display.getWidget("pv_input").getPV().setValue(voltage)

#text = listendings.index(4)
#checkpoint.setPropertyValue("text", text)

#one = display.getWidget("check_box1").getValue()
#two = display.getWidget("check_box2").getValue()
#count = 1
#numberofboxes = 20
#sum = 0
#while count <= numberofboxes:
            
#            sum = sum + int(display.getWidget("check_box%d" % count).getValue())
#            count = count + 1
            

#g = open ("/home/epics/streamApp/Tito/cbhv_elements_channel_map.txt", "r")
#maplines = g.readlines()
#count = 0
#elementarray = []
#boxarray = []
#levelarray = []
#channelarray = []
#linearray = []

#test = len(maplines)
#test = maplines[0].split()

#while count < len(maplines):
#    mapline = maplines[count].split()
#    checkpoint.setPropertyValue("text", mapline)
#    time.sleep(5)
    
#    elementarray.append(mapline[0])
#    boxarray.append(mapline[1])
#    levelarray.append(mapline[2])
#    channelarray.append(mapline[3])
#    string = "%s %s %s" % (mapline[1], mapline[2], mapline[3])
#    linearray.append(string)    
#    count = count + 1
    
#test = linearray[0]

#checkpoint.setPropertyValue("text", test)

#if radio == "Box":
#    box = display.getWidget("box").getValue()
#    level = display.getWidget("level").getValue()
#    channel = display.getWidget("channel").getValue()
#    if box == "" or level =="" or channel == "":
#        display.getWidget("label").setPropertyValue("text", "Specify Box/Level/Channel!!")
#    else:
#        boxvariable = display.getWidget("engage").getPVByName("CB:HV:BOX:%s:%s:%s:set_volt" % (box, level, channel))
#        boxvariable.setValue(voltage)
#            
#if radio == "File":
#    path = display.getWidget("filepath").getValue()
#    if path == "":
#        display.getWidget("label").setPropertyValue("text", "Specify filepath first") 
#    else:
 #       f = open (path, "r")
 #       werte = f.readlines()
 #       f.close
 #       count = 0
 #       length = len(werte) - 1    
 #       print len(werte)

#        while (count < length):
#
#            zeilenwerte = werte[count].split()
#            
#            if (len(zeilenwerte) == 2):
#                
#                pathvariable = display.getWidget("engage").getPVByName("CB:HV:ELEMENT:%s:set_volt" % (zeilenwerte[0]))
 #               pathvariable.setValue(zeilenwerte[1])
 #               count = count + 1
 #               print zeilenwerte[0]
 #               print zeilenwerte[1]
 #               print pathvariable
        
 #           else:

  #              count = count + 1
    