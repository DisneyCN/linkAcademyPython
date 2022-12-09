def suma():
    global sum, x
    try:
        sum += int(x)
        x = input('Enter number ')
    except ValueError:
        pass
    
x = input('Enter number ')
sum = 0
while True:
    if x.isnumeric():
        suma()
    else: 
        print(f'Sum is {sum}')
        x = input('Enter number ')
        suma = 0
        continue
        