"""responsible for enforcement of all rules on a valid math problem"""
import string
import bodmas

def parse(input_string):
    """:returns a list of operands and a list of operations in the order they appear"""
    # preprocessing steps: remove all whitespace
    input_string.translate({ord(c): None for c in string.whitespace})

    nums, ops = split(input_string, bodmas.supported_operations.keys())
    return nums, ops


def split(string, delimiters):
    '''takes a string and list of delimiters and returns a list of numbers and list delimiters
    in the order in which they occurred'''
    numbers = [0]
    last_position = 0
    operations_in_order = []

    if string[0] == '+' or string[0] == '-':
        operations_in_order.append(string[0])
        string = string[1:]
    else:
        operations_in_order.append('+')

    for i in range(len(string)):
        if string[i] in delimiters:
            numbers.append(int(string[last_position:i]))
            operations_in_order.append(string[i])
            last_position = i + 1
        elif i == len(string) - 1:
            numbers.append(int(string[last_position:]))

    return numbers, operations_in_order
