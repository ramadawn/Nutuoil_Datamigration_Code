import pandas as pd
import glob

file_list = glob.glob("import_files/*.*")

for file in file_list:
    try:
        df = pd.read_csv(file)
    except:
        continue

    print("File = ",file)

    possible_headers = []
    headers = list(df.columns.values)
    for header in headers:
        
        for pos in  range(len(header)):
            
            if header[pos] == "t" or header[pos] == "T":
                
                try:
                    if header[pos+1] == "x" or header[pos+1] == "A":
                        
                        try:
                            if header[pos+2] == "n" or header[pos+2] == "X":
                                
                                possible_headers.append(header)
                                
                        except:
                            continue
                except:
                    continue
        
    
    
    
    for entry in possible_headers:
        try:
            print("Header : ",entry)
            print(df.loc[:,entry])
            input()
        except:
            continue
