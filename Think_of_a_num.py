import time

print("🧠 Welcome to the Mind Reading Game!")

replay = True

while replay:
    print("\nThink of a number, and I will guess it!")

    try:
        start = int(input("Enter start range: "))
        stop = int(input("Enter end range: "))
    except ValueError:
        print("❌ Please enter valid numbers!")
        continue

    if start >= stop:
        print("❌ Start must be less than stop!")
        continue

    attempts = 0

    while True:
        if start > stop:
            print("🤔 Something doesn't add up. Did you change the number?")
            break

        attempts += 1
        guess = (start + stop) // 2

        print("\nThinking", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)

        print(f"\nMy guess is: {guess}")

        answer = input("Is this correct? (yes/no): ").lower()

        if answer == "yes":
            print(f"🎉 Got it in {attempts} attempts!")
            break

        hint = input("Is your number Higher (h) or Lower (l)? ").lower()

        if hint == "h":
            start = guess + 1
        elif hint == "l":
            stop = guess - 1
        else:
            print("❌ Invalid input! Please enter 'h' or 'l'.")

        print(f"📉 Updated range: {start} to {stop}")

    choice = input("\nDo you want to play again? (y/n): ").lower()
    if choice != "y":
        replay = False

print("\n👋 Thanks for playing!")
