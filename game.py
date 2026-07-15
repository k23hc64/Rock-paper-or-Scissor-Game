import random

choices = ["rock", "paper", "scissors"]

print("🪨📄✂️ Welcome to Rock Paper Scissors!")
print("Type rock, paper, or scissors to play.")
print("Type 'quit' to escape before the computer destroys your confidence.\n")

while True:
    user_choice = input("Your move: ").lower()

    if user_choice == "quit":
        print("🏳️ You left the battlefield. The computer accepts your surrender.")
        break

    if user_choice not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\n🤖 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("😐 It's a tie! Great minds think alike.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win! Humanity survives another round.")
    else:
        print("💀 Computer wins! The robots are learning.")

    print("-" * 40)
