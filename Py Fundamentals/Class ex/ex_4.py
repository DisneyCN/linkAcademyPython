nr=int(input('Enter number : '))
try:
    print('Number\' is Even :', end=" ")
    if nr % 2 == 0 :
        print('True ')
    elif nr % 2 == 1:
        print('False ')
except ValueError:
    print('Try again')