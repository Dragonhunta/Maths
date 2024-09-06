number = int(input("Enter a number: "))

numbers = [1]
s = 0
t = 1
u = 0
for i in range(8 - 1):
  numbers.append(u + t)
  s = t
  t = u + t
  u = s

print(numbers)