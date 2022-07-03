#This is a guess the number game.
import random

secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20 , take a guess")

#Ask the player to guess 6 times
for guessTaken in range (1,7):
    guess = int(input("Take a guess"))

    if guess < secretNumber:
        print("Your guess is too low , guess higher")
    elif guess > secretNumber:
        print(" Your guess is too high , guess lower")
    else:
        break # The guess was correct so were leaving this loop
if guess == secretNumber:
    print('goodjob you guessed my number in ' , str(guessTaken) + ' Guesses!')
else:
    print(f"Nope the number i was thinking of was {secretNumber}")