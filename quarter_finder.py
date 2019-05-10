def quarter(date):

    quarter_1 = 3
    quarter_2 = 6
    quarter_3 = 9
    quarter_4 = 12

    month = date[5:7]
    year = date[:4]

    month = int(month)

    if  month <= quarter_1:
        quarter = "1"

    elif month <= quarter_2:
        quarter = "2"

    elif month <= quarter_3:
        quarter = "3"

    elif month <= quarter_4:
        quarter = "4"

    else:
        "Quarter Calculation  Error"

    return quarter + " " + year

        
        
    

    




















