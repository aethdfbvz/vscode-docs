import random
import sys

def play_monty_hall():
    round_num = 1
    wins = 0
    total_games = 0

    while True:
        print(f"\nRound #{round_num}: Door 1 | Door 2 | Door 3")

        # Get player's initial choice
        while True:
            choice = input("Choose a door: ")
            if choice == " ":
                print(f"\nGame Over! You won {wins} out of {total_games} games ({(wins/total_games)*100:.1f}% win rate)")
                sys.exit()
            try:
                choice = int(choice)
                if 1 <= choice <= 3:
                    break
                else:
                    print("Please enter 1, 2, or 3")
            except ValueError:
                print("Please enter a valid number")

        # Place goat randomly
        goat_door = random.randint(1, 3)
        print(f"Goat is in Door {goat_door}")

        # Get stay/switch decision
        while True:
            decision = input("Stay or Switch? ").lower()
            if decision in ['stay', 'switch', 'Stay', 'Switch']:
                break
            print("Please enter 'stay' or 'switch'")

        # Calculate final door based on decision
        if decision == 'switch':
            # Find the remaining door that's not the original choice and not the goat
            available_doors = set([1, 2, 3])
            available_doors.remove(choice)
            available_doors.remove(goat_door)
            final_door = list(available_doors)[0]
            print(f"You switched to Door {final_door}", end=" ")
        else:
            final_door = choice
            print(f"You stayed with Door {final_door}", end=" ")

        # Determine if player won
        won = (final_door != goat_door)
        if won:
            print("... You WIN!")
            wins += 1
        else:
            print("... You lose!")

        total_games += 1
        round_num += 1

if __name__ == "__main__":
    print("Welcome to the Monty Hall Game!")
    print("Press SPACE and ENTER at any time to quit")
    play_monty_hall()