#                                                       Exercise (6):-
num = int(input("Enter Number: "))
count = 0
while num != 0:
        num //= 10
        count += 1
print(f"{count}")





#                                                       Exercise (7):-
a = 5
for x in range(a, 0, -1):
        for y in range(x, 0, -1):
            print(y, end=" ")
        print()





#                                                       Exercise (8):-
list1 = [10, 20, 30, 40, 50]
list1.sort(reverse = True)
for x in list1:
    print(x)





#                                                       Exercise (9):-
for num in range(-10, 0):
    print(num)





#                                                       Exercise (10):-
for i in range(5):
    print(i)
else:
    print("Done")