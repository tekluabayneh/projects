import random 


options = ("rock", "paper", "scissors") 

player = None 
computer = random.choice(options) 

player = input("Enter a choice (rock, paper, scissors): ") 
while player not in options: 
   print(f"{player} is not something that exist in game") 



if player == computer: 
    print("it's a tie!") 
elif player == "rock" and computer == "scissors": 
    print("You win!")
elif player == "paper" and computer == "rock": 
    print("You win!")
elif player == "sissors" and computer == "paper": 
    print("You win!")
else: 
    print("You win!")

print(f"player: {player}") 
print(f"computer: {computer}") 
