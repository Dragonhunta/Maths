num = int(input("Enter a number: "))

ls = []

for i in range(2, num):
  if i == 2 or i == 3 or i == 5 or i == 7:
    ls.append(i)
  elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
    pass
  else:
    ls.append(i)

print(ls)