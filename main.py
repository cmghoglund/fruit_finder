# Simple guessing game to showcase basic programming concepts and logic

import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_fruit(fruits):
    return random.choice(fruits)

def display_game_title(fruit):
    game_title = f"■ Welcome to the {fruit.title()} Finder! ■"
    border = "■" * len(game_title)
    print("\n".join([border, game_title, border]))

def display_game_intro():
    intro = [
        "\nWith this exciting game, you can now waste away hours of your life... Have fun!!",
    ]
    print("\n".join(intro))

def display_game_instructions(player_name, fruit, number_of_doors):
    instructions = [
        f"\nI have both good and bad news for you, {player_name}.",
        "The bad news is, you've just been transformed into an ape. (Yeah, I told you it was bad.)",
        "The good news is, you now face a very important task:",
        f"\n\tFIND A {fruit.upper()}!",
        "\nAs you'll soon find out, this is not as simple as it sounds.",
        f"You see, {player_name}, a delicious {fruit} has been cleverly hidden behind one of the following {number_of_doors} doors.",
        "Your task is to guess behind which one.\n",
        "Got it? Okay, here we go...\n",
    ]
    print("\n".join(instructions))

def get_player_name():
    player_name = input("\nFirst things first... Please tell me your name: ").title()
    return player_name

def display_final_message(player_name, fruit):
    message = [
        f"\nThat was a lot of fun, wasn't it, {player_name}?!",
        f"Just don't tell anyone how much time you wasted trying to find the {fruit}...\n",
    ]
    print("\n".join(message))

def get_player_guess(player_name, number_of_doors):
    while True:
        try:
            guessed_location = int(input(f"\nSo... Which door is it?? Choose 1-{number_of_doors}: "))
            if guessed_location < 1 or guessed_location > number_of_doors:
                raise ValueError
            return guessed_location
        except ValueError:
            print(f"\nNice try, {player_name}! But you need to choose a number between 1 and {number_of_doors}.")

def evaluate_player_guess(guessed_location, fruit_location, fruit):
    if guessed_location == fruit_location: # If player's guess is correct
        print("\nGood job! You found it so you can go bananas!")
        return True
    else: # If player's guess is wrong
        print(f"\nOops, no {fruit}. But hunger is a great motivator!")
        return False

def play_game(fruit, number_of_doors):
    clear_screen()
    display_game_title(fruit)
    display_game_intro()    
    player_name = get_player_name()
    display_game_instructions(player_name, fruit, number_of_doors)

    print("|X| " * number_of_doors)
    fruit_location = random.randint(1, number_of_doors)

    # Main game loop
    while True:
        guessed_location = get_player_guess(player_name, number_of_doors)
        if evaluate_player_guess(guessed_location, fruit_location, fruit):
            break

        input("\nPress Enter/Return to continue...")
        clear_screen()
        display_game_title(fruit)
        display_game_intro()    
        display_game_instructions(player_name, fruit, number_of_doors)

        print("|X| " * number_of_doors)

    display_final_message(player_name, fruit)

    continue_playing = input("Do you want to continue playing? (y/n) ").lower()
    if continue_playing == 'y':
        fruit = get_random_fruit(FRUITS)
        play_game(fruit, number_of_doors)
    else:
        print("\nThat's too bad, but thanks for playing! Bye!!\n")

if __name__ == '__main__':

    FRUITS = (
        "apple",
        "banana",
        "cantaloupe",
        "grapefruit",
        "kiwi",
        "lemon",
        "mango",
        "orange",
        "peach",
        "pear",
        "pineapple",
        "watermelon",
    )

    fruit = get_random_fruit(FRUITS)

    number_of_doors = 5

    play_game(fruit, number_of_doors)
