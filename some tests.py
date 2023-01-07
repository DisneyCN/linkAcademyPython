# def pow(func):
#         def wrapper(*args):       
#             newlist = list(args)
#         return list(item **2 for item in newlist)
#         return wrapper()
    

# @pow
# def sumOfElements(*args):
#     return "sum = " , sum(args)

# list = [int(item) for item in input("Enter the list items : ").split()]
# print(sumOfElements(list))

# nan = float('nan')
# print(bool(nan))
# print(nan)


def sumOfElements(*args):
    return sum(args)
print(sumOfElements(1,2,3,4))
