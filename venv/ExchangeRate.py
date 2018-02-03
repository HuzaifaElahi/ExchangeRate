import xlrd
import pandas as pd

#Open excel file
#pd.read_excel(open('C:/Users/Huzaifa/Documents/HACK.xlsx','rb'), sheet_name='Sheet4')
book = xlrd.open_workbook("C:/Users/Huzaifa/Documents/HACK.xlsx")

#Details of Excel file sheets
print("There are: ", book.nsheets, " sheets with names")
print(book.sheet_names())
print(" ")

#Access the corresponding excel sheet
firstSheet = book.sheet_by_index(0)

#Initialize Variables
CurrencyInitial = "British Pound"
CurrencyFinal = "Bahraini Dinar"
AmountInitial = 4.0
RateInitial = 0
RateFinal = 0

#Loop through excel sheet and find Currency Initial and Currency Final and assign rates
for i in range (firstSheet.nrows):
#  for j in range (firstSheet.ncols):
    if firstSheet.cell(i, 0).value ==  CurrencyInitial:
        CurrencyInitial == firstSheet.cell(i, 0).value
        print(CurrencyInitial)
        RateInitial = firstSheet.cell(i, 1).value
        print(RateInitial)

    if firstSheet.cell(i, 0).value == CurrencyFinal:
        CurrencyInitial == firstSheet.cell(i, 0).value
        print(CurrencyFinal)
        RateFinal = firstSheet.cell(i, 1).value
        print(RateFinal)

    #print(firstSheet.cell(i,0).value)

#Make final caculation
AmountFinal = (RateFinal/RateInitial) * AmountInitial
print(AmountFinal)