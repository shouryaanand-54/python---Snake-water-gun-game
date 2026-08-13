import random

choices = ["snake", "water", "gun"]

computer = random.choice(choices)
player = input("Enter your choice (Snake/Water/Gun): ").lower()

# Check for invalid input
if player not in choices:
    print(" Please enter Snake, Water, or Gun.")
else:
    print(f"\nComputer chose: {computer.capitalize()}")
    print(f"You chose: {player.capitalize()}")

    if computer == player:
        print(" It's a Draw!")

    elif (
        (player == "snake" and computer == "water") or
        (player == "water" and computer == "gun") or
        (player == "gun" and computer == "snake")
    ):
        print(" You Win!")

    else:
        print(" You Lose!")

print("\nThanks for playing!")