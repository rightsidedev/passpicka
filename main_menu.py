'''
Written by Mandy Kopelke for CSB2019 Assignment 1

Terminal Application: Password Manager
This is the main controlling module for the application.
It displays the main menu offering the following options:
(R) RECALL existing password
(N) Generate NEW password
(U) UPDATE existing password
(D) DELETE existing password
(X) EXIT
Then processes the appropriate functionality, requesting user input as required, and outputting messages to ensure the user understands what is happening.
'''
# Standard library imports
from time import sleep
import os
import json
import pyperclip #need to run pip install pyperclip
from datetime import datetime
import random

# custom module imports - written as part of the password manager application
from validate_recipe import get_num_nums
from validate_recipe import get_num_special
from validate_recipe import get_pass_length

"""
Function to clear screen output
Note! that this function may not work on all platforms
"""
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

"""
Function to check the password file exists
IN:     pass_file - name of the file to check (in same dir as code)
OUT:    True if ctrl_exists; False if it does not
"""
def pass_file_exists(pass_file):
    return os.path.exists(pass_file)

"""
Function to backup the password file
IN:     passfile - name of the file to check (in same dir as code)
OUT:    
"""
def backup_file(pass_file):
    backup_success = False
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    # print("date and time =", dt_string)
    archive_file = pass_file.strip('json')
    archive_file += timestamp
    command = 'cp '
    command += pass_file
    command += ' '
    command += archive_file
    # print(f'command is: {command}')
    cmd_success = os.system(command)
    if cmd_success == 0:
        print(f'\nBackup file: {archive_file} successfully created')
        backup_success = True   
    else:
        print(f'CRITICAL FAILURE: Cannot create backup file, Exiting application...')
        sleep(2)
    return(backup_success)

"""
Function to copy text to the clipboard
IN:     password: password to be copied to the clipboard
OUT:    
"""
def copy_to_clip(password):
    pyperclip.copy(password)

"""
Function to find and return a password from the password file
IN:     passfile: name of the password file (in same dir as code)
        inpassname: id(name) of the password being searched for
OUT:    rtnpassword: password if found, the text 'blank' if not found
        passfound: True if password exists in the file; False if it does not
"""
def find_password(pass_file, in_pass_name):
    find_password_success = False
    pass_found = False
    rtn_password = 'blank'
    try:
        with open(pass_file,'r') as pass_file:
            pass_data = json.load(pass_file)
            for pass_name,password in pass_data.items():
                if pass_name == in_pass_name:
                    pass_found = True
                    rtn_password = password
                    break
        find_password_success = True
    except:
        print(f'CRITICAL FAILURE: Cannot process password file, Exiting application...')
    return(rtn_password,pass_found,find_password_success)

"""
Function to request user input: id of the password and validate against the password name rules:
1. Must be > 5 characters long
2. Can only contain upper and lower case alphabet and fullstops
IN:     none (reads user input)  
OUT:    pass_name - the validated password name
"""
def in_pass_name():
    pass_invalid = True
    while pass_invalid:
        pass_name = input('\nPlease enter the name for the password\nPassword name must be minimum 5 characters long and contain only: a..z A..Z and fullstops.\n\nEnter password name> ')
        # Validate Password Name against required criteria
        if len(pass_name) < 5:
            print('Password name must be at least 5 characters long')
            sleep(2)
        else:
            letter_valid = True
            for letter in pass_name:
                if not letter.isalpha():
                    if not letter == '.':
                        # letter is not valid
                        letter_valid = False
                        break
                else: # letter is alpha
                    letter_upper = letter.upper()
                    if not letter_upper >= 'A' and letter_upper <= 'Z':
                        # letter is alpha but not valid
                        letter_valid = False
                        break
            
            if letter_valid == False: # stop validation processing at the first letter that is invalid, and request new valid input 
                print(f'Invalid name: password name can only contain letters a..z A..Z and fullstops')
                sleep(2)
            else: # all letters are valid
                pass_invalid = False
    return(pass_name)

