def calculate():
    if op in ['add','plus','+']:
        return a + b    
    elif op in ['sub','minus','-']:
        return a - b
    elif op in ['mul','*']:
        return a * b
    elif op in ['div','/']:
        return a / b

print('\t\bCalculator')
a = float(input('Enter first operand : '))
b = float(input('Enter second operand : '))
op = input('Choose operation : ')
print('Result is : ', calculate())
