profile = { 
    "username": 'jctansi',
    "password": "irxplg5S*;"
}


username_attempt = input('Enter username: ')
password_attempt = input('Enter password: ')



if username_attempt == profile['username'] and password_attempt == profile['password']:
    print(f'\n# Successful login. \nWelcome {username_attempt}!')
    #break
if username_attempt != profile['username'] or password_attempt != profile['password']:
    print(f'\n# unsuccessful login. \nYour username or password was incorrect.')
    user_try = input('Would you like to try again? (y/n): ')
    
    while user_try =='y':
        username_attempt = input('Enter username: ')
        password_attempt = input('Enter password: ')
        if username_attempt == profile['username'] and password_attempt == profile['password']:
            print(f'\n# Successful login. \nWelcome {username_attempt}!')
            break
        if username_attempt != profile['username'] or password_attempt != profile['password']:
            print(f'\n# unsuccessful login. \nYour username or password was incorrect.')
            user_try = input('Would you like to try again? (y/n): ')
            if user_try =='n':
                break

    if user_try =='n':
                print('Goodbye')
    
from userloginv1 import login_function
