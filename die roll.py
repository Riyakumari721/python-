import random

def roll_die():
    return random.randint(1, 6)

def main():
    print("Welcome to the Die Roll Simulator!")
    roll_again = "y"

    while roll_again.lower() == "y":
        result = roll_die()
        print(f"You rolled a {result}")
        roll_again = input("Roll again? (y/n): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
