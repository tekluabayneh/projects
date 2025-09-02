foods = [] 
prices = [] 
total = 0 


while True: 
    food = input("Enter a food to buy (q to quit): ") 
    if food.lower() == "q":
        break
    else: 
        price = float(input(f" Enter the price of a {food}: $"))
        foods.append(food) 
        prices.append(price)




print("------YOUR CART-----")
for x in foods: 
    print(x) 

for x in prices: 
    total = total + x  


print(f"Your total is {total}")



