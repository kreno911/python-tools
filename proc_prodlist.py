
import csv, sys, os, re
# Excel xlsx processing 
import openpyxl

# Run as: proc_prodlist.py --results 8_27-special_results.xlsx
#           --orig special-8-27-19.xlsx > final_results.csv
# Terminal: View->Tool Windows->Terminal
# Running on windows:
#  \python\Python27\python.exe proc_prodlist.py --orig shepher-9_13.xlsx
#                                               --results shepher-9_13-result.xlsx
#       --shtname Inventory

######################################
# Return a map of UPC to Brand name SKU
######################################
def getUPCtoSKUMap(sheet, upc_row, brand_sku_row):
    data = {}
    # Start at row 2 to skip header
    for row in range(2, sheet.max_row + 1):
        upc = str(sheet[upc_row + str(row)].value)
        if upc == "None" or upc == "- None -" or "'" in upc:
            continue
        # UPC fields that start with 0 are truncated
        # so 033 will be 33 which is wrong

        # Did some testing, some UPCs are 13 or 14 chars long but
        # any I added '0' to front matched a leading zero check
        # First exported whole UPC row to CSV
        #if str(upc_fixed)[0] == "0":
            #print upc_fixed
        upc_fixed = "%012d" % int(upc)
        sku = sheet[brand_sku_row+str(row)].value
        data[upc_fixed] = sku
    return data

######################################
# This will create a master list containing ASIN/UPC/Supplier SKU
# Results file will usually be smaller (less rows) than original
# Original contains:
#   UPC/Supplier Sku/Supplier Desc
# Results contains:
#   ASIN/Profit/Amz title
######################################
def processCombined(result_sheet, orig_sheet):
    print "ASIN,UPC,SupplierSku,Price,AmzDescription"
    # UPC,SKU
    #data = getUPCtoSKUMap(orig_sheet, 'F', 'A')  # Special
    data = getUPCtoSKUMap(orig_sheet, 'G', 'B')
    for row in range(2, result_sheet.max_row + 1):
        price = result_sheet['E'+str(row)].value
        if price is None:
            continue
        profit = result_sheet['I'+str(row)].value
        price = result_sheet['E' + str(row)].value
        asin = result_sheet['A'+str(row)].value
        upc  = result_sheet['B'+str(row)].value.lstrip()
        amz_desc   = result_sheet['D' + str(row)].value
        suppl_code = "none"
        if upc in data:
            suppl_code = data[upc]
        if suppl_code == "none":
            print "Supplier code is NONE!!!! [%s] (Check data assignment)" % upc
            sys.exit(13)
        # Need to remove spacial characters in description
        amz_desc = re.sub('[^A-Za-z0-9]+', ' ', amz_desc)
        print "%s,%s,%s,%s,%s" % (asin,upc,suppl_code,price,amz_desc)
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

original_file = "none"
sheet_name = "Inventory"
length = len(sys.argv)
if length < 2:
    print "--shtname <sheet nm>|--orig <xlsx>|--results <xlsx>"
    print "provide both orig/results together"
    print "--shtname is for sheets that are different than default."
    print "--orig is the original xlsx file"
    sys.exit(11)
else:
    for v in range(1, length):
        if sys.argv[v] == "--shtname":
            sheet_name = sys.argv[v+1]
        # original file we grab UPC/Supplier SKUs
        if sys.argv[v] == "--orig":
            original_file = sys.argv[v+1]
        if sys.argv[v] == "--results":
            results_file = sys.argv[v+1]

if original_file != "none" and results_file != "none":
    wb = openpyxl.load_workbook(original_file)
    orig_sheet = wb.get_sheet_by_name(sheet_name)
    wb2 = openpyxl.load_workbook(results_file)
    result_sheet = wb2.get_sheet_by_name("Worksheet")
    processCombined(result_sheet, orig_sheet)

