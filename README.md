# Nutuoil_Datamigration_Code

The following code is from my 4 months doing datamigration coding in Python for Natu'oil.

The code covers the 3 versions of data migration code written to convert highly messy .csv files into a format that could be read by an Oracle database creation program. 

Version One: uses .csv library and converts data by position can contains large amoounts of file specifc code

Version Two: use pandas library to create a data frame object that can reference data by name (use given that the data is often non-uniform in structure)

Version 3 implements a "data control dictionary" which allows mapping to be controlled on the fly using dictionary entries rather that using specifically encoded logic.

Also included is a web based GUI manual mapping interface to allow fro quick mapping of data. 
