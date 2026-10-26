import random
import os
MIN_LINES = 1
MAX_LINES = 999
wins_path = "wins.txt"

if os.path.exists(wins_path):
    with open(wins_path, "r") as file:
        wins = int(file.read())
else:
    wins = 0

while True:
    print("\nWelcome to a number guessing game, write 'play' to start the game, write 'wins' to see how many wins you have, and 'exit' to leave the programm")
    user_input = str(input("waiting: "))

    def random_number():
        random_choice = random.randint(min_input, max_input)
        return random_choice

    if user_input == "play":
        print("write a range between 1 and 999")
        while True:
            try:
                min_input = int(input("Min: "))
                if MIN_LINES <= min_input <= MAX_LINES:
                    break
                else:
                    print("number must be between 1 and 999")
            except Exception as error:
                print(f"Oops, something went wrong: {error}")
        while True:
            try:
                max_input = int(input("Max: "))
                if MIN_LINES <= max_input <= MAX_LINES:
                    break
                else:
                    print("number must be between 1 and 999")
            except Exception as error2:
                print(f"Oops, something went wrong: {error2}")

        secret_num = random_number()

        while True:
            guess = int(input("Your guess: "))
            if guess == secret_num:
                print("You won, congrats!")
                wins += 1
                with open(wins_path, "w", encoding="utf-8") as file:
                    file.write(str(wins))
                break
            else:
                print("Try again")

    elif user_input == "wins":
        print(wins)
    elif user_input == "exit":
        print("До скорой встречи!")
        break
    else:
        print("invalid command, press crtl+c to restart")
