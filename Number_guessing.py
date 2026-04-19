import random

print("Hello! This is a random number guessing game")

choice = "y"
BestScore = []

def get_hint(guess, number):
    diff = abs(guess - number)
    if diff == 0:
        return "correct"
    elif diff <= 2:
        return "Almost there! 🔥"
    elif diff <= 5:
        return "So close! 👀"
    elif guess < number:
        return "Guess higher ⬆️"
    else:
        return "Guess lower ⬇️"

while choice.lower() == "y":
    print("\nEnter your level")
    print("1. Easy --> 1 to 50, 15 attempts")
    print("2. Medium --> 1 to 100, 10 attempts")
    print("3. Hard --> 1 to 100, 5 attempts")
    print("4. Custom")

    try:
        level = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number!")
        continue

    # Set parameters
    if level == 1:
        start, stop, max_attempts = 1, 50, 15

    elif level == 2:
        start, stop, max_attempts = 1, 100, 10

    elif level == 3:
        start, stop, max_attempts = 1, 100, 5

    elif level == 4:
        try:
            start = int(input("Enter start value: "))
            stop = int(input("Enter stop value: "))
            max_attempts = int(input("Enter attempts: "))
        except ValueError:
            print("❌ Invalid input!")
            continue

        if start >= stop:
            print("❌ Start must be less than stop!")
            continue

    else:
        print("❌ Choose between 1–4")
        continue

    number = random.randint(start, stop)
    attempts = 0
    win = False

    print(f"\nGuess a number between {start} and {stop}")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Enter a valid number!")
            continue

        if guess < start or guess > stop:
            print(f"⚠️ Enter between {start} and {stop}")
            continue

        attempts += 1
        hint = get_hint(guess, number)

        if hint == "correct":
            print(f"🎉 You won in {attempts} attempts!")
            BestScore.append(attempts)
            win = True
            break
        else:
            print(hint)

    if not win:
        print(f"😢 You lost! The number was {number}")

    choice = input("\nPlay again? (y/n): ")

# Best score
if BestScore:
    print(f"\n🏆 Best Score: {min(BestScore)} attempts")
else:
    print("\nNo wins recorded yet.")
