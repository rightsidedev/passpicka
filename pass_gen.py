'''
Written by Mandy Kopelke for CSB2019 Assignment 1

Function to generate a random password
INPUT: 
    lenpass = length of password to be generated
    num_special = number of special characters to include in the password
    num_nums = number of numbers to include in the password
OUTPUT:
    Password of the requested length, made up using the supplied recipe
'''
import random

# This passes in a default value in case of the user not inputting a character
# get_random_char(num_special=4) 

def gen_random_char(lenpass=18,num_special=3,num_nums=5):
    newpass = []
    actual_len = 0
    CHARS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    NUMS = ['0','1','2','3','4','5','6','7','8','9']
    SPECIAL = ['!','@','#','$','%','^','&']
    num_chars = lenpass - num_special - num_nums # calculate number of alpha chars to include
    num_upper = random.choice(range(1,num_chars)) # calculate random number of alpha chars to convert to uppercase
    num_lower = num_chars - num_upper # calculate remaining number of alpha chars to keep in lowercase

    '''
    # Print values to ensure recipe is correctly generated
    print(f'Number of chars: {num_chars}')
    print(f'Number of uppercase: {num_upper}')
    print(f'Number of lowercase: {num_lower}')
    print(f'Number of nums: {num_nums}')
    print(f'Number of special: {num_special}')
    print(f'Total length of password: {lenpass}')
    '''
    '''
    Append correct number of each character type to newpass list
    '''
    for i in range(num_upper): # generate and append uppercase chars
        newpass.append((random.choice(CHARS)).upper()) 
        actual_len += 1
    print(f'num_upper = {num_upper}, actual_len = {actual_len}')
    for i in range(num_lower): # generate and append lowercase chars
        newpass.append(random.choice(CHARS)) 
        actual_len += 1
    print(f'num_lower = {num_lower}, actual_len = {actual_len}')
    for i in range(num_special): # generate and append special characters
        newpass.append(random.choice(SPECIAL)) 
        actual_len += 1
    print(f'num_special = {num_special}, actual_len = {actual_len}')
    for i in range(num_nums): # generate and append number characters
        newpass.append(random.choice(NUMS)) 
        actual_len += 1
    print(f'num_nums = {num_nums}, actual_len = {actual_len}')
    random.shuffle(newpass) # shuffle the list to ensure random order
    outpass = "".join(newpass) # create password by converting list to a string
    print(f'actual_len: {actual_len}')
    return(outpass)

'''
MAIN
'''
newpass = gen_random_char(15,2,)
print(f'Password is: {newpass}')