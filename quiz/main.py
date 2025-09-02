questions = (
    "does you Mon loves you",
    "are you felling ok",
    "how old are you",
    "do you love mango",
    "do you often go to church"
)

options = (
    ("A, yes ", "B, no", "C, sometimes", "D, dunno"), 
    ("A, yes", "B, maybe", "C, of course", "D, i think"),
    ("A, no", "B, yes", "C, yes", "D, yes"),
    ("A, yes", "B, yes", "C, no", "D, yes"),
    ("A, yes", "B, yes", "C, yes", "D, yes")
)

answers = ("A", "C", "A", "C", "D")
guesses = []
score = 0

for qu_num in range(len(questions)):
    print("------------------")
    print(questions[qu_num])
    
    for op in options[qu_num]:
        print(op)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[qu_num]:
        score += 1
        print("YOU GOT IT MAN!")
    else:
        print("YOU CAN DO BETTER MAN!")
        print(f"{answers[qu_num]} is the correct answer")

percentage = int((score / len(answers)) * 100)
print(f"Your total Score is {score}")
print(f"Your percentage is {percentage}%")

