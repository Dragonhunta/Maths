def domino(border):
  x = 1
  y = 1
  ls = []
  while True:
    if x > border:
      return ls
      break
    elif y > border:
      y = 1
      x += 1
    elif y <= border:
      new = str(x) + "|" + str(y)
      if new not in ls:
        ls.append(new)
        y += 1

number = int(input("Enter a number: "))

dominos = []
for i in domino(number):
  if int(i[0]) <= int(i[2]):
    dominos.append(i)

print(dominos)
