
'''File for processing SpecialActions'''




def posting_period(date):

    month = date[5:7]
    year = date[:4]

    month = int(month)

    switcher = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    month_string = switcher[month]

    return month_string + " " + year

def is_taxable(tax_code):

    if tax_code == 'E':
        return 'FALSE'

    elif tax_code == 'Z':
        return 'FALSE'

    else:
        return 'TRUE'

def currency(money_type):

   
    if money_type != "" :
        return money_type

    else:
        return 'US Dollar'

        
        
def Special_Actions(data, Action):

    if Action == 'QUARTER':

        return posting_period(data)

    
    if Action == 'TAXCODE':

        return is_taxable(data)

    if Action == 'CURRENCY':

        return currency(data)
    




















