numbers = input("Enter numbers: ")

nums = numbers.split()
operation = 0
for i in nums:
  operation += int(i)

print(operation / len(nums))