"""
Function to update a password in the password file
IN:     passfile: name of the password file (in same dir as code)
        inpassname: id(name) of the password being searched for
        newpass: new password to allocate to the password id(name)
OUT:    
"""
def update_pass_file(pass_file, in_pass_name, new_pass):
    try:
        update_pass_file_success = True
        with open(pass_file,'r') as pass_file_in:
            pass_data = json.load(pass_file_in)
            pass_data[in_pass_name] = new_pass

        with open(pass_file,'w') as pass_file_in:
            json.dump(pass_data, pass_file_in)
    except:
        print(f'CRITICAL FAILURE: An internal error occurred processing the password file')
        update_pass_file_success = False
    return(update_pass_file_success)

def delete_from_pass_file(pass_file, in_pass_name):
    try:
        delete_pass_file_success = True
        with open(pass_file,'r') as pass_file_in:
            pass_data = json.load(pass_file_in)
            del pass_data[in_pass_name]

        with open(pass_file,'w') as pass_file_in:
            json.dump(pass_data, pass_file_in)
    except:
        print(f'CRITICAL ERROR: An internal error occurred processing the password file')
        delete_pass_file_success = False
    return(delete_pass_file_success)
        

"""
Function to RECALL an existing password
IN:     passfile: name of the password file (in same dir as code)
OUT:    
"""
def recall_pass(pass_file):
    pass_name = in_pass_name() # Request user to enter the password id to search for
    rtn_password,pass_found,find_password_success = find_password(pass_file, pass_name) # find password in password file
    if find_password_success:
        if pass_found == True: # test whether password has been found in the password file
            copy_to_clip(rtn_password) # copy the password to the clipboard
            print(f'Password: {rtn_password}')
            print(f'The password has been copied to the clipboard')
            input('Press any key to continue...')
        else:
            print(f'Password not found')
            sleep(2)
    return(find_password_success)

'''
Function to generate a random password
INPUT: 
    lenpass = length of password to be generated
    num_special = number of special characters to include in the password
    num_nums = number of numbers to include in the password
OUTPUT:
    Password of the requested length, made up using the supplied recipe
'''

# This passes in a default value in case of the user not inputting a character
# get_random_char(num_special=4) 

def gen_pass(len_pass, num_nums, num_special):
    new_pass = []
    actual_len = 0
    CHARS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    NUMS = ['0','1','2','3','4','5','6','7','8','9']
    SPECIAL = ['!','@','#','$','%','^','&']
    num_chars = len_pass - num_special - num_nums # calculate number of alpha chars to include
    # Now calculate how many upper case and lower case alphas to include
    if num_chars == 0: # no alphas to be included
        num_upper = 0
        num_lower = 0
    elif num_chars == 1: # only 1 alpha to be included
        num_upper = 1
        num_lower = 0
    else: # more than 1 alpha, so random generate num uppercases to be included
        num_upper = random.choice(range(1,num_chars)) # calculate random number of alpha chars to convert to uppercase
        if num_chars == num_upper: # ie: no positions left to be lower case
            num_lower = 0
        else: # calc num chars to be converted to lowercase
            num_lower = num_chars - num_upper # calculate remaining number of alpha chars to keep in lowercase   

    '''
    Append correct number of each character type to newpass list
    Commented out print statements included here for testing purposes
    '''
    if num_upper > 0:
        for i in range(num_upper): # generate and append uppercase chars
            new_pass.append((random.choice(CHARS)).upper()) 
            actual_len += 1
    # print(f'num_upper = {num_upper}, actual_len = {actual_len}')
    if num_lower > 0:
        for i in range(num_lower): # generate and append lowercase chars
            new_pass.append(random.choice(CHARS)) 
            actual_len += 1
    # print(f'num_lower = {num_lower}, actual_len = {actual_len}')
    if num_special > 0:
        for i in range(num_special): # generate and append special characters
            new_pass.append(random.choice(SPECIAL)) 
            actual_len += 1
    # print(f'num_special = {num_special}, actual_len = {actual_len}')
    if num_nums > 0:
        for i in range(num_nums): # generate and append number characters
            new_pass.append(random.choice(NUMS)) 
            actual_len += 1
    # print(f'num_nums = {num_nums}, actual_len = {actual_len}')
    random.shuffle(new_pass) # shuffle the list to ensure random order
    out_pass = "".join(new_pass) # create password by converting list to a string
    # print(f'actual_len: {actual_len}')
    return(out_pass)


