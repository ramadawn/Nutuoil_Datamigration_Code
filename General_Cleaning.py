'''This Module Handles General Cleaning Tasks'''

import math

def General_Cleaning(cell_data, data_type, max_length, header):

   


    '''ensures data cell is entered as the right type of data'''
    if data_type == str or data_type == list:
        cell_data = str(cell_data)
        
    elif data_type == int:
        try:
            cell_data = int(cell_data)

        except:
            print("General Cleaning Exception Header = ",header, "Data Type int")

    elif data_type == float:
        try:
            cell_data = float(cell_data)
        except:
            print("cell data type cleaning error cell data = ",cell_data, " data type = ", data_type)

    else:
        return "Data Type Error"

    '''checks max length'''
    if type(cell_data) == str:
        if len(cell_data) > max_length:
            cell_data = cell_data[:max_length]
    


    return cell_data




