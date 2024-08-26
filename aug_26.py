#                                                       Exercise (1):-
i = 1
while i <= 10:
    print(i)
    i += 1

i = range(1, 11)
for x in i:
    print(x)





#                                                       Exercise (2):-
def pattern(a):
    for x in range(1, a + 1):
        for y in range(1, x + 1):
            print(y, end=" ")
        print()
pattern(5)



a = int(input("Enter Range: "))
for x in range(1, a + 1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()





#                                                       Exercise (3):-
a = int(input("Enter number: "))
print("Total: ", sum(range(1, a + 1)))





#                                                       Exercise (4):-
x = int(input("Enter Number: "))
for i in range(1, 11):
    print(f"{x * i}")





#                                                       Exercise (5):-
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x > 500:
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        print(x)