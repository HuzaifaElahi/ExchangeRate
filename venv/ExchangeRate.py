import xlrd
import pandas as pd

df = pd.read_excel(open('C:/Users/Huzaifa/Documents/HACK.xlsx','rb'), sheetname='Sheet4')
df.as_matrix();
book = xlrd.open_workbook("C:/Users/Huzaifa/Documents/HACK.xlsx")

print("There are: ", book.nsheets, " sheets with names")
print(book.sheet_names())
print(" ")

firstSheet = book.sheet_by_index(0)

#print(firstSheet.row_values(0))
#cell = firstSheet.cell(4,1)
#print(cell)

print(firstSheet.nrows)
print(firstSheet.ncols)

for i in range (firstSheet.nrows):
#  for j in range (firstSheet.ncols):
        print(firstSheet.cell(i,0))