import mysql.connector



def login_or_register():
    for i in range(len(data)):
        if login in data[i]:
            passworld = input('Passworld - ')
            sign(passworld)
            break
    
    return
    create = input('Login not found. Create a new account? (Y/N) ')
    if create == 'Y':
        passworld = input('Create passworld - ')
        register(passworld)    
    elif create == 'N':
        print('Bye!')
    else:
        print('Invalid input.')

def sign(x):
    y = ''

    for i in range(len(data)):
        if x in data[i]:
            y = 'You are logged in.'
            break
    
    if y  == '':
        print('Invalid password.')
        login_or_register()
    else:
        print(y)

def register(x):
    cursor.execute('INSERT INTO logins (login, passworld) VALUES ({}, {})'.format(login, x))
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
