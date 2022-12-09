# x = 10
# y = 4

# def my_fst_function():
#     r = str(x) * y
#     return r

# print(my_fst_function())

# def f_one():
#     pass
# def f_two():
#     pass
# def f_three(f):
#     print(id(f))
# t = (f_one, f_two, f_three)
# for i in t:
#     print("Function:", i.__name__)
#     print("Object is instance of object:", isinstance(i, object))
#     print("Id:", id(i))    
# f_three(f_one)

# print(type(lambda x, y: x + y))

# def filter_func(x):
#     if x % 2:
#         return True
#     else:
#         return False
 
# numbers= list(range(0,10))
# print(list(filter(filter_func, numbers)))
# print(list(filter(lambda x: x % 2, numbers)))

# s = "String"
# print(sorted(s, key=lambda x: x))

# s = "String"
# print(sorted(s, key=lambda x: x))

# # cities =[("New York",10001),
#        ("Paris",75000), 
#        ("Moscow", 101000),
#        ("Tokyo",100000)]
# cities=sorted(cities, key= lambda x: x[1])
# print(cities)

# def second_function():
#     print('second function')
# def change_to_second_function(func):
#     return second_function
# @change_to_second_function
# def first_function():
#     print('first_function')
# print(first_function())


# def decorator(func):
#     # Funcţia locală (imbricată)
#     def inner_function(l):
#         return [func(el) for el in l]
#     return inner_function
# @decorator
# def all_caps(s):
#     return s.upper()
 
# cities= ['london', 'moscow', 'new york']
# print(all_caps(cities))



# def addition(func):
#     def do_addition(a,b):
#         print("Sum : {} + {} = {}".format(a,b,a+b))
#         return func(a,b)
#     return do_addition

# def substraction(func1):
#     def do_substraction(a,b):
#         print("Dif : {} - {} = {}".format(a,b,a-b))
#         return func1(a,b)
#     return do_substraction

# @addition
# @substraction
# def operations(a,b):
#     print('Oke')

# print(operations(10,5))

# def addition(func):
#       def wrapper_function(a,b):
#             print("Addition result is {}".format(a+b))
#             return func(a,b)
#       return wrapper_function
 
# def subtraction(func):
#      def wrapper_function(a,b):
#              print("Subtraction result is {}".format(a-b))
#              return func(a,b)
#      return wrapper_function
 
# @addition
# @subtraction
# def operations(a,b):
#       print("Passed numbers are: {} and {}".format(a,b))
 
# operations(9, 15)

# cities = ["new york", "london", "moscow"]
# cities_iterator = iter(cities)
# print(next(cities_iterator))
# print(next(cities_iterator))
# print(next(cities_iterator))
# print(next(cities_iterator))

# cities = ["new york", "london", "moscow"]
# cities_iterator = iter(cities)
# while cities_iterator:
#     try:
#         print(next(cities_iterator))
#     except StopIteration:
#         break

# def even_numbers(a):
#     for x in range(a):
#         if x % 2==0:
#             yield x
# for e in even_numbers(10):
#     print(e,end=', ')

"""
Scrieţi o funcţie generatoare care, ca parametru, primeşte 
calea până la fişierul arbitrat şi îl citeşte linie cu linie."""

def x2(a):   
   for x in range(a):
       yield x*x

print(list(x2(4)))