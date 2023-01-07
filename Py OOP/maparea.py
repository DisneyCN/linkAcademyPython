import functools
col = [1,2,3,4,5,6,7,8,9,10,11,12]

def func(x):
    return x**2 

print(list(map(func,col)))

def func(x):
    return not (x % 2) 


print(list(filter(func,col)))

def func(x,y):
    return str(x) + str(y)
print(functools.reduce(lambda x, y: str(x) + str(y),col))

