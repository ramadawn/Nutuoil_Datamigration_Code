'''Version 2 Populator
Douglas Oak October 12 2018'''


from multi_file_template_builder import multi_file_pop
from item_cleaning_module import entry_clean
from clean_dictionary import cleaning_dictionary
import glob
import pandas as pd

'''creates header map dictionary'''
map_dictionary, out_df_columns = multi_file_pop()

clean_dictionary = cleaning_dictionary()

"out to output dataframe new headers from cleaning dictionary"
work_list = []

for column in out_df_columns:
    work_list.append(column)

incrementor = 0
for column in out_df_columns:
    poss_add_column = entry_clean("QUERY", column, test_dict)
    if poss_add_column != "No Match":
        segment = poss_add_column[0]
        work_list.insert(incrementor + 1, segment[5])
    incrementor += 1

'''prompts user for output file'''
out_file_name = input("Name of output file : " or "output.csv")

'''Makes a list of all names'''
file_list = glob.glob("import_files\*.csv")

data_mapped = 0


'''creating output dataframe'''

output_df = pd.DataFrame(columns=out_df_columns)


output_dataframe_index = 0

for file in file_list:

    print("Reading file ",file,".......")
    try:
        '''creates data frame from each input file file'''
        input_file_df = pd.read_csv(file,encoding = "ISO-8859-1")

    except:
        print(file," ---Exception File Not Read---")
        continue

    
    
    '''list of input headers from each input file'''
    input_file_headers = input_file_df.columns

    for index, row in input_file_df.iterrows():
        
        '''create a new zero row in the output dataframe'''
        

        place_holder_value = ''

        append_list = []

        for column in out_df_columns:
            append_list.append(place_holder_value)
          
        new_row = pd.Series(append_list, index=out_df_columns)

        '''Appends blanck row to bottom of data frame'''

        output_df = output_df.append(new_row,ignore_index=True)
        

        header_name_position = 0

        for header in input_file_headers:

            two_variables = False
            new_header = 'NEW HEADER ERROR'
            second_string = 'SECOND STRING ASSIGNMENRT ERROR'
            
            '''getting data from incomming input data frame row for input header'''
            '''DATA INSERTED HERE'''
            data = row[header]

            '''Send Data to cleaning module'''
            data = entry_clean(data,header,clean_dictionary)

            if type(data) != str:
                two_variables = True
                new_header = data[1]
                second_string = data[2]
                data = data[0]
                
            

            '''generating key from input_data_frame for mapping dictionary'''
            key_list = []
            key_list.append(header)
            key_list.append(str(header_name_position))
            header_name_position += 1
            key = str(key_list)
            
            '''map dictionary using generated key'''
            if key in map_dictionary:
                output_header = map_dictionary[key][0]
                output_df.iloc[output_dataframe_index][new_header] = data

                if two_variables == True:
                    output_df.iloc[output_dataframe_index][output_header] = second_string
                
                data_mapped += 1

        

        output_dataframe_index += 1
        if output_dataframe_index % 1000 == 0:
            print(output_dataframe_index," Lines Processed Accessing ", file)
            print("Individual Items mapped = ",data_mapped)

print("Writing To File")
output_df.to_csv(out_file_name)

        
