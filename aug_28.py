#                                                       Exercise (11):-
start = 25
end = 50

for x in range(start, end):
    if x > 1:
        for y in range(2, x):
            if (x % y) == 0:
                break
        else:
            print(x)




#                                                       Exercise (12):-
x, y = 0, 1

for i in range(10):
    print(x, end="   ")
    result = x + y

    x = y
    y = result
print()





#                                                       Exercise (13):-
num = 5
x = 1
for i in range(1, num + 1):
    x = x * i
print(x)





                                                      # Exercise (14):-
num = 76542
reverse_number = 0
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print(reverse_number)



x = 76542
y = str(x)
print(y[::-1])





#                                                       Exercise (15):-
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in list:
    if x % 20 == 0:
        print(x, end=" ")




list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in list[1::2]:
    print(x, end=" ")