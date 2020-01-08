'''
Written by Mandy Kopelke for CSB2019 Assignment 1

Function to hide a password display on the screen
INPUT: 
    1
OUTPUT:
    1
'''
def hide_pass(hide_on=True):
    newpass = "helloworld"
    if hide_on:
        display_pass = '*****'
    else:
        display_pass = newpass
    return(display_pass)

display_pass = hide_pass(False) 
print(f'Password is: {display_pass}')
