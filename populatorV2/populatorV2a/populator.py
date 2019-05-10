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


#out_file_name = input("Name of output file : " or "map.txt")

#Relaionship map file
map_file = open("VendorMap.txt")

#inititize template
template = []

#loads map file into template
for line in map_file:
    map_file_list = line.split(',')
    template.append(map_file_list)

#creates list of headers
header_list = []
for field in template:
    header_list.append(field[0])

print("Template written")

#populates data dump file with headers
with open("data_dump.csv", "a") as file:
        file.write(str(header_list)+"\n")

print("Headers Written")

#reads in input data file and creates data frame
df = pd.read_csv("VendorList.csv",encoding = "ISO-8859-1")

#imports headers from data frame
headers = df.columns



#iterats through each line of data in import file
for index, row in df.iterrows():
    str1 = ""
    line = []

    #iterates through template header maps import headers referenced by header
    #neme to current position in tmeplate
    for entry in template:
        if entry[2] == ' blank\n':
            line.append('')
        else:
            line.append(row[entry[2]])

    #dumps output to data dump file for further processing
    with open("data_dump.csv", "a", newline='') as file:
        wr = csv.writer(file)
        wr.writerow(line)

print("First Pass Written")
            
#opens data dump file for further cleaning
#exports cleaned data to template
with open("data_dump.csv") as file:

    for line in file:

        line_list = line.split(",")
        position = 0

        for entry in line_list:
            
            if entry == 'nan':
                line_list[position] = ""

            if entry == 'Y':
                line_list[position] = "TRUE"

            if entry == 'N':
                line_list[position] = "FALSE"
                
            position += 1
                

        with open("VendorTemplate.csv", "a", newline='') as file:
            wr = csv.writer(file)
            wr.writerow(line_list)
            #input()

            
#removes data dump file
os.remove("data_dump.csv")        

print("write complete")
   

   
