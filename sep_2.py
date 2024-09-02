#                                                       excel read:-
import pandas as pd
a = pd.read_excel('excel.xls')
print(a)





#                                                       excel write:-
import xlsxwriter

w = xlsxwriter.Workbook('excel.xls')

s = w.add_worksheet()

s.write('A1', '10')
s.write('B1', 'Mottaki')
s.write('C1', 'Male')
s.write('D1', 'Bangladesh')

w.close()