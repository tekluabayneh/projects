
weight = float(input("Enter your weight: ")) 

unit = input("killogram or pound?: (K or L)") 

if unit == "K": 
   weight *=  2.205 
   unit = "Lbs"
elif unit == "L": 
    weight /=  2.205
    unit = "Kgs"
else: 
    print(f"{unit} was not valid") 


print(f"Your weight is: {round(weight)} {unit}")