"""
Function to UPDATE an existing password
"""
def update_pass():
    update_pass_success = False
    pass_name = in_pass_name() # Request user to enter the password id to search for
    rtn_password,pass_found,find_password_success = find_password(pass_file, pass_name) # find password in password file
    if pass_found: # test whether password has been found in the password file
        backup_success = backup_file(pass_file) # backup the password file
        if backup_success:
            len_pass = get_pass_length()
            num_nums = get_num_nums(len_pass)
            num_special = get_num_special(len_pass, num_nums)
            new_pass = gen_pass(len_pass, num_nums, num_special) # generate the new password
            upd_file_success = update_pass_file(pass_file,pass_name,new_pass) # update the password file
            if upd_file_success:
                copy_to_clip(new_pass) # copy the password to the clipboard
                update_pass_success = True
                print(f'Password: {new_pass}')
                print(f'The password has been copied to the clipboard')
                input('Press any key to continue...')
    else:
        update_pass_success = True #indicating that process completed as expected
        print(f'Password not found')
        sleep(2)
    return(update_pass_success)

"""
Function to create a NEW password
"""
def create_new_pass():
    create_pass_success = False
    pass_name = in_pass_name() # request user to enter the password name
    rtn_password,pass_found,find_password_success = find_password(pass_file, pass_name) # check whether password already exists
    if pass_found: # password name exists - display message, drop back to main menu
        create_pass_success = True #behavior is as expected
        print(f'A password with that name ({pass_name}) already exists')
        sleep(2)
    else: # password name does not exist, therefore can create one with that name
        len_pass = get_pass_length()
        num_nums = get_num_nums(len_pass)
        num_special = get_num_special(len_pass, num_nums)
        backup_success = backup_file(pass_file) # backup the password file
        if backup_success:
            new_pass = gen_pass(len_pass, num_nums, num_special)
            upd_file_success = update_pass_file(pass_file,pass_name,new_pass) # update the password file
            if upd_file_success:
                copy_to_clip(new_pass) # copy the password to the clipboard
                create_pass_success = True
                print(f'\nPassword: {new_pass}')
                print(f'The password has been copied to the clipboard')
                input('Press any key to continue...')
    return(create_pass_success)

"""
Function to DELETE an existing password
"""
def delete_pass():
    delete_pass_success = False
    pass_name = in_pass_name() # Request user to enter the password id to search for
    rtn_password,pass_found,find_password_success = find_password(pass_file, pass_name) # find password in password file
    if pass_found: # test whether password has been found in the password file
        backup_success = backup_file(pass_file) # backup the password file, if successful:
        if backup_success:
            delete_from_pass_file(pass_file,pass_name) # update the password file
            delete_pass_success = True
            print(f'The password identified by {pass_name} has been deleted')
            input('Press any key to continue...')
    else:
        delete_pass_success = True 
        print(f'Password not found')
        sleep(2)
    return(delete_pass_success)

"""
Function to display main menu
"""
def show_menu():
    valid_options=['r','R','n','N','u','U','d','D','x','X']
    while True:
        clear()
        print('Password Manager Program\n')
        print('(R) RECALL existing password')
        print('(N) Generate NEW password')
        print('(U) UPDATE existing password')
        print('(D) DELETE existing password')
        print('(X) EXIT')
        user_choice = input('\nPlease Enter an option R,N,U,D,X: ')
        if user_choice in valid_options:
            user_choice = user_choice.upper()
            if user_choice == 'R':
                find_pass_success = recall_pass(pass_file)
                if not find_pass_success:
                    break
            elif user_choice == 'N':
                create_pass_success = create_new_pass()
                if not create_pass_success:
                    break
            elif user_choice == 'U':
                update_pass_success = update_pass()
                if not update_pass_success:
                    break
            elif user_choice == 'D':
                delete_pass_success = delete_pass()
                if not delete_pass_success:
                    break
            elif user_choice == 'X':
                print('\nExiting... Thankyou for using the system')
                break
        else:
            print('\nIncorrect selection - try again')
            sleep(2)

##
## MAIN
##

"""
STEP1: Check the password file exists
"""
pass_file = "./data/passfile.json"
if (pass_file_exists(pass_file)):
    show_menu()
else:
    print('ERROR: Password file does not exist - please refer to the help manual')


