# Password Management Terminal Application



# Software Development Plan

#### Author: Mandy Kopelke, Final Draft: 10th August 2019



### Statement of Purpose and Scope

In an age where data breaches are an everyday occurrence, it is the responsibilty of every person who does anything online, to understand the implications of password security.  By implementing secure password practices, people will have the best opportunity to protect themselves and their personal data. 

One of the key arguments that people use for lax password practices is that it is just too difficult to remember complicated and unique passwords. This results in simple, easily crackable passwords being used and the reuse of passwords across different systems. Both of these practices are an open invitation to hackers to exploit the users' accounts.

Gary Davis<sup>1</sup> at McAfee suggests some recommended guidelines for passwords:

1. Create strong passwords and avoid common and easy to crack passwords like "12345" for example.
2. Use unique passwords for each account
3. Use a password manager

This password management terminal application will address this problem through a menu based system, which can be run at the command prompt in the Terminal app (MacOS Only). Passwords will be saved with a unique identifier created by the user, for example a website name. Menu options offered will be:

- recall an existing password
- generate a new password
- update an exisiting password
- delete a password
- exit

Additional functionality includes:

- allow the user to define the "recipe" for the password generation or accept the default recipe
- automatically copy the generated password to the clipboard (MacOS Only)

Functionality outside the scope of this project may be added at later stage:

- enter a 'master password' to access the main menu of the application.
- store the passwords in an encrypted format, in a data file held locally

The password management application will be useful for any MacOS user who would like to implement more secure password practices for their personal use. It should be noted however that since the password file is stored locally, should the machine be lost or corrupted the user would lose all of the stored passwords. It is vital that an appropriate backup procedure is implemented to protext from data loss.

It should also be noted that this application has been written as a college assignment, with a remit of developing a basic terminal application to develop knowledge of coding and development practices. It may not therefore reflect best password management practice.

##Features
### 1. Main Menu - Application Control System

The password application management system is run at the command line in the Terminal app. When initiated, it first checks that the password file exists. If it is found, the main menu is shown, allowing the user to select an action from:

(R) RECALL an existing password

(N) generate a NEW password

(U) UPDATE an exisiting password

(D) DELETE a password

(X) EXIT

An on screen prompt will be shown (Please Enter an option R,N,U,D,X:), requesting that the user enter a choice.

Input will then be validated to ensure only R,N,U,D or X is accepted. Should an invalid key choice be entered by the user, an error message will be briefly displayed before the screen is cleared and the menu reshown.

### 2. RECALL Password

This option will allow the user to recall a previously saved password. Application code is reused across multiple features for efficiency. 

The user will first be required to enter the unique password name. This will then be used to locate and  identify the password in the password file. Should the password not be found, an error message will be briefly displayed on the screen and the user will be returned to the main menu to try again.

When the password is found, it will be displayed on the screen and copied to the clipboard. A message will inform the user that the password is in the clipboard, and "Press any key to continue..." will be displayed on screen to pause further action until the user is ready to continue.

NOTE: The password is displayed on the screen to enable a user to type it directly into another device. This broadens the use of the application so that it can be used outside of the clipboard functionality. If the password was hidden as perhaps more secure practice, the functionality would be limited to the device on which the application is being run.

### 3. UPDATE Existing Password

The update option enables the user to update the password stored against a password name. The first step is to follow the same process as the Recall Password feature, to find an existing password to update.

Once found the password file is backed up with a date/time stamp to provide a rollback position if required. If the backup process produces any error, the user will be notified that a critical failure has occurred, and the application will exit.

On successful completion of the backup, the user will be asked to input the recipe to use for the new password. Validation at this point ensures that the password is between 11 and 30 characters long. The user can also select the number of numbers and special characters to be included in the generation process. The remaining characters default to alphabetic between 'a' to 'z', with a random number of those being converted to upper case. After the password is generated to the recipe stipulation, the characters are randomly shuffled together.

