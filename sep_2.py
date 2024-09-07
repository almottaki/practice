#                                                       excel read:-
import pandas as pd
a = pd.read_excel('excel.xls')
print(a)





#                                                       excel write:-
import pandas as pd

w = pd.Workbook('excel.xls')                          # check

s = w.add_worksheet()

s.write('A1', '10')
s.write('B1', 'Mottaki')
s.write('C1', 'Male')
s.write('D1', 'Bangladesh')

w.close()