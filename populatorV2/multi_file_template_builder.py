'''The app uses the map file to draw in multiple files and output
the information in those files according to a common templete'''


import pandas as pd

def multi_file_pop():

    map_dictionary = {}

    #load outputnfile
    '''*****MAP FILE NAME****'''
    with open('itemMapFirstClean.txt') as file:

        for line in file:
            #convert data_mao into string into list
            raw_data_map_list = line.split(",")

    '''template headers are every header nth space in list'''

    template_header_distance = 4
    first_template_header_postion = 1

    header_list = []
    stop_adding = False
    data_map_list = []
    dataMapList_position = 0

    data_map_dictionary = {}
    
    for entry in raw_data_map_list:
        current_map_unit = []
        if entry == 'FILENAME' or entry == 'EMPTY':

            '''populate header list'''
            if dataMapList_position > 0:

                if entry == 'FILENAME':
                    stop_adding = True
                    
                if stop_adding == False:
                    header_list.append(raw_data_map_list[dataMapList_position + 1])

            else:
                header_list.append(raw_data_map_list[dataMapList_position + 1])
            
            
            '''creating list of used Fields'''
            if raw_data_map_list[dataMapList_position + 3] == 'EMPTY':
                dataMapList_position += 1
                continue
            else:
               current_map_unit.append(raw_data_map_list[dataMapList_position + 1])
               current_map_unit.append(raw_data_map_list[dataMapList_position + 2])
               current_map_unit.append(raw_data_map_list[dataMapList_position + 3])
               current_map_unit.append(raw_data_map_list[dataMapList_position + 4])
               dataMapList_position += 1
               data_map_list.append(current_map_unit)
               continue

        else:
           dataMapList_position += 1
           continue        
    

    list_size = 0


    '''turning used input list into dictionary'''
    for entry in data_map_list:
        
        key = []
        key.append(entry[2])
        key.append(entry[3])
        key_str = str(key)
        
        if key_str not in data_map_dictionary:
    
            data_map_dictionary[key_str] = (entry[0], entry[1])


    '''removing unused headers from header list'''
    used_headers = []
    for key in data_map_dictionary:
        used_headers.append(data_map_dictionary[key][0])

   

    for header in header_list:
        if header not in used_headers:
            header_list.remove(header)
            
    

    return data_map_dictionary, header_list




