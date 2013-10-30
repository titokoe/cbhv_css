import time
from org.csstudio.opibuilder.scriptUtil import PVUtil

combo_box = display.getWidget("combo_box").getValue()
combo_channel = display.getWidget("combo_channel").getValue()
combo_level = display.getWidget("combo_level").getValue()
element = int(display.getWidget("spinner_element").getValue())
filepath = display.getWidget("filepath").getValue()
message = display.getWidget("message")
numberofboxes = 20
pv_input = display.getWidget("engage")
radio_target = display.getWidget("radio_target").getValue()
radio_source = display.getWidget("radio_source").getValue()
voltage = int(display.getWidget("spinner_voltage").getValue())

g = open ("/home/epics/streamApp/Tito/cbhv_elements_channel_map.txt", "r")
maplines = g.readlines()
count = 0
mapelementarray = []
mapboxarray = []
maplevelarray = []
mapchannelarray = []
maplinearray = []

while count < len(maplines):
    mapline = maplines[count].split()
    mapelementarray.append(int(mapline[0]))
    mapboxarray.append(int(mapline[1]))
    maplevelarray.append(int(mapline[2]))
    mapchannelarray.append(int(mapline[3]))
    string = "%s %s %s" % (int(mapline[1]), int(mapline[2]), int(mapline[3]))
    maplinearray.append(string)    
    count = count + 1

if radio_source =="" or radio_target == "":
    
    message.setPropertyValue("text", "Specify source and/or target first")
    
else:
    
    ############################ Element -> selected Value #######################
    
    if radio_target == "Element" and radio_source == "selected Value":
        
        if element == -1 and voltage != 0:
            
            message.setPropertyValue("text", "Choose an element.")
                      
        elif voltage == 0 and element != -1:
            
            message.setPropertyValue("text", "Choose a voltage value.") 
            
        elif voltage == 0 and element == -1:
            
            message.setPropertyValue("text", "Choose a voltage value and an element.")
            
        else:
            
            elementexists = int(element) in mapelementarray
              
            if elementexists == False:
                
                message.setPropertyValue("text", "Element not in use/ unknown - choose another one")
                
            elif elementexists == True:             
                    
                pv_input.getPVByName("CB:HV:ELEMENT:%s:set_volt" % (element)).setValue(voltage)
                    
    ######################## Element -> File ###########################
    
    if radio_target == "Element" and radio_source == "File":
    
        if element == -1 and filepath != "":
        
            message.setPropertyValue("text", "Choose an element.")
                  
        elif filepath == "" and element != -1:
        
            message.setPropertyValue("text", "Choose a filepath.") 
        
        elif filepath == "" and element == -1:
        
            message.setPropertyValue("text", "Choose a filepath and an element.")
            
        else:
            
            f = open (filepath, "r")
            file_element_voltages = f.readlines()
            count = 0
            file_elementarray = []
            file_voltagearray = []

            while count < len(file_element_voltages):
                line = file_element_voltages[count].split()
                file_elementarray.append(int(line[0]))
                file_voltagearray.append(int(line[1]))  
                count = count + 1
                
            file_exist = element in file_elementarray
            file_element_voltage_exist = element in file_elementarray
                           
            if file_exist == False and file_element_voltage_exist == True:
                              
                message.setPropertyValue("text", "Element not in use/ unknown - choose another one.")
                
            elif file_element_voltage_exist == False and file_exist == True:
                              
                message.setPropertyValue("text", "Element not listed in voltage file - choose another one.")
                
            elif file_exist == False and file_element_voltage_exist == False:
                              
                message.setPropertyValue("text", "Element not in use/ unknown and not listed in voltage file - choose another one.")
            
            else:
                
                file_index = file_elementarray.index(element)
                file_voltage = file_voltagearray[file_index]             
                pv_input.getPVByName("CB:HV:ELEMENT:%s:set_volt" % (element)).setValue(file_voltage)
                
