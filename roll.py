import random
from dice import Die

def dice_roller(dice_input_string):
    """ 
    Creates dice objects from the Die class using user input
    Rolls the dice and outputs the results as a string

    """
    # List of all dice user wants to roll
    roll_list = roll_input.split(' ')
    output = 'Diceroll result: '
    dice_dict = {}
    # Loop that creates dict of Die Obeject
    for dice in roll_list:
        #  {2:Die(20), 1:Die(6), 3:Die(8)}
        dice_list = dice.split('d')
        dice_dict.update({dice_list[0]:Die(dice_list[1])})

    dice_results = []
    for dice in dice_dict.items():
        # dice = (number of dice, Die object)
        for dice_number in range(int(dice[0])):
            dice_results.append(dice[1].roll())
    i = 0
    # Loop that creates results string
    for result in dice_results:
        if i == 0:
            output += str(result)
        elif i == len(dice_results):
            output += "{}".format(result)
        else:
            output += " + {}".format(result)
        i += 1
    
    output += " = {}".format(sum(dice_results))
    return output


print('Type "q" to quit')

# Menu loop
while True:
    # input from User
    roll_input = input('Type the dice you want to roll (ex: 2d8): ')
    if roll_input == 'q':
        break
    else:
        print(dice_roller(roll_input))
