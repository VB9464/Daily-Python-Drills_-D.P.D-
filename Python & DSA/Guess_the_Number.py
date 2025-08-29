import random

def guess_the_number():
   print("🎯 Welcome to Guess the Number Game!")
   print("Enter Number Between 1 to 100")

   # computer chooses the random number between 1 to 100
   number_to_guess = random.randint(1,100)
   attempts = 0
   while True :
       try:
           # Take input from user
           guess = int(input("Enter you guessed Number :"))
           attempts = 0

           if guess < number_to_guess:
                print(" Too low! Try again.")
           elif guess > number_to_guess:
                print("Too high! Try again.")
           else: 
                print(f"Congratulations! You guessed it in {attempts} attempts ")
                break
       except ValueError:
           print(" Please enter a valid Number!")


guess_the_number()

