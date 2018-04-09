import random
import os
import re
import operator

from dice import Die


def dice_roller(dice_input_string):
    """
    Creates dice objects from the Die class using user input
    Rolls the dice and outputs the results as a string
    
    """
    # List of all dice user wants to roll
    roll_list = re.findall(r'\d*[d,D]\d+', dice_input_string) 
    # Check if any numbers need to be added as modifiers
    mod_string = re.findall(r'\s+[0-9]+\s+', dice_input_string + ' ')
    mod_int = int()
    if mod_string:
        mod_int = int(mod_string[0])
    # Check if there are any operators they want to use on their dice rolls
    op = re.findall(r'[+,\-,*]', dice_input_string)
    # operator reference library
    ops = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul
    }
    # Output string
    output = 'Diceroll result: '
    # Dice Dictionary used to hold Die Objects
    # EX: {2:Die(20), 1:Die(6), 3:Die(8)}
    dice_dict = {}
    # Loop that creates dict of Die Object
    for dice in roll_list:
        dice_list = dice.split('d')
        if '' in dice_list or dice_list[0] == '1':
            # No number was given before 'd' ex: 'd20' so the integer 1 is used since only a single die is cast
            dice_dict.update({1:Die(dice_list[1])})
        else:
            # Key is the number of dice rolled, Value is the Die object
            dice_dict.update({dice_list[0]:Die(dice_list[1])})
            
    # List that holds results of the rolled Dice       
    dice_results = []
    # Loop that rolls the dice a number of times equal to the Key (number of dice)
    # then appends the result to the dice_results list
    for dice in dice_dict.items():
        # dice = (number of dice, Die class object)
        for dice_number in range(int(dice[0])):
            dice_results.append(dice[1].roll())
    i = 0
    # Loop that creates results string
    for result in dice_results:
        # If this result is the first in the list just add the string to 'output'
        if i == 0:
            output += str(result)
        # Otherwise it needs to be added together with proper spaces
        else:
            output += " + {}".format(result)
        i += 1
    # Adds up all dice rolled into a total
    total = sum(dice_results)
    # if a modifier and operator were found, use them to change total and add them to the output
    if mod_int and op:
        total = ops[op[0]](total,mod_int)
        output += " {} {}".format(op[0], mod_int)
    output += " = {}".format(total)

    return output


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


roll_input = ''


def show_results():
    """
    Keeps menu open for instruction
    """
    clear_screen()

    print("""
    ############
    Dice Roller!
    ############

    Type 'done' to Quit

    ----------------------------------------
    Roll dice by typing roll combos: ex:'2d6'
    ----------------------------------------
    """)
    if roll_input:
        print(dice_roller(roll_input))

show_results()

# Input loop
while True:
    print('')
    # input from User
    roll_input = input('Roll Dice!: ').lower()
    if roll_input == 'done':
        break
    else:
        show_results()
