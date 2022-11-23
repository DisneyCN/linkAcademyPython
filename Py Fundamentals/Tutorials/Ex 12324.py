# a=float(input('First: '))
# b=float(input('Second: '))
# print('Sum: ', a+b)


# def my_function(x):
#     print(x.replace('o','0'))

# a=input('Enter some words : ')
# my_function(a)   


# Sum = lambda a, b: a + b
# a, b = map(int, input('Enter a and b : ').split())
# print(Sum(a,b))


# a, b = input('Enter two values : ').split()
# print('Sum is {} + {} + {} '.format(a,b,a+b))


# list_ = [int(list_) for list_ in input("Enter multiple value: ").split(",")]
# print('List ', list_)


add_value = lambda x, z: x+z
a, b = map(int, input('Enter a and b : ').split())
print("a  = {} \nb = {} ".format(a,b))
print(add_value(a,b))


# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# print(full_name('guido', 'van rossum'))


# lambda_example = (lambda x:
#     (x % 2 and 'odd' or 'even'))
# print(lambda_example(3))

# t1 = [int(t1) for t1 in input("Enter multiple value: ").split()]
# for item in t1 :
#     print(int(item+1), end = ' ')
    
    
'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''

# from operator import length_hint as le 

# list_ = [23,5,46,24,2,200,51]
# list_.append(62)
# list_1 = list_.copy()
# list_.clear()
# print(len(list_), " l2 : ", len(list_1))
# print('Second\'s list size : ', le(list_1))
# print(list_1.index(5))
# list_1.insert(1,25)
# print('Second list : ', list_1)
# list_1.pop(2)
# list_1.reverse()
# print('Second list : ', list_1)
# list_1.sort(reverse = True)
# print('Second list : ', list_1)

# def myFunc(e):
#   return len(e['car'])


# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myFunc)

# for item in cars:
#     print(item)
    
    
# class Book:
#   def __init__(self, name, author):
#     self.name = name
#     self.author = author

# b1 = Book('Be or not to be','Somebody')

# print(' {} released {}'.format(b1.author,b1.name))


