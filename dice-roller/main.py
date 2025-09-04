dice_faces = {
    1: (
        "-----------",
        "|         |",
        "|    .    |",
        "|         |",
        "-----------"
    ),
    2: (
        "-----------",
        "| .       |",
        "|         |",
        "|       . |",
        "-----------"
    ),
    3: (
        "-----------",
        "| .       |",
        "|    .    |",
        "|       . |",
        "-----------"
    ),
    4: (
        "-----------",
        "| .     . |",
        "|         |",
        "| .     . |",
        "-----------"
    ),
    5: (
        "-----------",
        "| .     . |",
        "|    .    |",
        "| .     . |",
        "-----------"
    ),
    6: (
        "-----------",
        "| .     . |",
        "| .     . |",
        "| .     . |",
        "-----------"
    )
}
import random 


dice = [] 
total = 0 

num_of_dice = int(input("How many many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))


for die in dice_faces: 
    for diee in dice: 
        print(dice_faces.get(diee))

print()
    



    
for die in dice:
    total += die 


print(f"Your total is {total}")





