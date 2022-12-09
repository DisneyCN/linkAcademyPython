user = {}
while True:
    user['gen']=input('introduceti genul m/f ')
    user['varsta']=int(input('introduceti varsta '))

    if user['varsta'] < 70 and ((user['gen'] == 'm' and user['varsta'] >= 18) or (user['gen'] == 'f' and user['varsta'] >= 16)):
        print('Access granted:')
        print(' " World secret "')
    else: 
        print('Access denied ')
        print(user)
