import mysql.connector



def login_or_register():
    for i in range(len(data)):
        if login in data[i]:
            password = input('Passworld - ')
            sign(password)
            break
    
    return
    create = input('Login not found. Create a new account? (Y/N) ')
    if create == 'Y':
        password = input('Create passworld - ')
        register(password)    
    elif create == 'N':
        print('Bye!')
    else:
        print('Invalid input.')

def sign(x):
    result = ''

    for i in range(len(data)):
        if x in data[i]:
            result = 'You are logged in.'
            break
    
    if result  == '':
        print('Invalid password.')
        login_or_register()
    else:
        print(result)

def register(password):
    cursor.execute('INSERT INTO logins (login, passworld) VALUES ({}, {})'.format(login, password))
    con.commit()
    print('Successful registration!')
    
login = input('Login - ')

con = mysql.connector.connect(host='localhost',
                                database='logins',
                                user='south',
                                password='21199')

cursor = con.cursor()

cursor.execute('SELECT * FROM logins')
data = cursor.fetchall()

login_or_register()

cursor.close()
