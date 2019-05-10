'''Template Filler Version 3
Douglas Oak November 2018'''


import pandas as pd
from Dynamic_Data_Dictionary_Active import Dynamic_Data_Info
from General_Cleaning import General_Cleaning
from Additional_Actions import Special_Actions
from Empty_Column_Filler import mandatory_empty_cell_filler_control

'''nameof incomming files'''
file = 'OpenARInvoiceNatuoilNov28.csv'
manditory_missing_data_flag = "FILL"
ouput_df_new_row_place_holder_value = " "
new_row_append_list = []
output_df_index = 0


'''import data dictionary'''
data_dictionary = Dynamic_Data_Info('OpenARInvoice')

output_df_header_list = []
manditory_header_list = []

'''builda list of output headers and manditory headers'''

for key in data_dictionary:
    output_df_header_list.append(data_dictionary[key][0])


    '''if the header is manditory IE the data dictionary position 2 lists as true add the manditory list'''
    if data_dictionary[key][2] == True:
        manditory_header_list.append(data_dictionary[key][0])

'''create output data frame'''
output_df = pd.DataFrame(columns=output_df_header_list)

'''load import data into a dataframe'''
input_df = pd.read_csv(file,encoding = "ISO-8859-1")

'''create list of input file headers'''
input_header_list = input_df.columns

'''iterate through input dataframe cells'''

for column in output_df_header_list:
    new_row_append_list.append(ouput_df_new_row_place_holder_value)

for index, row in input_df.iterrows():

    '''create new row for output dataframe'''

    new_row = pd.Series(new_row_append_list, index=output_df_header_list)

    '''append blank row to output dataframe'''
    output_df = output_df.append(new_row,ignore_index=True)

    
    '''take input header list and iterate through list'''
    for header in input_header_list:

        '''select individual cell data'''
        cell_data = row[header]

        '''filter out NAN data'''
        if pd.isnull(cell_data) == True:
            continue

        try:
            '''Try to send input header to data dictionary and extract data cleaning list'''
            clean_list = data_dictionary[header]
            

        except:
            continue


        '''Unpacking Clean List'''

        output_header = clean_list[0]
        data_type = clean_list[1]
        manditory = clean_list[2]
        max_length = clean_list[3]
        additional_actions = clean_list[4]


        '''General Cell Data Cleaning'''
        clean_cell_data = General_Cleaning(cell_data, data_type, max_length,)

        '''Check For additional Cleaning'''
        if additional_actions == True:
            extra_cleaning = clean_list[5]
            extra_cleaning_location = clean_list[6]
            additional_action_data = Special_Actions(clean_cell_data, extra_cleaning)
            

        '''write Cell Data to output data frame'''
        output_df.iloc[output_df_index][output_header] = clean_cell_data

        '''if addtional cleaning write additional cleaning to cells'''
        if additional_actions == True:
            output_df.iloc[output_df_index][extra_cleaning_location] = additional_action_data

    output_df_index += 1

'''flag any empty manditory cells in the output dataframe'''
second_run_index = 0
for index, row in output_df.iterrows():

    for manditory_header in manditory_header_list:
        manditory_cell = row[manditory_header]


        '''Code for filling in empty manditory cells'''

        
        if manditory_cell == " ":
            output_df.iloc[second_run_index][manditory_header] = Empty_Column_Filler(manditory_header)
        
                
        
    second_run_index += 1    
'''prompt for file to write too'''

out_file_name = input("Enter Output File Name: ")

print("writing to file")
output_df.to_csv(out_file_name)
            

        

        
