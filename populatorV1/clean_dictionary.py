'''File for storing cleaning relations'''

'''relation index'''

'''   --- (entry, entry conversion, action, action result, additional header, additional header position --- ''' 

def cleaning_dictionary():


    cleaning_dict = {

        "all headers":[
                        ('y','TRUE'),
                        ('Y','TRUE'),
                        ('n','FALSE'),
                        ('N','FALSE'),
                        


                      ],

        "Purchase Tax Code":[
                            ('G','G-GST Only'),
                            ('HBC','HST BC Only'),
                            ('HON','HST ON Only'),
                            ('E','Exempt'),
                            ('P','PST Only'),
                            ('S','Standard'),
                            ('SBC','Standard BC (GST/PST)'),
                            ('Z','Zero Rate'),
                            ('QST','Quecbc on Purchase'),

                            ],

        "Sales Tax Code":[
                            ('G','G-GST Only'),
                            ('HBC','HST BC Only'),
                            ('HON','HST ON Only'),
                            ('E','Exempt'),
                            ('P','PST Only'),
                            ('S','Standard'),
                            ('SBC','Standard BC (GST/PST)'),
                            ('Z','Zero Rate'),
                            ('QST','Quecbc on Purchase'),

                            ],

        "Item numbers":[
                            ('','','split',':',0)
                            ],

        "multi_header_split":[
                            ('','','split',' ',0,'last name',1)
                            ],

        "Item":[
                ('','','split',':',0,'externalid',1)
                ],

                            }
        
    return cleaning_dict
