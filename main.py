print("\nWelcome to the Banana Finder!")
print("\nWith this exciting game, you can now waste away hours of your life... Have fun!!")

player_name = input("\nFirst things first... Please tell me your name: ")
print("\nI have both good and bad news for you, " + player_name + ".")
print("The bad news is, you've just been transformed into an ape. (Yeah, I told you it was bad.)")
print("The good news is, you now face a very important task:")
print("\n\tFIND A BANANA!")
print("\nAs you'll soon find out, this is not as simple as it sounds.")
print("You see, " + player_name + ", a delicious banana has been cleverly hidden behing one of the following five doors.")
print("Your task is to guess behind which one.\n")
print("Got it? Okay, here we go...\n")

print("|X| |X| |X| |X| |X|")

banana_location = 1

guessed_location = input("\nSo... Which door is it?? Choose 1-5: ")

if guessed_location == banana_location:
    print("\nGood job! You found it so you can go bananas!")
else:
    print("\nOops, no banana. But hunger is a great motivator!")
