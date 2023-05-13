# Simple guessing game to showcase basic programming concepts and logic

import random

def display_game_title(fruit):
    game_title = f"■ Welcome to the {fruit.title()} Finder! ■"
    border = "■" * len(game_title)
    print("\n".join([border, game_title, border]))

fruit = "pineapple" # Can be changed according to the player's taste and mood
number_of_doors = 5

# Display game title and welcome message
print()
display_game_title(fruit)

print("\nWith this exciting game, you can now waste away hours of your life... Have fun!!")

# Get player name
player_name = input("\nFirst things first... Please tell me your name: ").title()

# Display game instructions
print(f"\nI have both good and bad news for you, {player_name}.")
print("The bad news is, you've just been transformed into an ape. (Yeah, I told you it was bad.)")
print("The good news is, you now face a very important task:")
print(f"\n\tFIND A {fruit.upper()}!")
print("\nAs you'll soon find out, this is not as simple as it sounds.")
print(f"You see, {player_name}, a delicious {fruit} has been cleverly hidden behind one of the following {number_of_doors} doors.")
print("Your task is to guess behind which one.\n")
print("Got it? Okay, here we go...\n")

print("|X| " * number_of_doors)

fruit_location = random.randint(1, number_of_doors)

# Main game loop
while True:
    try:
        guessed_location = int(input(f"\nSo... Which door is it?? Choose 1-{number_of_doors}: "))
        if guessed_location < 1 or guessed_location > number_of_doors:
            raise ValueError
        if guessed_location == fruit_location: # If player's guess is correct
            print("\nGood job! You found it so you can go bananas!")
            break
        else: # If player's guess is wrong
            print(f"\nOops, no {fruit}. But hunger is a great motivator!")
    except ValueError:
        print(f"\nNice try, {player_name}! But you need to choose a number between 1 and {number_of_doors}.")

# Display thank-you message
print(f"\nMany thanks for playing, {player_name}! It was lots of fun, wasn't it?!")
print(f"Just don't tell anyone how many hours you wasted trying to find the {fruit}...\n")
