# in-built module that generates
# random numbers
import random

def monty_game(chances, switch_strategy=True):

    for i in range(chances):
        doors = [0, 0, 0]
        # randomly replaces one of the goats with a car
        car_door = random.randint(0,2)
        doors[car_door] = 1
        a = 1

        # contestant makes a choice
        print('Round #' + a + ': Door 1 | Door 2 | Door 3')
        first_choice = int(input('Choose a door: '))
        a += 1

        # monty reveals a goat from a door that hasn't been opened by the contestant
        monty_choice = [x for x in range(3) if x != first_choice and doors[x]==0]
        print('Goat is in Door ' + monty_choice)
        # .choice() method from the random module
        second_choice = input('Stay or switch? ')
        if second_choice == 'stay' or second_choice == 'Stay':
            monty_choice = [x for x in range(3) if x != first_choice and doors[x]==0]  #i have no idea what this does, will ask about later.
            b = 'You switched to Door ' + monty_choice
            return b
        else:
            b = 'You stayed with Door ' + first_choice
            return b

        # switch strategy
        if switch_strategy:
            third_choice = next(x for x in range(3) if x != first_choice and x != second_choice)

            if doors[third_choice] == 1:
                c = 'WIN!'
                return c
            else:
                c = 'lose'
                return c

        print(b + ' ....You ' + c)