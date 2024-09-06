year = 2037

a = year % 19
b = year % 4
c = year % 7

k = int(year / 100)
p = int(k / 3)
q = int(k / 4)

m = (15 + k - p - q) % 30
d = (19 * a + m) % 30
n = (4 + k - q) % 7
e = (2 * b + 4 * c + 6 * d + n) % 7
easter = 22 + d + e

if d == 29 and e == 6:
  print("Easter is on April 19th.")
elif (d == 28 and e == 6) and (11 * m + 11) % 30 < 19:
  print("Easter is on April 18th.")
elif easter > 31:
  easter = easter - 31
  print(f"Easter is on the {easter}.04.{year}.")
else:
  print(f"Easter is on March {easter}th.")
