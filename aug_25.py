if __name__ == '__main__':
    a = int(input())
    if (a >= 80):
        print(f"Mark:- {a} and Grade:- A+ (5.0)")
    elif (a >= 70):
        print(f"Mark:- {a} and Grade:- A (4.0)")
    elif (a >= 60):
        print(f"Mark:- {a} and Grade:- A- (3.5)")
    elif (a >= 50):
        print(f"Mark:- {a} and Grade:- B (3.0)")
    elif (a >= 40):
        print(f"Mark:- {a} and Grade:- C (2.0)")
    elif (a >= 33):
        print(f"Mark:- {a} and Grade:- D (1.0)")
    else:
        print(f"Mark:- {a}, Fail (0)")

i = 1
while i < 8:
  print(i)
  i += 1


i = 1
while i < 6:
  print(i)
  if i == 4:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

x = ["apple", "banana", "cherry"]
y = ["mango", "pineapple", "papaya"]
z = []
for data in x:
    z.append(data)
    if data == "banana":
        print("Yes")

a = ["mottaki", "mamun", "akash", "mahin"]
b = []
for x in a:
   if "m" in x:
      b.append(x)

print(b)


y = 10
z = 0
if (z == 0):
    print("Cannot divide by zero")
else:
    print(y // z)

print("a")