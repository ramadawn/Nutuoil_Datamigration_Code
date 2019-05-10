"""
Douglas Oak September 25th 2018

This script Opens up the relationship map file
It then creates a template relating imported headers and output headers
It then loads up the import data file
it first maps the import data to the output CSV headings
It then dumps the data into a data dump file
the then loads the data dump file for additional cleaning
it then  outputs the indicatated template
"""
import pandas as pd
import csv
import os
from multi_file_template_builder import multi_file_pop
import glob


out_file_name = input("Name of output file : " or "output.csv")

#Makes a list of all names
file_list = glob.glob("import_files\*.csv")

#imports relationship dictionary
template_dictionary = multi_file_pop()

header_list = []

for key in template_dictionary:
    header_list.append(key)

print("Template written")


#populates data dump file with headers
with open("data_dump.csv", "a") as file:
        file.write(str(header_list)+"\n")

print("Headers Written")

template_length = 0
for key in template_dictionary:
    if int(template_dictionary[key][1]) > template_length:
        template_length = int(template_dictionary[key][1])
        
    


for file in file_list:

    #reads in input data file and creates data frame
    try:
        df = pd.read_csv(file,encoding = "ISO-8859-1")

    except:
        print("Exception")
        print("File = ",file)
        continue
        

    #imports headers from data frame
    headers = df.columns
    output_list = []

    for position in range(template_length + 1):
        output_list.append("")

    
    #iterats through each line of data in import file
   
    for index, row in df.iterrows():
        str1 = ""
        line = []

        for header in headers:
           
            if header in template_dictionary:
                output_list[int(template_dictionary[header][1])] = row[header]
    
                
        #dumps output to data dump file for further processing
        with open("data_dump.csv", "a", newline='') as file:
            file.write(str(output_list)+"\n")

print("First Pass Written")
            
#creates dataframe out of dump file
dumpdf = pd.read_csv("data_dump.csv",encoding = "ISO-8859-1")

dump_file_headers = df.columns


#iterates through data frame to clean data 
for index, row in dumpdf.iterrows():
    iterator = 0
    
    while iterator < len(row):
        
       
        if dumpdf.iloc[index,iterator] == 'Y':
            dumpdf.iloc[index,iterator] = 'TRUE'

        if dumpdf.iloc[index,iterator] == 'N':
            dumpdf.iloc[index,iterator] = 'FALSE'

        iterator += 1

dumpdf.to_csv("EmployeeTemplate.csv")           
                
            
#removes data dump file
os.remove("data_dump.csv")        

print("write complete")
   

   
