""" 
Create a REPL which allows a user to 'log in'.

Please complete the sections in order. Create a working version of 5.1 before attempting 5.2, etc. This will make your life easier. You may also want to consider creating separate .py files for each version, so you can refer back to previous working versions.

5.1

Create a dictionary called profile

The profile should contain two key : value pairs with keys of username and password and values of your choosing. They will represent a username and password for a single user.

username - gandalfTheGrey
password - noneShallPass!
Do not create your profile with the user's username as the key and their password as the value as below:

'gandalfTheGrey':'noneShallPass'
Define a function called login() which will have three parameters for:

username_attempt
password_attempt
profile

If the values passed to the function for username_attempt and password_attempt match the values at the keys of username and password found in the profile, The login() function will return True.

If the credentials don't match those in the profile, the login() function will return False

Create variables for a username_attempt and password_attempt which will emulate a user's login attempt.

Pass the profile dictionary, username_attempt and password_attempt to login(). Use the boolean that is returned to tell the user whether or not their login attempt was successful.


 """


johnpaul = { 
    "username": 'jctansi',
    "password": "abc123"
}



def login_function(username_attempt, password_attempt, profile): #profile is an empty parameter until you call the function is called
        if username_attempt == profile['username'] and password_attempt == profile['password']:
            return True
        elif username_attempt != profile['username'] or password_attempt != profile['password']:
            return False


while True:
    username_attempt = input('Enter username: ')
    password_attempt = input('Enter password: ')
    if login_function(username_attempt, password_attempt, johnpaul):
        print(f"\n# Successful login! \n Welcome {username_attempt}")
        break
    else:
        print('\n# unsuccessful login. \nError! Your username or password was incorrect!')
        user_try = input('Would you like to try again? (y/n): ')
        if user_try =='y':
            continue # continue: python accesses the next statement then returns the loop to the beginning (starts all over)
        if user_try == 'n':
            break
        if user_try != 'y' or user_try != 'n':
            print('Invalid entry')
        continue
# else:
#     print('Goodbye')

           