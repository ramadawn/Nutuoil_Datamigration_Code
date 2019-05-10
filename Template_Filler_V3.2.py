'''Template Filler Version 3.2
Douglas Oak November 2018'''


import pandas as pd
from Dynamic_Data_Dictionary_Active import Dynamic_Data_Info
from General_Cleaning import General_Cleaning
from Additional_Actions import Special_Actions
from Empty_Column_Filler import mandatory_empty_cell_filler_control
from Label_Prompt import templateID_prompt
from location_translator import location_translation

'''initialized variables'''
manditory_missing_data_flag = "FILL"
ouput_df_new_row_place_holder_value = " "
new_row_append_list = []
output_df_index = 0


'''name of incomming file'''
input_file = 'OpenVendorCreditNatuoil.csv'

'''full path'''
input_path = "./input_files/"

file = input_path + input_file

'''request template label'''
template_label = templateID_prompt()

'''import data dictionary'''
data_dictionary = Dynamic_Data_Info(template_label)

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

'''create second output data frame'''
final_output_df = pd.DataFrame(columns=output_df_header_list)

'''load import data into a dataframe'''
input_df = pd.read_csv(file,encoding = "ISO-8859-1",low_memory=False)

'''create list of input file headers'''
input_header_list = input_df.columns

'''iterate through input dataframe cells'''

for column in output_df_header_list:
    new_row_append_list.append(ouput_df_new_row_place_holder_value)

counter = 0


for index, row in input_df.iterrows():


    '''1000th line counter'''
    if counter % 1000 == 0:
        print("Line = ",counter)

    counter += 1


    '''create new row for output dataframe'''

    new_row = pd.Series(new_row_append_list, index=output_df_header_list)

    '''append blank row to output dataframe'''
    output_df = output_df.append(new_row,ignore_index=True)

    
    '''take input header list and iterate through list'''
    for header in input_header_list:

        '''select individual cell data'''
        cell_data = row[header]


        ''' test code
        if header == 'Vendor Address Line2':
            print(cell_data)
            input()

        '''

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
        clean_cell_data = General_Cleaning(cell_data, data_type, max_length, header)

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

    '''check itemLine1_item for duplicate rows'''

   
    try:
        if output_df.iloc[output_df_index]['itemLine1_item'] == " " or output_df.iloc[output_df_index]['itemLine1_item'] == '999':
        
            '''if item is empty incrase quantity of item in line above'''
            output_df.iloc[output_df_index - 1]['itemLine1_quantity'] = output_df.iloc[output_df_index - 1]['itemLine1_quantity'] + 1
            output_df.drop(output_df.index[output_df_index])
            output_df_index = output_df_index - 1

    except:
        non_variable = True
    
    
    output_df_index += 1


'''flag any empty manditory cells in the output dataframe'''
second_run_index = 0

print("Flagging Empty Rows...")

#final_output_df.to_csv("test.csv")


for index, row in output_df.iterrows():

    for manditory_header in manditory_header_list:
        manditory_cell = row[manditory_header]


        '''Code for filling in empty manditory cells'''

       
        
    
        if manditory_cell == " ":
            
            new_cell_value = mandatory_empty_cell_filler_control(manditory_header, "STANDARD_CELL")
            output_df.iloc[second_run_index][manditory_header] = new_cell_value
            
            
                
        
    second_run_index += 1

print("Assessing Location Information...")

for index, row in output_df.iterrows():

    try:
        customer = row['customer']
        translated_location = location_translation(customer)

        if translated_location != "No Location":
            output_df.iloc[index]['billCountry'] = translated_location

        else:
            continue
            

    except:
        continue

#output_df.to_csv("test.csv")
#input()

'''extra code for removing empty rows with no itemLine1_item data '''

empty_row_list = []

print("Sorting Item Lines....")

for index, row in output_df.iterrows():

    try:
        if row['itemLine_item'] != "FILL":
            empty_row_list.append(index)

    except:
        false_variable = True

    #except:
        #non_variable = True

#print(empty_row_list)
#input()

'''if there are no duplicate lines just use all the rows'''

if len(empty_row_list) < 1:

    for index, row in output_df.iterrows():
        empty_row_list.append(index)

    

print("Performing Drop Out....")

line = 0

for index in empty_row_list:
    output_df.drop(output_df.index[index])

    final_output_df.loc[output_df.index[index]] = output_df.iloc[index]
    if line % 1000 == 0:
        print("Drop_out on line", line)
    line += 1
    '''Other field reference filling'''



    





'''prompt for file to write too'''

out_file_name = input("Enter Output File Name: ")

output_path = "./output_files/"

full_output_path = output_path + out_file_name

print("writing to file")
final_output_df.to_csv(full_output_path)
