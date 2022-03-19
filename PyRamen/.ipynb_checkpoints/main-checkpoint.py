# Importing functions 
from pathlib import Path
import csv

# define functions

def printFinancialSummaryFile():
    reportout = Path('.\Output/sales_report.txt') 
    tempvar=""
    for key in report.keys():
        tempvar=tempvar + str(key) +": " + str(report[key]) + "\n"
    with open (reportout , 'w') as dataout:
        dataout.write(tempvar)
    return
    
# global variables
menuFile = Path('.\Resources/menu_data.csv')
salesFile = Path('.\Resources/sales_data.csv')
menu = []
sales = []
report = {}


# Load menuData into reader and process
with open (menuFile , 'r') as menuData:
    csvRead = csv.reader(menuData, delimiter = ',')
    # skip header record 
    next(menuData)
    menu=list(csvRead)
    
        
# Load salesData into reader and process
with open (salesFile , 'r') as salesData:
    csvRead = csv.reader(salesData, delimiter = ',')
    # skip header record 
    next(salesData)
    sales = list(csvRead)
    #for  salesRow in salesData:
    #    salesRowStripped=salesRow.rstrip()
    #    each=[]
    #    each=salesRowStripped.split(',')
    #    sales.append(each)

# Iterate through Sales Item and create report record in dictionary
for sale_item in sales:
    menu_item=sale_item[-1]
    quantity=sale_item[-2]

    if menu_item not in report:
        report[menu_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0,}
    else:
        pass
        #print (f"{menu_item} already exist in report!")
    
    #Iterate through all menu items amd if match current sale_item accumulate dictionary value items
    for menu_master_item in menu:

        item=menu_master_item[0]
        price=menu_master_item[-2]
        cost=menu_master_item[-1]
        # Start building report data
        if menu_item == item:
            report[item]["01-count"] += int(quantity)
            report[item]["02-revenue"] += float(price) * int(quantity)
            report[item]["03-cogs"] += float(cost) * int(quantity)
            report[item]["04-profit"] += (float(price)-float(cost)) * int(quantity)
        else:
            #pass
            print (f"{item} does not equal {menu_item} NO MATCH!")

#Call Function to print report to file            
printFinancialSummaryFile()
# Output Done Processing to screen
print ("Done Processing ...")