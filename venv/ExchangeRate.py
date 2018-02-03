import xlrd
import pandas as pd

df = pd.read_excel(open('C:/Users/Huzaifa/Documents/HACK.xlsx','rb'), sheet_name='Sheet4')
df.as_matrix();
book = xlrd.open_workbook("C:/Users/Huzaifa/Documents/HACK.xlsx")

print("There are: ", book.nsheets, " sheets with names")
print(book.sheet_names())
print(" ")

firstSheet = book.sheet_by_index(0)

CurrencyInitial = "British Pound"
CurrencyFinal = "Bahraini Dinar"
AmountInitial = 4.0
RateInitial = 0
RateFinal = 0


for i in range (firstSheet.nrows):
#  for j in range (firstSheet.ncols):
    if firstSheet.cell(i, 0).value ==  "British Pound":
        CurrencyInitial == firstSheet.cell(i, 0).value
        print(CurrencyInitial)
        RateInitial = firstSheet.cell(i, 1).value
        print(RateInitial)

    if firstSheet.cell(i, 0).value == "Bahraini Dinar":
        CurrencyInitial == firstSheet.cell(i, 0).value
        print(CurrencyFinal)
        RateFinal = firstSheet.cell(i, 1).value
        print(RateFinal)

    #print(firstSheet.cell(i,0).value)

AmountFinal = (RateFinal/RateInitial) * AmountInitial

print(AmountFinal)