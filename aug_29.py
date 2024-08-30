#                                                            Slice :-
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])                 #a of x





#                                                       Exercise (16):-
a = 6
for i in range(1, a + 1):
    print(f"Current Number is :", i, " and the cube is", (i * i * i))





#                                                       Exercise (17):-
n = 5
a = 0
b = 0

for i in range(1, n + 1):
    b = b * 10 + 2
    a += b

print(a)





#                                                       Exercise (18):-
x = int(input("Enter Patter Number: "))

for a in range(1, x + 1):
    print("*" * a)

for a in range(x - 1, 0, -1):
    print("*" * a)