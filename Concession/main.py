menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "burger": 5.75,
    "fries": 2.50,
    "soda": 1.25,
    "ice cream": 2.00
}

cart = []
total = 0 


print("======= Menu ========")
for key, value in menu.items(): 
    print(f"{key:10}: ${value:.2f}")
print("======= Menu ========")
while True: 
    food = input("Select an item (q to quit BTW): ").lower() 
    if food == "q": 
        break 
    elif menu.get(food, "not found"): 
        cart.append(food)

print("======= Your Cart ========")
for item in cart: 
    total += menu[item]
    print(item, end=" ") 


print(f"\n======= Your total is ${total}========\n")



