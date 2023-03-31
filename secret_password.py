password_file = open('secretPassword.txt')
secret_password = password_file.read()
print ('Enter your password.')
typed_password = input()

if typed_password == secret_password:
    print('Access granted')
else:
    print('Access denied')