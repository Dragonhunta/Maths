number = int(input("Enter a number: "))

factorial = 1
num = 1
for i in range(number):
  factorial = factorial * num
  num += 1

print(factorial)