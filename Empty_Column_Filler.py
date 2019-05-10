'''control module for controlling second run manditory field filling'''

def empty_cell_filler(header):

    if header == 'currency':
        return 'US Dollar'

    elif header == 'exchangerate' or header == 'itemLine_rate':
        return 1

    elif header == 'orderstatus':
        return 'approved'

    else:
        return 'FILL'



def mandatory_empty_cell_filler_control(header, control_string):

    if control_string == "STANDARD_CELL":

        return empty_cell_filler(header) 

        
