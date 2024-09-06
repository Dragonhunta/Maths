number = int(input("Enter the temperature: "))
name = input("Enter 1 for Celsius, 2 for Fahrenheit and 3 for Kelvin: ")

if name == "1":
  print(f"{number} degree Celsius are:")
  fahrenheit = (number * 9/5) + 32
  print(f"{fahrenheit} degree Fahrenheit.")
  kelvin = number + 273,15
  print(f"{kelvin} degree Kelvin.")
elif name == "2":
  print(f"{number} degree  Fahrenheit are:")
  celsius = (number - 32) * 5/9
  print(f"{celsius} Celsius.")
  kelvin = (number - 32) * 5/9 + 273.15
  print(f"{kelvin} degree Kelvin.")
elif name == "3":
  print(f"{number} degree Kelvin are:")
  celsius = number - 273.15
  print(f"{celsius} Celsius.")
  fahrenheit = (number - 273.15) * 9/5 + 32
  print(f"{fahrenheit} degree Fahrenheit.")

