import random
import sys

def play_monty_hall():
    a = 1 #number of rounds
    results = []
    switch = 0 #number of wons through switching doors
    stay = 0 #number of wons through staying with the same door

    while True:
        print(f"\nRound #{a}: Door 1 | Door 2 | Door 3")

        #get player's initial choice
        while True:
            choice = input("Choose a door: ")
            if choice == " ":
                #display results table
                print("\nRESULTS TABLE")
                print("-" * 40)
                print(f"{'Round':<8} {'Choice':<8} {'Action':<8} {'Outcome':<8}")
                print("-" * 40)
                for result in results:
                    print(f"{result['round']:<8} {result['choice']:<8} {result['action']:<8} {result['outcome']:<8}")

                #display summary
                print("\nSUMMARY")
                print("-" * 40)
                print(f"Wins with switch = {switch}")
                print(f"Wins with stay = {stay}")
                print()

                #calculate probabilities
                total_switches = sum(1 for r in results if r['action'] == 'Switch')
                total_stays = sum(1 for r in results if r['action'] == 'Stay')

                switch_prob = (switch / total_switches * 100) if total_switches > 0 else 0
                stay_prob = (stay / total_stays * 100) if total_stays > 0 else 0

                print(f"Pr(Winning with switch) = {switch_prob:.0f}%")
                print(f"Pr(Winning with stay) = {stay_prob:.0f}%")
                sys.exit()

            try:
                choice = int(choice)
                if 1 <= choice <= 3:
                    break
                else:
                    print("Please enter 1, 2, or 3")
            except ValueError:
                print("Please enter a valid number")

        #place goat randomly
        goat_door = random.randint(1, 3)
        print(f"Goat is in Door {goat_door}")

        #get stay/switch decision
        while True:
            decision = input("Stay or Switch? ").lower()
            if decision in ['stay', 'switch', 'Stay', 'Switch']:
                break
            print("Please enter either 'stay'/'Stay' or 'switch'/'Switch'")

        #calculate final door based on decision
        if decision == 'switch':
            #find the remaining door that's not the original choice and not the goat
            available_doors = set([1, 2, 3])
            available_doors.remove(choice)
            available_doors.remove(goat_door)
            final_door = list(available_doors)[0]
            print(f"You switched to Door {final_door}", end=" ")
        else:
            final_door = choice
            print(f"You stayed with Door {final_door}", end=" ")

        #determine if player won
        won = (final_door != goat_door)
        outcome = "WIN" if won else "Lose"
        print(f"... You {outcome}!")

        #update statistics
        if won:
            if decision == 'switch':
                switch += 1
            else:
                stay += 1

        #store result
        results.append({
            'round': a,
            'choice': choice,
            'action': decision.capitalize(),
            'outcome': outcome
        })

        a += 1

if __name__ == "__main__":
    print("Welcome to the Monty Hall Game!")
    print("Press SPACE and ENTER at any time to quit and see results")
    play_monty_hall()