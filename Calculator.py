#!/usr/bin/env python3
# A four function calculator
import parse
import bodmas


def display_help_message():
    print("I haven't done that yet \xBA Remind me to do that")


def main():
    print('======================Four Function Calculator=================================')
    print('version 1.1 ')
    print(' By Nathan Kamenchu\r\n')
    print('Enter a problem to evaluate\nTo close the application simply type: exit')
    print('To access the help type: help')
    while True:
        user_input = input('Problem: ')
        if user_input.lower() == 'help':
            display_help_message()
        elif user_input.lower() == 'exit':
            break
        else:
            # try:
            nums, ops = parse.parse(user_input)
            operations = []
            for i in ops:
                operations.append(bodmas.supported_operations[i])
            res = bodmas.determine_order_of_operation(nums, operations)
            print(res)
            # except Exception:
            #     print('Looks like your input had some errors. Please input a valid problem')
            #     if input('if you wish to see help type \'help\'\n').lower() == 'help':
            #         display_help_message()


if __name__ == '__main__':
    main()