############################# Box -> selected Value ############################
    if radio_target == "Box":
        
        boxcount = 0
        check_boxarray = []
            
    # Checking for ticked boxes: Creation of an array with all boxes. Checked ones get an entry 1, unchecked ones an entry 0. After that checking if 1 is in the array at least once reveals if at least one box is checked.
            
        while boxcount < numberofboxes:
            
            check_boxarray.append(display.getWidget("check_box%d" % (boxcount+1)).getValue())
            boxcount = boxcount + 1  
                               
        one_box_checked = True in check_boxarray
    
        if radio_target == "Box" and radio_source == "selected Value":
            
            if one_box_checked == False and voltage != 0:
                
                message.setPropertyValue("text", "Check at least one box.")
                          
            elif voltage == 0 and one_box_checked == True:
                
                message.setPropertyValue("text", "Choose a voltage value.") 
                
            elif voltage == 0 and one_box_checked == False:
                
                message.setPropertyValue("text", "Choose a voltage value and check at least one box.")
                
            else:
                
                boxcount = 0
                
                while boxcount < numberofboxes:
                    
                        
                    if check_boxarray[boxcount] == False:
                        
                        boxcount = boxcount + 1
                    
                    elif check_boxarray[boxcount] == True:
                    
                        boxcount = boxcount + 1
                        
                        level = 0
                        
                        while level < 5:
                            
                            channel = 0
                        
                            while channel < 8:
                                
                                box_line = "%s %s %s" % (boxcount, level, channel)
                                
                                box_line_check = box_line in maplinearray
                                
                                if box_line_check == True:
                                    
                                    pv_input.getPVByName("CB:HV:BOX:%s:%s:%s:set_volt" % (int(boxcount), int(level), int(channel))).setValue(voltage)
                                    channel = channel + 1
                                    
                                if box_line_check == False:
                                    
                                    channel = channel + 1
                                    
                            level = level + 1                
     
        ######################## Box -> File ###########################
        
        if radio_target == "Box" and radio_source == "File":
            
            if one_box_checked == False and filepath != "":
                
                message.setPropertyValue("text", "Check at least one box.")
                          
            elif filepath == "" and one_box_checked == True:
                
                message.setPropertyValue("text", "Choose a file.") 
                
            elif filepath == "" and one_box_checked == False:
                
                message.setPropertyValue("text", "Choose a filepath and check at least one box.")
                
            else:
                
                f = open (filepath, "r")
                file_element_voltages = f.readlines()
                count = 0
                file_elementarray = []
                file_voltagearray = []
    
                while count < len(file_element_voltages):
                    line = file_element_voltages[count].split()
                    file_elementarray.append(int(line[0]))
                    file_voltagearray.append(int(line[1]))  
                    count = count + 1
                    
                boxcount = 0
                
                while boxcount < numberofboxes:
                    
                        
                    if check_boxarray[boxcount] == False:
                        
                        boxcount = boxcount + 1
                    
                    elif check_boxarray[boxcount] == True:
                    
                        boxcount = boxcount + 1
                        
                        level = 0
                        
                        while level < 5:
                            
                            channel = 0
                        
                            while channel < 8:
                                
                                box_line = "%s %s %s" % (boxcount, level, channel)
                                
                                box_line_check = box_line in maplinearray
                                
                                if box_line_check == True:
                                    
                                    box_line_index = maplinearray.index(box_line)
                                    box_line_element = mapelementarray[box_line_index]
                                    map_file_match = box_line_element in file_elementarray
                                    
                                    if map_file_match == True:
                                    
                                        file_voltage_index = file_elementarray.index(box_line_element)
                                        file_voltage = file_voltagearray[file_voltage_index]
                                        pv_input.getPVByName("CB:HV:BOX:%s:%s:%s:set_volt" % (int(boxcount), int(level), int(channel))).setValue(file_voltage)
                                        channel = channel + 1
                                    
                                    if map_file_match == False:
                                        
                                        channel = channel + 1
                                    
                                if box_line_check == False:
                                    
                                    channel = channel + 1
                                    
                            level = level + 1
                            
############################# Channel -> selected Value ############################
    
    if radio_target == "Channel":
        
        ch_box = display.getWidget("combo_box").getValue()
        ch_level = display.getWidget("combo_level").getValue()
        ch_channel = display.getWidget("combo_channel").getValue()
        
        if radio_target == "Channel" and radio_source == "selected Value":
            
            if ch_box == "" or ch_level == "" or ch_channel == "":
                
                channel_selected = False
                
            else:
                
                channel_selected = True
            
            if channel_selected == False and voltage != 0:
                
                message.setPropertyValue("text", "Choose a value for box, level and channel..")
                          
            elif voltage == 0 and channel_selected == True:
                
                message.setPropertyValue("text", "Choose a voltage value here2 %s." % voltage) 
                
            elif voltage == 0 and channel_selected == False:
                
                message.setPropertyValue("text", "Choose a voltage value and a value for box, level and channel.")
                
            else:
                
                ch_pv = pv_input.getPVByName("CB:HV:BOX:%s:%s:%s:set_volt" % (ch_box, ch_level, ch_channel))
                
                if ch_pv == "None":
                    
                    message.setPropertyValue("text", "Chosen channel not known.")
                    
                else:
                    
                    ch_pv.setValue(voltage)
                    
############################# Channel -> File ############################
                    
        if radio_target == "Channel" and radio_source == "File":
            
            if channel_selected == False and filepath != "":
                
                message.setPropertyValue("text", "Choose a value for box, level and channel..")
                          
            elif filepath == "" and channel_selected == True:
                
                message.setPropertyValue("text", "Choose a file.") 
                
            elif filepath == "" and channel_selected == False:
                
                message.setPropertyValue("text", "Choose a file and a value for box, level and channel.")
                
            else:
                
                f = open (filepath, "r")
                file_element_voltages = f.readlines()
                count = 0
                file_elementarray = []
                file_voltagearray = []
    
                while count < len(file_element_voltages):
                    
                    line = file_element_voltages[count].split()
                    file_elementarray.append(int(line[0]))
                    file_voltagearray.append(int(line[1]))  
                    count = count + 1
                
                ch_line = "%s %s %s" % (ch_box, ch_level, ch_channel)
            
                ch_line_check = ch_line in maplinearray
                
                if ch_line_check == False:
                    
                    message.setPropertyValue("text", "Chosen channel not known.")
                    
                else:
                    
                    ch_line_index = maplinearray.index(ch_line)
                    ch_element = mapelementarray[ch_line_index]                    
                    map_line_match = ch_element in file_elementarray
                    
                    if map_line_match == False:
                        
                        message.setPropertyValue("text", "No correpsonding element for the chosen channel listed in voltage file.")
                        
                    else:
                        file_voltage_index = file_elementarray.index(ch_element)
                        file_voltage = file_voltagearray[file_voltage_index]
                        pv_input.getPVByName("CB:HV:BOX:%s:%s:%s:set_volt" % (ch_box, ch_level, ch_channel)).setValue(file_voltage)
                        
                        
                    
                    
            
        
                            

                    
                
           
