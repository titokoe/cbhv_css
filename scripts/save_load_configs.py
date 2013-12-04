from org.csstudio.opibuilder.scriptUtil import PVUtil

save_load_configs_pv = display.getWidget("save_load_configs_radio").getPV()

save_load_option = PVUtil.getString(save_load_configs_pv)

message = ""

if save_load_option == "Save voltage configuration":
    
    print 'here'
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    
    filename_pv = display.getWidget("save_load_configs_filename").getPV()
    filename = PVUtil.getString(filename_pv)
    
    if filename=="" or filepath == "":
        
        message = 'Please choose directory and/ or filename first.'
        
    else:
        
        message = ""
        
        file = filepath + "/" + filename
        
        f= open(file, "w")        
        
        box = 19        
        
        while box < 20:
            
            level = 0
            
            while level < 5:
                
                channel = 0
                
                while channel < 8:
                    
                    voltage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:LatestSetVolt" % (box, level, channel))
                    voltage = PVUtil.getLong(voltage_pv)
                    f.write("%s %s %s %s\n" % (box, level, channel, voltage))
                    
                    channel+=1
                    
                level+=1
                
            box+=1
            
        f.close()
        
if save_load_option == "Save channel usage configuration":
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    
    filename_pv = display.getWidget("save_load_configs_filename").getPV()
    filename = PVUtil.getString(filename_pv)
    
    if filename=="" or filepath == "":
        
        message = 'Please choose directory and/ or filename first.'
        
    else:
        
        message = ""
        
        file = filepath + "/" + filename
        
        f= open(file, "w")        
        
        box = 19        
        
        while box < 20:
            
            level = 0
            
            while level < 5:
                
                channel = 0
                
                while channel < 8:
                    
                    usage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:InUse" % (box, level, channel))
                    usage = PVUtil.getLong(usage_pv)
                    f.write("%s %s %s %s\n" % (box, level, channel, usage))
                    
                    channel+=1
                    
                level+=1
                
            box+=1
            
        f.close()
        
if save_load_option == "Load voltage configuration":
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    
    if filepath == "":
        
        message = 'Please choose file first.'
        
    else:
        
        message = ""
        
        f= open(filepath, "r")
        lines = f.readlines()
        f.close()       
        
        linecount = 0
        
        while linecount < len(lines):
        
            lineparts = lines[linecount].split()
            voltage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:LatestSetVolt" % (lineparts[0], lineparts[1], lineparts[2]))
            voltage = voltage_pv.setValue(lineparts[3])
            
            linecount+=1
            
if save_load_option == "Load channel usage configuration":
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    
    if filepath == "":
        
        message = 'Please choose file first.'
        
    else:
        
        message = ""
        
        print filepath
        
        f= open(filepath, "r")
        lines = f.readlines()
        f.close()       
        
        linecount = 0
        
        while linecount < len(lines):
        
            lineparts = lines[linecount].split()
            usage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:InUse" % (lineparts[0], lineparts[1], lineparts[2]))
            usage = usage_pv.setValue(lineparts[3])
            
            linecount+=1
            
display.getWidget("configuration_message").setPropertyValue("text", message)
                    
                    