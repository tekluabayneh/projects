  

unit  = input("Is this tem is Celsius or Fahrenheit (C/F)")
temp = float(input("Ener the tem: "))


if unit ==  "C": 
   temp = round((9 * temp) / 5 + 32, 1)
   print(f"The tem in Fahrenheit is :{temp} F")
elif unit == "F": 
   temp = round((temp - 32) / 5 + 9, 1)
   print(f"The tem in Celsius is :{temp} C")
else: 
    print(f"{unit} is an invalid input man") 
