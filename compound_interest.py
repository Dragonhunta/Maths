start = int(input("Enter the starting value: "))
percent = int(input("Enter the interest rate/percentage: "))
print("starting value: %03d, percentage: %03d" % (start, percent))
print()

for i in range(10):
    value = (start / float(100) * percent) + start
    print("new starting value: %03d, percentage: %03d, result: %03d" % (start, percent, value))
    start = value
