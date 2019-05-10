reg = 38

dynamic = {

    

    '''Our Header : Their Header, cleaning rules'''

                '''OpenARInvoiceNetSuiteHeaders'''
                '''location is in seperate file'''
                '''accounting periods seperate file'''

'''
Input header  Output header                 Output Type, Is Mandatory, Max Char Length,      Split
'''
      TxnId      : ['externalid'                      ,          ,True        ,reg               ,False],
      RefNumber      : ['tranid'                          ,str       ,True        ,15                ,False], 
      Customer      : ['customer'                        ,list      ,True        ,reg               ,False], #Parent CustomerID : Child CustomerID
            : ['opportunity'                     ,list      ,False       ,reg               ,False], #noman List
            : ['job'                             ,list      ,False       ,reg               ,False],
      TxnDate      : ['trandate'                        ,str       ,True        ,reg               ,False], #man string
      Inventory Site      : ['location'                        ,list      ,True        ,reg               ,False], #man list         
            : ['otherrefnum'                     ,str       ,False       ,reg               ,False], #noman string
      Terms      : ['terms'                           ,list      ,False       ,reg               ,False],
      Due Date      : ['duedate'                         ,str       ,False       ,reg               ,False], #noman string
      ?      : ['postingperiod'                   ,str       ,True        ,reg               ,False], #man string
      Sales Rep      : ['salesrep'                        ,list      ,False       ,reg               ,False], #noman List
      Memo      : ['memo'                            ,str       ,False       ,999               ,False], #noman string
            : ['discountitem'                    ,list      ,False       ,reg               ,False],
            : ['discountrate'                    ,float     ,False       ,reg               ,False], '''dollar or percent format'''
      Currency      : ['currency'                        ,list      ,True        ,reg               ,False], #man list
      Exchange Rate      : ['exchangerate'                    ,float     ,True        ,reg               ,False], #man float
      TxnLine Item      : ['item'                            ,list      ,True        ,reg               ,False], #man list
      TxnLine Quantity      : ['quantity'                        ,list      ,True        ,reg               ,False], #man list
            : ['units'                           ,list      ,False       ,reg               ,False], #noman List
      Price Each      : ['pricelevel'                      ,list      ,True        ,reg               ,False], #man list
      TxnLine Amount      : ['amount'                          ,float     ,True        ,reg               ,False], #man float
            : ['istaxable'                       ,bool      ,True        ,reg               ,False], #man boolian look at TxnLine SalesTaxCode if empty = False else true
            : ['itemLine_class'                  ,list      ,False       ,reg               ,False],

            '''added flields'''
      ARAccount : ['ARAccount'                  ,int        ,False
      BalanceRemaining : [''                    ,float
      Ship Date : [''                           ,str

            '''OpenCreditMemoNetSuiteHeaders'''

     TxnId       : ['externalid'                      ,          ,True        ,reg               ,False], 
     RefNumber       : ['tranid'                          ,str       ,True        ,45                ,False], #man string
     Customer       : ['customer'                        ,list      ,True        ,reg               ,False], #man list
            : ['job'                             ,list      ,False       ,reg               ,False], #noman List
     TxnDate        : ['trandate'                        ,str       ,True        ,reg               ,False], #man string
     ?       : ['postingperiod'                   ,list      ,True        ,reg               ,False], #man list
            : ['otherrefnum'                     ,str       ,False       ,45                ,False], #noman string
            : ['memo'                            ,str       ,False       ,999               ,False], #noman string
            : ['partner'                         ,list      ,False       ,reg               ,False], #noman List
      Sales Rep      : ['salesrep'                        ,str       ,False       ,reg               ,False], #noman string
            : ['saleseffectivedate'              ,str       ,False       ,reg               ,False], #noman string
            : ['leadsource'                      ,list      ,False       ,reg               ,False], #noman List
            : ['department'                      ,list      ,False       ,reg               ,False], #noman List
            : ['class'                           ,list      ,False       ,reg               ,False], #noman List
     Inventory Site       : ['location'                        ,list      ,True        ,reg               ,False], #man list
            : ['discount-discountItem'           ,list      ,False       ,reg               ,False], #noman List
            : ['discount-discountRate'           ,float     ,False       ,reg               ,False], #noman float
                                        '''custom field here'''         
                                        '''custom field here'''
     TxnLine Item      : ['itemLine1_item'                  ,list      ,True        ,reg               ,False], #man list
     TxnLine Quantity       : ['itemLine1_quantity'              ,int       ,True        ,reg               ,False], #man integer
            : ['itemLine1_units'                 ,list      ,False       ,reg               ,False], #noman List
            : ['itemLine1_salesPrice'            ,float     ,False       ,reg               ,False], #noman float
     TxnLine Amount  : ['itemLine1_amount'                ,float     ,False       ,reg               ,False], #noman float
            : ['itemLine1_description'           ,str       ,False       ,999               ,False], #noman string
            : ['itemLine1_isTaxable'             ,bool      ,False       ,reg               ,False], #noman boolian
            : ['itemLine1_priceLevel'            ,list      ,False       ,reg               ,False], #noman List
            : ['itemLine1_costestimatetype'      ,list      ,False       ,reg               ,False], #noman List
            : ['itemLine1_invdetail_bin'         ,list      ,False       ,reg               ,False], #noman List
            : ['itemLine1_invdetail_quantity'    ,float     ,False       ,reg               ,False], #noman float
            : ['shipcarrier'                     ,list      ,False       ,reg               ,False], #noman List
            : ['billAttention'                   ,str       ,False       ,83                ,False], #noman string 
            : ['billAddressee'                   ,str       ,False       ,83                ,False], #noman string
            : ['billAddr1'                       ,str       ,False       ,150               ,False], #noman string
            : ['billAddr2'                       ,str       ,False       ,150               ,False], #noman string
            : ['billCity'                        ,str       ,False       ,50                ,False], #noman string
            : ['billState'                       ,str       ,False       ,reg               ,False], #noman string
            : ['billZip'                         ,str       ,False       ,50                ,False], #noman string
     Bill To Country       : ['billCountry'                     ,list      ,True        ,reg               ,False], #man list   ****No full***
            : ['billPhone'                       ,str       ,False       ,21                ,False], #noman string
           Currency : ['currency'                        ,list      ,True        ,reg               ,False], #man list *** use curency *** 
           Exchange Rate : ['exchangerate'                    ,float     ,True        ,reg               ,False], #man float  
            : ['istaxable'                       ,bool      ,False       ,reg               ,False], #noman boolian
            : ['taxitem'                         ,list      ,False       ,reg               ,False], #noman list
            : ['taxrate'                         ,float     ,False       ,reg               ,False], #noman float
            : ['tobeprinted'                     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['tobeemailed'                     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['email'                           ,str       ,False       ,64                ,False], #noman string
            : ['tobefaxed'                       ,bool      ,False       ,reg               ,False], #noman boolian
            : ['fax'                             ,str       ,True        ,21                ,False], #man string
            : ['customerMessage'                 ,str       ,False       ,reg               ,False], #noman string

            '''Added Headers'''
            ARAccount : ['ARAccount'                  ,int        ,False


            '''Open purchase Orders'''

    'TxnId' : ['externalid'                      ,          ,True        ,reg               ,False],
            : ['otherrefnum'                     ,str       ,False       ,reg               ,False], #noman string
   'Vendor' : ['vendor'                          ,list      ,True        ,reg               ,False], #man list
            : ['purchasecontract'                ,list      ,True        ,reg               ,False], #man list
            : ['Employee'                        ,list      ,False       ,reg               ,False], #noman list
            : ['supervisorapproval'              ,bool      ,False       ,reg               ,False], #noman boolian
            : ['duedate'                         ,str       ,False       ,reg               ,False], #noman string
  'TxnDate' : ['trandate'                        ,str       ,True        ,21                ,False], #man string
'RefNumber' : ['tranId'                          ,str       ,True        ,reg               ,False], #man string
            : ['memo'                            ,str       ,False       ,reg               ,False], #noman string
            : ['department'                      ,list      ,False       ,reg               ,False], #noman list
            : ['class'                           ,list      ,False       ,reg               ,False], #noman list
      'special country'      : ['location'                        ,list      ,False       ,reg               ,False], #noman list
            : ['custbody_nsts_gaw_tran_requestor' ,list    ,False       ,reg               ,False],  #noman list
            : ['exchangeRate'                    ,float     ,False       ,reg               ,False], #noman float
      TxnLine Item      : ['purchaseItemLine_item'           ,list      ,True        ,reg               ,False], #man list  Parent Item Name : Child Item Name
      TxnLine Quantity      : ['purchaseItemLine_quantity'       ,int       ,True        ,reg               ,False], #man integer
            : ['purchaseItemLine_serialNumbers'  ,str       ,False       ,reg               ,False], #noman string
            : ['purchaseItemLine_units'          ,list      ,False       ,reg               ,False], #noman list
     Price Each       : ['purchaseItemLine_rate'           ,float     ,True        ,reg               ,False], #man float
            : ['purchaseItemLine_amount'         ,float     ,False       ,reg               ,False], #noman float
            : ['purchaseItemLine_description'    ,str       ,False       ,reg               ,False], #noman string
            : ['purchaseItemLine_amount'         ,list      ,False       ,reg               ,False], #noman list
            : ['purchaseItemLine_class'          ,list      ,False       ,reg               ,False], #noman list
            : ['purchaseItemLine_location'       ,list      ,False       ,reg               ,False], #noman list
            : ['Customer [column in Items Tab]'  ,list      ,False       ,reg               ,False], #noman list
            : ['purchaseItemLine_isBillable'     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['purchaseItemLine_isClosed'       ,bool      ,False       ,reg               ,False], #noman boolian
            : ['itemLine_custom:Field Name'      ,str       ,False       ,reg               ,False], #noman string
            : ['itemLine_custom:Field Name'      ,str       ,False       ,reg               ,False], #noman string
    'Terms' : ['terms'                           ,list      ,False       ,reg               ,False], #noman list
            : ['billaddresslist'                 ,str       ,False       ,reg               ,False], #noman string
            : ['billAttention'                   ,str       ,False       ,reg               ,False], #noman string
            : ['billAddressee'                   ,str       ,False       ,reg               ,False], #noman string
            : ['billAddr1'                       ,str       ,False       ,reg               ,False], #noman string
            : ['billAddr2'                       ,str       ,False       ,reg               ,False], #noman string
            : ['billCity'                        ,str       ,False       ,reg               ,False], #noman string
            : ['billState'                       ,str       ,False       ,reg               ,False], #noman string
            : ['billZip'                         ,str       ,False       ,reg               ,False], #noman string
            : ['billCountry'                     ,str       ,False       ,reg               ,False], #noman string
            : ['billPhone'                       ,str       ,False       ,reg               ,False], #noman string
            : ['toBePrinted'                     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['toBeEmailed'                     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['email'                           ,str       ,False       ,reg               ,False], #noman string
            : ['toBeFaxed'                       ,bool      ,False       ,reg               ,False], #noman boolian
            : ['fax'                             ,str       ,False       ,reg               ,False], #noman string
            : ['vendorMessage'                   ,str       ,False       ,reg               ,False], #noman string

                '''custom'''
    Unit of Measure : ['Unit of Measure'

            '''Open Sales Order Template'''

     'TxnId'       : ['externalid'                      ,          ,True        ,reg               ,False], 
     'RefNumber'   : ['tranId'                          ,str       ,True        ,45                ,False], #man string
     'Customer'    : ['Customer'                        ,list      ,True        ,reg               ,False], #man list Parent Customers ID : Child Customer ID
     'TxnDate'     : ['trandate'                        ,str       ,True        ,reg               ,False],
     ****       : ['orderstatus'                     ,list      ,True        ,reg               ,False], #man list  #say everything is approved
            : ['startdate'                       ,str       ,False       ,reg               ,False], #noman string
            : ['enddate'                         ,str       ,False       ,reg               ,False],
            : ['otherrefnum'                     ,int       ,False       ,reg               ,False],
            : ['memo'                            ,str       ,False       ,999               ,False],
            : ['salesrep'                        ,list      ,False       ,reg               ,False], #noman list
            : ['opportunity'                     ,list      ,False       ,reg               ,False],
            : ['saleseffectivedate'              ,str       ,False       ,reg               ,False],
            : ['leadsource'                      ,list      ,False       ,reg               ,False],
            : ['partner'                         ,list      ,False       ,reg               ,False],
            : ['Department'                      ,list      ,False       ,reg               ,False],
            : ['Class'                           ,list      ,False       ,reg               ,False],
            : ['Location'                        ,list      ,False       ,reg               ,False],
            : ['couponcode'                      ,str       ,False       ,reg               ,False],
            : ['promocode'                       ,list      ,False       ,reg               ,False],
            : ['discount-discountItem'           ,list      ,False       ,reg               ,False],
            : ['discount-discountrate'           ,float     ,False       ,reg               ,False],
         TxnLine Item   : ['itemLine_item'                   ,list      ,True        ,reg               ,False],
         TxnLine Quantity   : ['itemLine_quantity'               ,int       ,True        ,reg               ,False], #man integer
            : ['itemLine_serialNumbers'          ,str       ,False       ,reg               ,False], #noman string
            : ['itemLine_units'                  ,list      ,False       ,reg               ,False],
         TxnLine Cost   : ['itemLine_salesPrice'             ,float     ,True        ,reg               ,False], #man float
         TxnLine Amount   : ['itemLine_amount'                 ,float     ,False       ,reg               ,False], #noman float
            : ['itemLine_description'            ,str       ,False       ,999               ,False], #noman sring
            : ['itemLine_isTaxable'              ,bool      ,False       ,reg               ,False], #noman boolian
            : ['itemLine_priceLevel'             ,list      ,False       ,reg               ,False], #noman list
            : ['itemLine_department'             ,list      ,False       ,reg               ,False], #noman list
            : ['itemLine_class'                  ,list      ,False       ,reg               ,False], #noman list
            : ['itemLine_location'               ,list      ,False       ,reg               ,False], #noman list

                                         '''item line custom field'''
                                         '''item line custom field'''
                                         '''item line custom field'''

          Ship Date  : ['shipdate'                        ,str       ,False       ,reg               ,False], #noman sring
            : ['shipcarrier'                     ,list      ,False       ,reg               ,False], #noman list
            : ['shipmethod'                      ,list      ,False       ,reg               ,False], #noman list
          Due Date  : ['shipcomplete'                    ,bool      ,False       ,reg               ,False], #noman boolian
            : ['shipaddresslist'                 ,float     ,False       ,reg               ,False], #noman float
            : ['shipattention'                   ,str       ,False       ,100               ,False], #noman sring
          Ship To Line1  : ['shipaddressee'                   ,str       ,False       ,100               ,False], #noman sring
            : ['shipAddr1'                       ,str       ,False       ,150               ,False], #noman sring
            : ['shipAddr2'                       ,str       ,False       ,150               ,False], #noman sring
            : ['shipCity'                        ,str       ,False       ,reg               ,False], #noman sring
            : ['shipState'                       ,list      ,False       ,reg               ,False], #noman sring
            : ['shipZip'                         ,str       ,False       ,reg               ,False], #noman sring
            : ['shipCountry'                     ,list      ,False       ,reg               ,False], #noman sring
            : ['shipPhone'                       ,str       ,False       ,50                ,False], #noman sring
         Terms   : ['terms'                           ,list      ,False       ,reg               ,False], #noman list
            : ['billattention'                   ,str       ,False       ,100               ,False],
         Bill To Line1   : ['billAddressee'                   ,str       ,False       ,100               ,False],
         Bill To Line2   : ['billAddr1'                       ,str       ,False       ,150               ,False],
            : ['billAddr2'                       ,str       ,False       ,150               ,False],
         Bill To City   : ['billCity'                        ,str       ,False       ,reg               ,False],
         Bill To State   : ['billState'                       ,list      ,False       ,reg               ,False],
         Bill To Postal Code  : ['billZip'                         ,str       ,False       ,reg               ,False],
            : ['billCountry'                     ,list      ,False       ,reg               ,False], #noman sring
            : ['billPhone'                       ,str       ,False       ,50                ,False],
            : ['currency'                        ,list      ,False       ,reg               ,False], #noman list
            : ['exchangerate'                    ,float     ,False       ,reg               ,False], #noman float
            : ['istaxable'                       ,bool      ,False       ,reg               ,False], #noman boolian
            : ['taxitem'                         ,list      ,False       ,reg               ,False], #noman list
            : ['taxrate'                         ,float     ,False       ,reg               ,False], #noman float #percentage
            : ['tobeprinted'                     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['tobeemailed'                     ,bool      ,False       ,reg               ,False], #noman boolian
            : ['email'                           ,str       ,False       ,64                ,False],
            : ['tobefaxed'                       ,bool      ,False       ,reg               ,False], #noman boolian
            : ['fax'                             ,str       ,False       ,21                ,False],
            : ['customermessage'                 ,list      ,False       ,reg               ,False],
            : ['custbody_nsts_ci_exclude'        ,bool      ,False       ,reg               ,False],

        Txn Qty Invoiced : ['Qty Invoiced'
            
            
            '''Open Vendor Credit Expense Line'''

        'TxnId'    : ['externalid'                      ,          ,True        ,reg               ,False],
         'RefNumber'    : ['tranId'                          ,str       ,True        ,45                ,False], #man string
         'Vendor'   : ['vendor'                          ,list      ,True        ,reg               ,False], #man list
        'TxnDate'   : ['currency'                        ,list      ,False       ,reg               ,False], #noman list
            : ['echangerate'                     ,float     ,False       ,21                ,False], #noman float
            : ['trandate'                        ,str       ,True        ,reg               ,False], #man string
         '''Create Spread Sheet'''   : ['postingperiod'                   ,list      ,True        ,reg               ,False], #man list
            : ['memo'                            ,str       ,False       ,999               ,False], #noman string
            : ['custbody_nsts_gaw_tran_requestor' ,str      ,False       ,reg               ,False], #noman string

                              '''custom field name'''

            : ['autoapply'                      ,bool       ,False       ,reg               ,False], #noman boolian
          TxnExpLine Account  : ['purchaseExpenseLine_accountRef' ,list       ,True        ,reg               ,False], #man list
          TxnExpLine Amount  : ['purchaseExpenseLine_amount'     ,float      ,True        ,reg               ,False], #man float
            : ['purchaseExpenseLine_memo'       ,str        ,False       ,4000              ,False], #noman string
            : ['purchaseExpenseLine_department' ,list       ,False       ,reg               ,False], #noman list
            : ['purchaseExpenseLine_class'      ,list       ,False       ,reg               ,False], #noman list
            : ['purchaseExpenseLine_isBillable' ,bool       ,False       ,reg               ,False], #noman boolian
            : ['purchaseExpenseLine_taxCode'    ,list       ,False       ,reg               ,False], #noman list
            : ['purchaseExpenseLine_taxCodeAmount' ,float     ,False       ,21                ,False], #noman float

                            '''purchaseItemLine custom field'''

           ***lookup*** : ['applyLine1_tranId'             ,list        ,True       ,reg                ,False], #noman list
           ***loopup*** : ['applyLine1_Line'               ,list        ,True       ,reg                ,False], #noman list
            : ['applyLine1_paymentAmount'      ,float       ,True       ,reg                ,False], #will loopup

            '''Open Vendor Return Authorization Template'''

            
            : ['externalid'                      ,          ,True        ,reg               ,False],
            : ['tranId'                          ,str       ,True        ,45                ,False], #man string        
            : ['status'                          ,str       ,True        ,reg               ,False], #man list must be / Pending, Approval/Pending/Retur
            : ['trandate'                        ,str       ,True        ,reg               ,False],
            : ['Currency'                        ,list      ,True        ,reg               ,False],
            : ['exchangerate'                    ,float     ,True        ,reg               ,False],
            : ['memo'                            ,str       ,False       ,999               ,False],
            : ['subsidiary'                      ,list      ,True        ,reg               ,False],
            : ['Department'                      ,list      ,False       ,reg               ,False],
            : ['Class'                           ,list      ,False       ,reg               ,False],
            : ['Location'                        ,list      ,False       ,reg               ,False],

                            '''three custom fields'''

            : ['itemLine_item'                  ,list       ,True        ,reg               ,False],
            : ['itemLine_quantity'              ,int        ,True        ,reg               ,False],
            : ['itemLine_units'                 ,list       ,False       ,reg               ,False],
            : ['itemLine_salesPrice'            ,float      ,True        ,reg               ,False],
            : ['itemLine_amount'                ,float      ,False       ,reg               ,False],
            : ['itemLine_description'           ,str        ,False       ,999               ,False],
            : ['itemLine_departmentRef'         ,list       ,False       ,reg               ,False],
            : ['itemLine_class'                 ,list       ,False       ,reg               ,False],
            : ['itemLine_location'              ,list       ,True        ,reg               ,False],
            : ['itemLine_AmortSched'            ,list       ,False       ,reg               ,False],
            : ['itemLine_AmortStart'            ,str        ,False       ,reg               ,False],
            : ['itemLine_DropShip'              ,bool       ,False       ,reg               ,False],
            : ['itemLine1_invdetail_bin'        ,list       ,False       ,reg               ,False],
            : ['itemLine1_invdetail_quantity'   ,float      ,False       ,reg               ,False],

                        '''custom Item Line'''

            : ['expenseLine_account'            ,list       ,True        ,reg               ,False],
            : ['expenseLine_amount'             ,float      ,True        ,reg               ,False],
            : ['expenseLine_memo'               ,float      ,False       ,999               ,False],
            : ['expenseLine_departmentRef'      ,list       ,False       ,reg               ,False],
            : ['expenseLine_classRef'           ,list       ,False       ,reg               ,False],
            : ['expenseLine_location'           ,list       ,False       ,reg               ,False],
            : ['expenseLine_AmortSched'         ,list       ,False       ,reg               ,False],
            : ['expenseLine_AmortStart'         ,str        ,False       ,reg               ,False],
            : ['expenseLine_AmortEnd'           ,str        ,False       ,reg               ,False],

                         '''custom expense line fields'''
            }




















































            
