import random
from dice import Die

def dice_roller(dice_input_string):
    """ Creates dice objects from the Die class using user input
        Input Example: '2d8 1d20 5d6'
    """
    # List of all dice user wants to roll
    roll_list = roll_input.split(' ')

    dice_dict = {}
    # Loop that creates dict of Die Obeject
    for dice in roll_list:
        #  {2:Die(20), 1:Die(6), 3:Die(8)}
        dice_list = dice.split('d')
        dice_dict.update({dice_list[0]:Die(dice_list[1])})
    
    for dice in dice_dict.items():
        # dice = (number of dice, Die object)
        for dice_number in range(dice[0]):
            dice[1].roll()
    return


print('Type "q" to quit')

# Menu loop
while True:
    # input from User
    roll_input = input('Type the dice you want to roll (ex: 2d8): ')
    if roll_input == 'q':
        break
    else:
        print('Diceroll result: ' + dice_roller(roll_input))
