# 15 Common Errors in Python [Done]      #https://betterstack.com/community/guides/scaling-python/python-errors/




#                                                       txt read:-
f = open("homework.txt")
a = f.read()
print(a)
f.close()

with open("homework.txt") as f:
    a = f.read()

    print(a)




#                                                       txt write:-
file = open ('homework.txt', 'w')
file.write('New')
file.close()

with open('homework.txt', 'w') as file:
    file.write('New Text')





#                                                       txt append:-
file = open('homework.txt', 'a')
file.write('\nHello World')
file.close()

with open('homework.txt', 'a') as file:
    file.write('\nPython')





#                                                       csv read:-
import csv

with open("sample.csv", 'r') as f:
  csvreader = csv.reader(f)
  for x in csvreader:
    print(x)





#                                                       csv append:-
from csv import writer
List = [11, 'abc', 'mottaki', 1, 'UAE', 'xyz', 'this is new row']

with open('sample.csv', 'a') as f:
    a = writer(f)
    a.writerow(List)
    f.close()