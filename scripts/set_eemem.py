from org.csstudio.opibuilder.scriptUtil import PVUtil
import os, time

numberofboxes = 19
check_eemem_boxarray =[]
eemem_message = display.getWidget("eemem_message")
set_eemem = display.getWidget("eemem_choice").getPV()
set_eemem_choice = PVUtil.getString(set_eemem)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if set_eemem_choice == "":
    
    eemem_message.setPropertyValue("text","Please select which values to change and alter at least one of them.")
    
####################### SetEemem => Cards ###############################

elif set_eemem_choice == "Cards":
    
    cardscount = 0
    empty_cards = 0
    cards_message =""
    
    ################ check if calibration file exists #################
    
    filepath = display.getWidget("eemem_cards_cal_file").getValue()
            
    check_filepath = os.path.isfile(filepath)
            
    if check_filepath == False:
                
        cards_message = cards_message + 'No calibration file specified or the file is gone.\n'
            
    elif check_filepath == True:
                
        f = open (filepath, "r")
        cal_lines = f.readlines()
        count = 0
        cal_card_array = []
        cal_channel_array = []
        cal_gradient_array = []
        cal_offset_array = []
        
        ##################### read and check if lines in calibration file contain 4 arguments that are only numbers - only the values of these lines are stored in arrays for card, channel, gradient and offset #
        
        while count < len(cal_lines):
                    
            cal_line_parts = cal_lines[count].split(",")
                    
            if len(cal_line_parts) != 4:
                        
                cards_message = cards_message + "Wrong number of arguments in line %s of the calibration file.\n" % count
                        
            else:
                
                cal_digitcount = 0
                cal_all_digits = 0
                
                while cal_digitcount < 4:
                    
                    check_cal_digits = is_number(cal_line_parts[cal_digitcount])
                        
                    if check_cal_digits == False:
                            
                        cards_message = cards_message + "Forbidden characters found in new cards for box %s. Only digits are allowed.\n" % cardscount
                            
                        break
                    cal_digitcount+=1
                        
            if check_cal_digits == True:
                        
                cal_card_array.append(cal_line_parts[0])
                cal_channel_array.append(cal_line_parts[1])
                cal_gradient_array.append(cal_line_parts[2])
                cal_offset_array.append(cal_line_parts[3])
                        
            count+=1
    
    ############ check if the number of cards entered in css is correct and if the cardnumbers are really only digits #        
            
    print cal_card_array             
    
    while cardscount < numberofboxes:
        
        print cardscount
        cardscount+=1
        print cardscount
        cards_pv = display.getWidget("Cards%d" % cardscount).getPV()
        new_cards = PVUtil.getString(cards_pv)
        new_cards_parts = new_cards.split(",")
        
        if new_cards == "":
            
            empty_cards+=1
        
        elif new_cards != "" and len(new_cards_parts) != 5:
            
            cards_message = cards_message + "Wrong number of cards at Box %d. 5 cards separated by \",\" are expected.\n" % cardscount
            
        elif new_cards !="" and len(new_cards_parts) == 5:
            
            digitcount = 0
            all_digits = 0
                
            while digitcount < 5:
                    
                check_cards_digits = new_cards_parts[digitcount].isdigit()
                    
                if check_cards_digits == False:
                        
                    cards_message = cards_message + "Forbidden characters found in new cards for box %s. Only digits are allowed\n" % cardscount    
                    break
                digitcount+=1
                
                print check_cards_digits
                    
            if check_cards_digits == True:
                    
                count0 = 0
                
                ######### search for indices in the cards array for the entered cards -> this way the indices of the channel, gradient and offset values for the cards are obtained
                    
                while count0 < 5:
                        
                    cards_ch_indices = [i for i,val in enumerate(cal_card_array) if val == new_cards_parts[count0]]
                    
                    count1 = 0
                    
                    while count1 < 8:
                    
                        display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:WriteM%s_%s" % (cardscount, count0, count1)).setValue("%s" % (cal_gradient_array[cards_ch_indices[count1]]))
                        display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:WriteN%s_%s" % (cardscount, count0, count1)).setValue("%s" % (cal_offset_array[cards_ch_indices[count1]]))
                        
                        count1+=1
                        
                    count0+=1
                    

                
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:UnprotectEememCards" % (cardscount)).setValue("go")                
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:SetCardsAndMN" % (cardscount)).setValue("%s" % new_cards)                   
            if empty_cards == numberofboxes:
                
               eemem_message.setPropertyValue("text", "Enter at least 1 new set of cards.")
        
            else:
                
                eemem_message.setPropertyValue("text", "%s" % cards_message)
            
###################### SetEemem => IP ###############################

