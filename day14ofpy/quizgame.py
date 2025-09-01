# python quiz game

question = (" Which planet is known as the Red Planet?",
            "what is the Chemical symbol for gold",
            "Who wrote the play 'Romeo and juliet",
            "what is the capital city of japan?")
options = (("A. venus","B.earth","C.jupiter","D.mars"),
           ("A. Au","B.ia","C.ds","D.zine"),
            ("A. Romeo","B.William Shakespeare","c.William","d.shake"),
            ("A.Tokyo","B.newyork","C.delhi","D.us"))

answers = ("C","A","B","A")

guesses = []
score = 0
question_num = 0

for question in question:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("-----------------------")
print("       RESULTS        ")
print("-----------------------")

for answer in answers:
    print(answer, end=" ")
    print(f"Your score is {score}")
    print()
print("guess answer: ", end="")
for guess in guesses:
    print(guess, end=" ")
    print()


score = int(score / len(answers) * 100)
print(f"Your score is {score}%")