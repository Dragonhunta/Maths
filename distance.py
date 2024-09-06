numbers = input("Enter numbers: ")

numbers = numbers.split()
s = 0
for i in numbers:
  for j in numbers:
    diff = int(i) - int(j)
    if diff > s:
      s = diff
print(s)
