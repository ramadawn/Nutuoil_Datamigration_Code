

from item_cleaning_module import entry_clean
from clean_dictionary import cleaning_dictionary


                            
test_dict = cleaning_dictionary()


data = 'John Doe'
header = "multi_header_split"
#header = "Purchase Tax Code"
#print(entry_clean(test_string,header,test_dict))


'''creates header map dictionary'''


clean_dictionary = cleaning_dictionary()

data = entry_clean(data,header,clean_dictionary)

if type(data) != str:
    two_variables = True
    new_header = data[1]
    last = data[2]
    data = data[0]

print(data)
print(last)
print(new_header)
