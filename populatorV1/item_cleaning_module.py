'''Cleaning module testing file'''

def entry_clean(entry,header, clean_dictionary):

    '''limit max entry length'''
    try:
        entry = entry[0:59]

    except:
        no_item = 0

    if entry == 'QUERY':
    
        if header in clean_dictionary:
            return clean_dictionary[header]

        else:
            return "No Match"

    '''load general rules'''
    general_rules = clean_dictionary['all headers']

    '''apply general rules'''
    for rule in general_rules:

        if rule[0] == entry:
            entry = rule[1]

    '''look for entry in cleaning dictionary'''
    if header in clean_dictionary:
        '''load header conversion code'''
        conversion_list = (clean_dictionary[header])

        

        for position in conversion_list:
            
            if position[0] == entry:
                entry = position[1]

            if len(position) > 2:

                if position[2] == 'split':
                    split_item = entry.split(position[3])
                    entry = split_item[position[4]]

            if len(position) > 5:
                new_header = position[5]

                try:
                    new_entry = split_item[position[6]]
                except:
                    new_entry = "Flag"

                entry_return = (entry, new_header, new_entry)
               

                return entry_return, True

    return entry, False

def number_clean(entry,header, clean_dictionary):

    
    if entry == 'QUERY':
    
        if header in clean_dictionary:
            return clean_dictionary[header]

        else:
            return "No Match"

    '''load general rules'''
    general_rules = clean_dictionary['all headers']

    '''apply general rules'''
    for rule in general_rules:

        if rule[0] == entry:
            entry = rule[1]

    '''look for entry in cleaning dictionary'''
    if header in clean_dictionary:
        '''load header conversion code'''
        conversion_list = (clean_dictionary[header])

        for position in conversion_list:
            
            if position[0] == entry:
                entry = position[1]

            if len(position) > 2:

                if position[2] == 'split':
                    split_item = entry.split(position[3])
                    entry = split_item[position[4]]

            if len(position) > 5:
                new_header = position[5]
                new_entry = split_item[position[6]]
                return entry, new_header, new_entry

    return entry
