# l = list(input("Enter list elements: ").strip().split(','))
# # Ex 1
# def onlyNumber(list):
#     for item in list:
#         try:
#             yield int(item)
#         except ValueError:    
#             pass
# l = list(onlyNumber(l))
# print( "Maximum value in list is ", max(l), "\nMinimum value in list is ", min(l))
# # Ex 2
# def check_if_x_exist(x, lst): 
#         return  x in lst
# print(check_if_x_exist(input("Enter value : "),l))
# # Ex 3
# def anagram(s1, s2):
#     return set(s1) == set(s2)
# def palindrom(s1, s2):
#     return s1 == s2[::-1]
# print(anagram(input("Enter list 1 elements: "),input("Enter list 2 elements: ")))
# print(palindrom(input("Enter list 1 elements: "),input("Enter list 2 elements")
# # Ex 4
def render(x=5,y=5):
    for i in range(x):
        for j in range(y):
            print("#",end="")
        print()
render()
