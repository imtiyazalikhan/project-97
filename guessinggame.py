import random
print("Number guessing game")
number = random.randint(1,9)
chances = 0

print("Guess a number (brtween 1 two 9")

while chances <5:
    
    guess = int(input("enter you guess:- "))

    if guess == number:
        print("congratulation you won !!")
        break
    elif guess < number:
        print("you guess was too low: guess a number higher than", guess)
    else:
        print("you guess was too high: guess a number lower than", guess)
    chances += 1
    if not chances < 5:
        print("you lose !! the number is ",number) 