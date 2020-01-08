'''
Written by Mandy Kopelke for CSB2019 Assignment 1

Terminal Application: Password Manager
This module requests the user to input 3 values or accept the suggested defaults, then validates the inputs. These 3 values are used in the recipe to build the new password, generated in the main program module.

CALLING PROGRAM:    main_menu.py
INPUT 1 (len_pass): length of the password to be generated between 11..30, default 18
INPUT 2 (num_nums): number of numbers to be included in the password, between 0..len_pass, default 5
INPUT 3 (num_specials): number of special characters to be included in the password, 
        between 0..(len_pass - num_nums), default 3 (unless there are not 3 positions left - if this is the case the default is recalculated based on the number of positions left)

OUTPUT: len_pass, num_nums, num_specials as described above
'''

'''
Function to ask the user to input a value for the length of the password

OUTPUT: len_pass: length of the password to be generated
Validation: Password can be between 11..30 characters long, default = 18. Value entered must be an integer, or blank to set the default
'''
def get_pass_length():
    pass_length_invalid = True
    while pass_length_invalid:
        try:
            len_pass = input(
                '\nWhat length password should be generated (11..30)?\nJust press <RETURN> to accept the default of 18\n\nEnter password length > ')
            if not len_pass:
                len_pass = 18
            len_pass = int(len_pass)
            if not (len_pass > 10 and len_pass <= 30):
                print(
                    f'Password length ({len_pass}) must be between 11 and 30')
            else:
                pass_length_invalid = False
        except ValueError:
            print(f'Invalid value entered for length: {len_pass}')
    return(len_pass)

'''
Function to ask the user to input a value for the number of numbers to include in the password

OUTPUT: num_nums: number of numbers to be included
Validation: Entered value can be between 0 and the full length of the password. default = 5. Value entered must be an integer, or blank to set the default
'''
def get_num_nums(len_pass):
    num_nums_invalid = True
    while num_nums_invalid:
        try:
            num_nums = input(
                f'\nHow many numbers should be included in the password (0..{len_pass})?\nJust press <RETURN> to accept the default of 5\n\nEnter number of numbers > ')
            if not num_nums:
                num_nums = 5
            num_nums = int(num_nums)
            if not (num_nums >= 0 and num_nums <= len_pass):
                print(
                    f'Number of numbers included ({num_nums}) must be between 0 and {len_pass}')
            else:
                num_nums_invalid = False
        except ValueError:
            print(
                f'Invalid value entered for the number of numbers to be included: {num_nums}')
    return(num_nums)

'''
Function to ask the user to input a value for the number of special characters to include in the password

OUTPUT: num_specials: number of special characters to be included
Validation: Entered value can be between 0 and the remaining length of the password once the numbers have been deducted from the length. default = 3. default value is recalculated if there are not 3 remaining positions in the password. Value entered must be an integer, or blank to set the default
'''
def get_num_special(len_pass, num_nums):
    num_specials_invalid = True
    max_specials = len_pass - num_nums
    default_specials = 3
    while num_specials_invalid:
        try:
            if max_specials == 0:
                num_specials = 0
                break
            elif max_specials == 1:
                default_specials = 1
            elif max_specials == 2:
                default_specials = 2
            num_specials = input(
                f'\nHow many special characters should be included in the password (0..{max_specials})?\nJust press <RETURN> to accept the default of {default_specials}\n\nEnter number of Special Characters > ')
            if not num_specials:
                num_specials = default_specials
            num_specials = int(num_specials)
            if not (num_specials >= 0 and num_specials <= max_specials):
                print(
                    f'Number of special characters included ({num_specials}) must be between 0 and {max_specials}')
            else:
                num_specials_invalid = False
        except ValueError:
            print(
                f'Invalid value entered for number of special characters to include: {num_specials}')
    return(num_specials)

'''
Run and test the code:

len_pass = get_pass_length()
num_nums = get_num_nums(len_pass)
num_specials = get_num_special(len_pass, num_nums)

print(f'Length of password will be: {len_pass}')
print(f'Number of numbers included will be: {num_nums}')
print(f'Number of special characters included will be: {num_specials}')
'''
