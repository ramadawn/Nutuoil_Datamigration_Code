'''The app uses the map file to draw in multiple files and output
the information in those files according to a common templete'''


import pandas as pd

def Item_template():

    item_template = {
'dummy': 'externalid', 
'Expiry': 'itemLocationLine1_expirationdate', 
'Lot#': 'itemLocationLine1_lotnumbers', 
'In': 'inventory in', 
'Out ': 'inventory out', 
'Remain': 'inventory remaining', 
'Container#': 'container #', 
'CONTAINER#': 'container #', 
'Release#': 'release #', 
'Item Code': 'Item code', 
'SalesTaxCode': 'SalesTaxCode', 
'AccountRefFullName': 'name', 
'ClassRefFullName': 'Class', 
'InventoryAdjustmentLineValueAdjustmentQuantityDifference': 'purchaseorderquantitydiff', 
'InventoryAdjustmentLineQuantityAdjustmentSiteLocRefFullName': 'preferredlocation', 
'CustomerRefFullName': 'vendor1_name', 
'InventorySiteRefFullName': 'itemLocationLine1_location', 
'InventoryAdjustmentLineQuantityAdjustmentLotNumber': 'itemLocationLine1_lotnumbers', 
'externalid': 'custom:Name of the field(Label of the field).1', 
'Item': 'parent', 
'Type': 'unitstype', 
'Description': 'description', 
'Cost': 'cost', 
'Purchase Description': 'purchasedescription', 
'Reorder Pt (Min)': 'reordermultiple', 
'Manu. Part No.': 'mpn', 
'Preferred Vendor': 'vendor1_preferred', 
'Price': 'vendor1_purchaseprice', 
'U/M': 'weight', 
'U/M Set': 'weightunit', 
'COGS Account': 'itemPriceLine3_quantityPricing', 
'Account': 'incomeaccount', 
'Asset Account': 'assetaccount', 
'Amounts Include Tax': 'istaxable', 
'Purchase Tax Code': 'purchasetaxcode', 
'Sales Tax Code': 'sales tax code', 
'Accumulated Depreciation': 'accumulated depriciation', 
'Quantity On Hand': 'quantity on hand', 
'Gross Price': 'gross price', 
'Purchased for Resale': 'purchased for resale', 
'Sales Tax Return Line': 'sales tax return', 
'ListID': 'externalid', 
'Name': 'name', 
'FullName': 'displayname', 
'ParentRefFullName': 'parent', 
'PurchaseCost': 'cost', 
'PurchaseDesc': 'purchasedescription', 
'ReorderPoint': 'autoreorderpoint', 
'ManufacturerPartNumber': 'mpn', 
'QuantityOnOrder': 'purchaseorderquantity', 
'PrefVendorRefFullName': 'vendor1_preferred', 
'SalesDesc': 'salesdescription', 
'UnitOfMeasureSetRefFullName': 'weight', 
'SalesPrice': 'salesprice', 
'COGSAccountRefFullName': 'cogsaccount', 
'IncomeAccountRefFullName': 'incomeaccount', 
'AssetAccountRefFullName': 'assetaccount', 
'IsActive': 'isinactive', 
'SalesTaxCodeRefFullName': 'sales tax code', 
'QuantityOnHand': 'quantity on hand', 
'AverageCost': 'average cost', 
'PaymentMethodRefFullName': 'payment method', 
'TaxRate': 'tax rate', 
'ItemDesc': 'item discount description', 
'DiscountRate': 'Discount rate', 
'DiscountRatePercent': 'Discount rate percent', 
'VendorOrPayeeName': 'vendorname', 
'Location': 'Location', 
'PONumber': 'PO number', 
'AssetNumber': 'asset number', 
'TotalValue': 'totalvalue', 
'UnitOfMeasureSetRefListID': 'weightunit', 
'Maximum': 'maximum', 
'InventoryDate': 'inventory date', 
'Purchase Cost': 'cost', 
'Reorder Point': 'autoreorderpoint', 
'MFG Part No': 'mpn', 
'Sales Description': 'salesdescription', 
'Expense/COGS Account': 'cogsaccount', 
'Account/Income Account': 'incomeaccount', 
'Is Act;ive': 'isinactive', 
'Qty on Hand': 'quantity on hand', 
'Qty on Order': 'quantity on order', 
'Unit of Measure': 'UMO', 
'Price Each': 'price each',
'DATE' : 'Date',
"B.O.L #/ RELASE#" : "B.O.L #/ RELASE#",
'SHIP TO/ FROM' : 'SHIP TO/ FROM', 
'Status' : 'Status',
'LOC.' : 'LOC.',
'LOT #' : 'LOT #',
'Expiry' : 'Expiry',
'UOM/ Notes' : 'UOM/ Notes',

}
    return item_template


def multi_file_pop():

    map_dictionary = {}


    template_file_name ='Inventory_Item_Template.csv'

    header_df = pd.read_csv(template_file_name,encoding = "ISO-8859-1")
    header_list = header_df.columns
    

    #load outputnfile
    '''*****MAP FILE NAME****'''
    with open('itemMapSecondClean.txt') as file:

        for line in file:
            #convert data_mao into string into list
            raw_data_map_list = line.split(",")

    '''template headers are every header nth space in list'''

    template_header_distance = 4
    first_template_header_postion = 1

    #header_list = []
    stop_adding = False
    data_map_list = []
    dataMapList_position = 0

    data_map_dictionary = {}
    
    

    for entry in raw_data_map_list:
        current_map_unit = []
        if entry == 'FILENAME' or entry == 'EMPTY':

            '''populate header list'''
            #if dataMapList_position > 0:

                #if entry == 'FILENAME':
                    #stop_adding = True
                    
                #if stop_adding == False:
                    #header_list.append(raw_data_map_list[dataMapList_position + 1])

            #else:
                #header_list.append(raw_data_map_list[dataMapList_position + 1])
            
            
            '''creating list of used Fields'''
            if raw_data_map_list[dataMapList_position + 3] == 'EMPTY':
                dataMapList_position += 1
                continue
            else:
               current_map_unit.append(raw_data_map_list[dataMapList_position + 1])
               current_map_unit.append(raw_data_map_list[dataMapList_position + 2])
               current_map_unit.append(raw_data_map_list[dataMapList_position + 3])
               current_map_unit.append(raw_data_map_list[dataMapList_position + 4])
               dataMapList_position += 1
               data_map_list.append(current_map_unit)
               continue

        else:
           dataMapList_position += 1
           continue        
    




    list_size = 0


    '''turning used input list into dictionary'''
    for entry in data_map_list:
        
        key = []
        key.append(entry[2])
        key.append(entry[3])
        key_str = str(key)
        
        if key_str not in data_map_dictionary:
    
            data_map_dictionary[entry[2]] = entry[0] #, entry[1])
            
            
    '''************Fix HACK FOR DICTIONARY**************'''
    data_map_dictionary = Item_template()
    

    '''removing unused headers from header list'''
    used_headers = []
    for key in data_map_dictionary:
        used_headers.append(data_map_dictionary[key])

    
    new_header_list = []
    for header in  header_list:
        new_header_list.append(header)

    print("Raw Header List = ",len(new_header_list))
    print("Used Header List = ",len(used_headers))
    
    for header in new_header_list:
        if header not in used_headers:
            new_header_list.remove(header)

    print("Header List After Removal = ",len(new_header_list))

    for header in used_headers:
        if header not in new_header_list:
            new_header_list.append(header)

    print("Header List After Appending = ",len(new_header_list))

    
    return data_map_dictionary, new_header_list




