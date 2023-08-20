import random

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100.")
answer = random.randint(1,100)
print(answer)

def guess_f(attempts):
    for i in range(attempts+2):
        attempts = attempts - 1
            # print(attempts)
        if attempts == -1:
            print("You've run out of guesses, you lose.")
            return
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return
        elif guess < answer:
            print("Too Low.")
        elif guess > answer:
            print("Too High.")
        print("Guess Again.")
        print(f"You have {attempts} attempts remaining to guess the number")

decision = input("Choose a difficulty. Type 'easy' or 'hard': ")
if decision == 'easy':
    print("You have 10 attempts remaining to guess the number")
    guess_f(10)
else:
    print("You have 5 attempts remaining to guess the number")
    guess_f(5)
    
    
    



