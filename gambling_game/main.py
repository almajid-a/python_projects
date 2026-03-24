# Python Project: Gambling Game
# Focus: control flow, randomness, and user interaction

import random

# first dice roll is an int
first_dice_roll = random.randint(1,6)

# second dice roll is an int
second_dice_roll = random.randint(1,6)

# YOUR CODE BELOW
print("Welcome to the Dice Game, if you win you win double!")
user_input = input("Would you like to play? (yes/no) ")

if user_input == "no": # User don't want to play.
    print("Thanks, see you soon")

elif user_input == "yes": # User wants to play!
    wager = int(input("How much would you like to wager? (enter an integer less than or equal 100) "))
    user_guess = int(input("What is your guess number guess? (1-6) "))
    # print(f"If you guess correctly you win {wager * 2}") <- commented out as it was breaking the test!

    if wager > 100: # User input is greater than 100
        print("That's too much sorry")
       
    elif user_guess == first_dice_roll: # User wins!
        winnings = wager * 2
        print(f"Congratulations, you win {winnings}")
        user_second_input = input(f"\nWould you like to go double play for {winnings * 2 } ? (yes/no) ")
        
        if user_second_input == "yes": # User wants to play a second round!
            user_second_guess = int(input(f"What is your guess number guess? (1-6) "))

            if user_second_guess == second_dice_roll: # Won original bet & second bet!!
                winnings = (wager * 2) + (winnings * 2)
                print(f"Wow! you won all {winnings} in total")

            else: # Won original bet, lost second bet.
                winnings = (- wager * 2)
                print(f"You lose all {winnings} in total")

        else: # User doesn't want to play a second round.
            print(f"Thank you, your current total is {winnings}")

    else: # User loses first round.
        winnings = - (wager)
        print(f"You lost your wager {wager}")
        user_second_input = input(f"\nWould you like to go double play for {wager * 2} ? (yes/no) ")
        
        if user_second_input == "yes": # User wants another try!
            user_second_guess = int(input(f"What is your guess number guess? (1-6) "))

            if second_dice_roll == user_second_guess: # User wins second bet after losing first bet!
                winnings = winnings + (wager * 4)
                print(f"Wow! you won all {winnings} in total")

            else: # Double loss.
                winnings = winnings - (wager * 2)
                print(f"You lose all {winnings} in total")

else: # Invalid input from user.
    print("Invalid input, Please try again")