import operator
import re 

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
} 
def operation(nr1,op,nr2):
    return ops[op](int(nr1),int(nr2))

def calculator(x):
    check = re.match(r'([0-9]+)([(+*-/)])([0-9]+)', x, re.I)
    if check:
        n1,op,n2 = check.groups()
        with open('ieşire.txt', 'a') as f_write:
            f_write.write(f'{n1}{op}{n2}={operation(n1,op,n2)}\n')
    
    
with open(r'expresii.txt', "r") as f_read:
    list_ = list(f_read.readlines()) 
    
for item in list_:
    calculator(item) 

