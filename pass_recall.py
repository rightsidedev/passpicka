from time import sleep
import os

"""
Function to clear screen output
"""
def clear():
## can name be unexpected value in else statement, for a system that doesn't use clear?
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

"""
Function to check the password file exists
IN: ctrl_file - name of the file to check (in same dir as code)
OUT: True if ctrl_exists; False if it does not
"""
def pass_file_exists(passfile):
    return os.path.exists(passfile)

"""
Function to request user input: Password Name
"""
def in_passname():
    pass_invalid = True
    while pass_invalid:
        passname = input('\nPlease enter the name for the password.\n Name must be minimum 5 characters long and contain \n only alphanumerics and fullstops:\n')
        #validate that passname is > 5 characters perhaps
        if len(passname) < 5:
            print('Password name must be at least 5 characters (alphnumerics and fullstops only)')
            sleep(2)
            # test for alpha's here
        else:
            pass_invalid = False
    return(passname)

"""
Function to find the password name in the password file 
IN: passfile - name of the file to check (in same dir as code)
OUT: True if password exists in the file; False if it does not
"""
def check_passfile(passfile, passname):
    passfound = False
    passdata = []
    with open(passfile,'r') as filedata:
        for line in filedata:
            if passname in line:
                passdata = line
                passfound = True
                break
    return(passdata,passfound)    

"""
Function to RECALL an existing password
"""
def recall_pass(passfile):
    passname = in_passname()
    # print(f'Pass name in recall_pass = {passname}')
    # sleep(2)
    passdata,passfound = check_passfile(passfile, passname)
    password = passdata.split(',')
    print(password[1])
    if passfound == True:

        sleep(4)
        #decrypt password
        #copy password to clipboard
        pass
    return("msgone")

    # read the password file and find the passname


"""
Function to Generate a NEW password
"""
def gen_pass():
    pass

"""
Function to UPDATE an existing password
"""
def update_pass():
    pass

"""
Function to DELETE an existing password
"""
def delete_pass():
    pass

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
                # print('Recalling Password...')
                # sleep(2)
                print(f'passfile: {passfile} in show_menu function')
                msg = recall_pass(passfile)
                print(msg)
                sleep(2)
            elif user_choice == 'N':
                print('Generating New Password...')
                sleep(2)
                gen_pass()
            elif user_choice == 'U':
                print('Updating Existing Password...')
                sleep(2)
                update_pass()
            elif user_choice == 'D':
                print('Deleting password...')
                sleep(2)
                delete_pass()
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
passfile = "passfile.txt"
if (pass_file_exists(passfile)):
    show_menu()
else:
    print('ERROR: Password file does not exist - please refer to the help manual')