elif set_eemem_choice == "Ip":
    
    ipcount = 0
    empty_ip = 0
    ip_message =""
    
    while ipcount < numberofboxes:
        
        ipcount+=1
        
        ip_pv = display.getWidget("Ip%d" % ipcount).getPV()
        new_ip = PVUtil.getString(ip_pv)
        new_ip_parts = new_ip.split(".")
        
        if new_ip == "":
            
            empty_ip+=1
        
        elif new_ip != "" and len(new_ip_parts) != 4:
            
            ip_message = ip_message + "Wrong IP format at Box %d. 4 blocks of digits separated by \".\" are expected." % ipcount
            
        elif new_ip !="" and len(new_ip_parts) == 4:
            
            digitcount = 0
            all_digits = 0
            
            while digitcount < 4:
                
                check_ip_digits = new_ip_parts[digitcount].isdigit()
                
                if check_ip_digits == False:
                    
                    ip_message = ip_message + "Forbidden characters found in new IP for box %s. Only digits are allowed" % ipcount
                    
                    break
                digitcount+=1
                
            if check_ip_digits == True:
                
                print "here"
                
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:UnprotectEemem" % (ipcount)).setValue("go")
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:SetIp" % (ipcount)).setValue("%s" % new_ip)
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:ReloadEemem" % (ipcount)).setValue("go")
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:ProtectEemem" % (ipcount)).setValue("go")
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:PrintEemem" % (ipcount)).setValue("go")
                
    if empty_ip == numberofboxes:
            
        eemem_message.setPropertyValue("text", "Enter at least 1 new IP.")
            
    else:
            
        eemem_message.setPropertyValue("text", "%s" % ip_message)
            
#################### Set Eemem => Mac ###################
            

elif set_eemem_choice == "Mac":
    
    maccount = 0
    empty_mac = 0
    mac_message =""
    
    while maccount < numberofboxes:
        
        maccount+=1
        
        mac_pv = display.getWidget("Ip%d" % maccount).getPV()
        new_mac = PVUtil.getString(mac_pv)
        new_mac_parts = new_mac.split(":")
        
        if new_mac == "":
            
            empty_mac+=1
        
        elif new_mac != "" and len(new_mac_parts) != 6:
            
            mac_message = mac_message + "Wrong Mac format at box %d. 6 blocks of digits and/or letters separated by \":\" are expected." % ipcount
            
        elif new_mac !="" and len(new_mac_parts) == 6:
            
            charcount = 0
            all_char = 0
            
            while charcount < 6:
                
                check_mac_chars = len(new_mac_parts[charcount])
                
                if check_mac_chars != 2:
                    
                    mac_message = mac_message + "Wrong number of characters found in new Mac for box %s. Only 2 characters are allowed between \":\"." % ipcount
                    
                    break
                charcount+=1
                
            if check_mac_chars == 2:
                
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:UnprotectEemem" % (maccount)).setValue("go")
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:SetMac" % (maccount)).setValue("%s" % new_mac)
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:ReloadEemem" % (maccount)).setValue("go")
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:ProtectEemem" % (maccount)).setValue("go")
                display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:PrintEemem" % (maccount)).setValue("go")
                
    if empty_mac == numberofboxes:
            
        eemem_message.setPropertyValue("text", "Enter at least 1 new Mac.")
            
    else:
            
        eemem_message.setPropertyValue("text", "%s" % mac_message)
            
        
############################ SetEemem => General Values ###################

elif set_eemem_choice == "General values":

    eemem_values = ["Dhcp", "Mask", "Gate", "Dns", "Ntpserver", "Utczone", "Ntp", "Umin", "Umax", "Reg", "Regn", "Reg_div", "Levels", "Mem", "File", "Lease"]
    
    count = 0
    
    while count < numberofboxes:
                
                check_eemem_boxarray.append(display.getWidget("eemem_check_box%d" % (count+1)).getValue())
                count+=1  
                                   
    one_box_checked = True in check_eemem_boxarray
    
    if one_box_checked == False:
        
        eemem_message.setPropertyValue("text", "Choose at least one box.")
        
    else:
        
        eemem_valuearray = []
        
        count1 = 0
        
        while count1 < len(eemem_values):
            
            name = display.getWidget("Set%s" % eemem_values[count1]).getPV()
            eemem_value = eemem_values[count1]
            value = PVUtil.getString(name)
            whitespace_check = "".join(value.split())
            
            if value != None and whitespace_check != "":
                
                if eemem_value == "Utczone" or eemem_value == "Umin" or eemem_value == "Umax" or eemem_value == "Regn" or eemem_value == "Levels" or eemem_value == "Mem" or eemem_value == "Lease":
                    
                    array = value.split(".")
                    value = array[0]
                
                array_value = "%s_%s" % (eemem_values[count1], value)
                array_value = str(array_value)
                eemem_valuearray.append(array_value)
                
            count1+=1
            
        if len(eemem_valuearray) == 0:
            
            eemem_message.setPropertyValue("text", "Enter at least one new eemem value.")
            
        else:
            
            count2 = 0
            
            while count2 < numberofboxes:
                
                if check_eemem_boxarray[count2] == True:
                    
                    display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:UnprotectEemem" % (count2+1)).setValue("go")
                    
                    count3 = 0
                    
                    while count3 < len(eemem_valuearray):
                        
                        eemem_set_valuearray = eemem_valuearray[count3].split("_")
                       
                        display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:Set%s" % (count2+1, eemem_set_valuearray[0])).setValue("%s" % eemem_set_valuearray[1])
                        
                        count3+=1
                            
                    display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:ReloadEemem" % (count2+1)).setValue("go")
                    display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:ProtectEemem" % (count2+1)).setValue("go")
                    display.getWidget("set_eemem").getPVByName("CB:CB:HV:BOX:%s:PrintEemem" % (count2+1)).setValue("go")
                      
                count2+=1
       
