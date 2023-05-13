import random

number_of_doors = 5

print()
game_title = "■ Welcome to the Banana Finder! ■"
print("■" * len(game_title))
print(game_title)
print("■" * len(game_title))

print("\nWith this exciting game, you can now waste away hours of your life... Have fun!!")

player_name = input("\nFirst things first... Please tell me your name: ")
print(f"\nI have both good and bad news for you, {player_name}.")
print("The bad news is, you've just been transformed into an ape. (Yeah, I told you it was bad.)")
print("The good news is, you now face a very important task:")
print("\n\tFIND A BANANA!")
print("\nAs you'll soon find out, this is not as simple as it sounds.")
print(f"You see, {player_name} , a delicious banana has been cleverly hidden behind one of the following five doors.")
print("Your task is to guess behind which one.\n")
print("Got it? Okay, here we go...\n")

print("|X| " * number_of_doors)

banana_location = random.randint(1, number_of_doors)

keep_guessing = True

while keep_guessing:
    guessed_location = input("\nSo... Which door is it?? Choose 1-5: ")
    guessed_location = int(guessed_location)

    if guessed_location == banana_location:
        print("\nGood job! You found it so you can go bananas!")
        keep_guessing = False
    else:
        print("\nOops, no banana. But hunger is a great motivator!")

print(f"\nMany thanks for playing, {player_name}! It was lots of fun, wasn't it?!")
print("Just don't tell anyone how many hours you wasted trying to find the banana...\n")