The new password is then updated in the password file, again with a critical failure error displayed to the user if required followed by the application exit. If the password file is updated successfully, the same process in the password recall feature is used, to show the use the password, copy to the clipboard and display user messages, including the "Press any key to continue..." functionality.

### 4. Generate NEW Password

Generating a new password uses mostly existing functionality from already described features. Initially the user enters a password name. Using a similar process from recall password the application establishes whether the password name already exists. If it does, the user is presented with an error (as the password name must be unique) and is returned to the main menu.

If the password name is new and unique then the password file is backed up, using the same process as the update password feature.

Generating the new password is also the same process used in update password, as is the update password file process.

### 5. DELETE Existing Password

Deleting an existing password completely reuses existing functionality. Initially requesting the password name and finding the password in the password file. If the password is found, the password file is backed up. Once a backup has been successfully created, the password is deleted from the main password file. User messages are displayed at all key steps as per previous processes.

##User Interaction and Experience

The user will understand the initial application installation process, through the implementation and user guide. This will detail installation instructions and how to start the application step by step.

The features themselves are self explanatory once the application is started:

- User messages are displayed on the screen at each stage, so that the user understands the process. More specific information on using each feature, is described in the Features section of this document. 
- Similarly error handling is explained in the  Features section. 

##Control Flow Diagram

Note that in the flow diagram, process boxes are reused across functions. For example the "copy to clipboard" and the "backup/archive password file" is the same function used by all modules. They have been grouped by module for simplicity. 

(./passwordapp.svg)

##Implementation Plan

| Phase          | Task                                                  | Priority* | Deadline |
| -------------- | ----------------------------------------------------- | --------- | -------- |
| Planning       | Define purpose & scope                                | H         | 04/08/19 |
|                | Describe features                                     | L         | 08/08/19 |
|                | Describe user interaction and experience              | L         | 08/08/19 |
|                | Develop control flow diagram                          | H         | 05/08/19 |
|                | Define implementation plan                            | M         | 05/08/19 |
| Development    | Develop menu                                          | M         | 05/08/19 |
|                | Develop recall password                               | M         | 05/08/19 |
|                | Develop update password                               | M         | 06/08/19 |
|                | Develop generate new password                         | M         | 06/08/19 |
|                | Develop delete password                               | M         | 06/08/19 |
|                | Audit development style conventions                   | L         | 06/08/19 |
| Testing        | Test menu                                             | M         | 07/08/19 |
|                | Test recall password                                  | M         | 07/08/19 |
|                | Test update password                                  | M         | 07/08/19 |
|                | Test generate new password                            | M         | 07/08/19 |
|                | Test delete password                                  | M         | 07/08/19 |
|                | Develop test case 1                                   | L         | 08/08/19 |
|                | Develop test case 2                                   | L         | 08/08/19 |
| Implementation | Prepare application for implementation                | L         | 09/08/19 |
|                | Prepare all documentation for implementation          | L         | 09/08/19 |
|                | Prepare implementation help file                      | M         | 09/08/19 |
| Final Delivery | Deliver final application complete with documentation | H         | 10/08/19 |

Priority: (H) High; (M) Medium; (L) Low

Note: Two status reports will be produced during the course of this project. They can be found in the GitHub repository for this project in: development-log.md

###Overall Project Plan in Trello

(./trelloplan.png)

#### Individual Task Breakdown for "generate NEW password module"

(./trelloplan-deets.png)

## Help File

This password amangement application is written and tested on MacOS and requires access to the terminal application.

1. Copy the main_menu program to the directory required (where you wish to store te application)

2. Launch the terminal application

3. Run the following commands to initialise an empty password file:

   mkdir data

   cd data

   touch passfile.json

   cd ..

4. The program is now ready to run using thew following command:
   .main_menu

#Application Process Flow

(./passwordapp.svg)

## Reference

<sup>1</sup>Gary Davis, McAfee "The Past, Present and Future of Password Security"
https://securingtomorrow.mcafee.com/consumer/consumer-threat-notices/security-world-password-day/