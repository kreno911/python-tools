import csv, sys, os, re
# Excel xlsx processing
import openpyxl

# proc_prodlist.py --input <file>.xlsx > 9_13.csv

######################################
# This will create the initial csv file to feed into the analyzer
######################################
def processExcelForBow(sheet):
    print("Base Price,UPC Code")
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
            print("Found: ", upc)
            upc = upc.split(".")[0]
        upc_fixed = "%012d" % int(upc)
        print("%s,%s" % (price,upc_fixed))

bow_file = "none"
sheet_name = "Inventory"
show_sheets = False
length = len(sys.argv)
if length < 2:
    print("Options: --input <xlsx> [--sheetname <sheet>|--sheets]")
    print("Option --sheets will print sheet names and exit.")
    print("Sheet name default is %s" % sheet_name)
    sys.exit(11)
else:
    for v in range(1, length):
        # Export for Bow's tool (price,upc)
        if sys.argv[v] == "--input":
            bow_file = sys.argv[v+1]
        if sys.argv[v] == "--sheets":
            show_sheets = True
        if sys.argv[v] == "--sheetname":
            sheet_name = sys.argv[v+1]

if bow_file != "none":
    if not os.path.exists(bow_file):
        print("File %s does not exist." % bow_file)
        sys.exit(11)
    wb = openpyxl.load_workbook(bow_file)
    # If we want to show sheets, just print them and exit
    if show_sheets:
        sheets = wb.sheetnames
        for sht in sheets:
            print("-->%s" % sht)
    else:
        # Can access a sheet by name with wb[sheets[<sheet_num>]]
        bow_sheet = wb.active #wb.get_sheet_by_name(sheet_name)
        processExcelForBow(bow_sheet)
