import csv, sys, os, re
# Excel xlsx processing
import openpyxl

# proc_prodlist.py --bowfile <file>.xlsx > 9_13.csv

######################################
# This will create the initial csv file to feed into the analyzer
######################################
def processExcelForBow(sheet):
    print "Base Price,UPC Code"
    for row in range(2, sheet.max_row + 1):
        # Base price could be different
        #price = sheet['D'+str (row)].value
        price = sheet['E' + str(row)].value
        if price is None:
            continue
        #upc = sheet['F'+str(row)].value
        #upc = sheet['G' + str(row)].value
        # Error correction like above
        upc = str(sheet['G' + str(row)].value)
        if upc == "None" or upc == "- None -" or "'" in upc:
            continue
        # Some upc's come in format: 26608001249.0, strip any decimals
        if "." in upc:
            print "Found: ", upc
            upc = upc.split(".")[0]
        upc_fixed = "%012d" % int(upc)
        print "%s,%s" % (price,upc_fixed)

bow_file = "none"
sheet_name = "Inventory"
length = len(sys.argv)
if length < 2:
    print "options: --bowfile <xlsx>"
    sys.exit(11)
else:
    for v in range(1, length):
        # Export for Bow's tool (price,upc)
        if sys.argv[v] == "--bowfile":
            bow_file = sys.argv[v+1]

if bow_file != "none":
    if not os.path.exists(bow_file):
        print "File %s does not exist." % bow_file
        sys.exit(11)
    wb = openpyxl.load_workbook(bow_file)
    bow_sheet = wb.get_sheet_by_name(sheet_name)
    processExcelForBow(bow_sheet)
    sys.exit(0)
