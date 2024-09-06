from random import randint

def lottery():
  numbers = []
  while len(numbers) < 6:
    number = randint(1, 49)
    if number not in numbers:
      numbers.append(number)

  return numbers

print(lottery())