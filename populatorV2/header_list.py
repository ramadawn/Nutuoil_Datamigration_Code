import glob

file_list = glob.glob("output_files/*.*")


full_line_list = []


for file in file_list:
    
    with open(file, 'r') as lines:
        for line in lines:
            line_list = line.split(',')
            full_line_list.extend(line_list)


out_list = []

for position in range(len(full_line_list)):

    try:
        test = (int(full_line_list[position]))
        possible_entry = full_line_list[position + 1]
        if possible_entry == '':
            continue
        else:
            out_list.append(possible_entry)
            

    except:
        continue
    

    
for entry in out_list:
    for pos in  range(len(entry)):
        if entry[pos] == "t" or entry[pos] == "T":
            try:
                if entry[pos+1] == "a" or entry[pos+1] == "A":
                    print(entry)
            except:
                continue
