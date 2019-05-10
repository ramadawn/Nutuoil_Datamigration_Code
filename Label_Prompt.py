'''This File Prompts the user to identify which
template they are using and returns the coresponding label'''

def templateID_prompt():

    print("Press 1 to fill Open AR Invoice Template")
    print(" 2 for Open Credit Memo")
    print(" 3 for Open Purchase Orders")
    print(" 4 for Open Sales Orders")
    print(" 5 for Open Vendor Credit Expense Line")

    choice = int(input())

    if choice == 1:
        return 'OpenARInvoice'

    elif choice == 2:
        return 'OpenCreditMemo'

    elif choice == 3:
        return 'OpenPurchaseOrders'

    elif choice == 4:
        return 'OpenSalesOrder'

    elif choice == 5:
        return 'OpenVendorCreditExpenseLine' 

    else:
        print("Label Prompt Error")
