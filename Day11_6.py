my_username = 'admin'
my_password = '12345'

username = input('Enter username: ')
password = input('Enter password: ')

if username == my_username and password == my_password:
    print('Login Success!')
    
else:
    if username != my_username and password != my_password:
        print('Both username and password incorrect')
    elif username != my_username and password == my_password:
        print('Username Incorrect!')
    else:
        print('Password Incorrect!')