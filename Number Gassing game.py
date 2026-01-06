import random

print("🎮 Welcome to Number Guessing Game")

while True:
    print("\nChoose Level:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–20, 6 attempts)")
    print("3. Hard (1–50, 7 attempts)")

    level = int(input("Enter level (1/2/3): "))

    if level == 1:
        max_number = 10
        max_attempts = 5
    elif level == 2:
        max_number = 20
        max_attempts = 6
    elif level == 3:
        max_number = 50
        max_attempts = 7
    else:
        print("❌ Invalid level")
        continue

    number = random.randint(1, max_number)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print("🎉 Congratulations! You WIN 💪")
            print("Attempts used:", attempts)
            break
        elif guess < number:
            print("🔼 Hint: Number is bigger")
        else:
            print("🔽 Hint: Number is smaller")

    if guess != number:
        print("😢 Game Over")
        print("Correct number was:", number)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break