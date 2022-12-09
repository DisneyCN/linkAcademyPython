# odd = []
# even = []
# try:
#     a = [int(item) for item in input("Enter the list items : ").split()]
#     for item in a:
#         if item % 2 == 0:
#             even.append(item) 
#         elif item % 2 == 1:
#             odd.append(item)
#     print('Even :\n',even)
#     print('Odd :\n',odd)
# except:
#     print('Enter corect value')
    

# try:
#     a = [int(item) for item in input("Enter the list items : ").split()]
#     odd = [item for item in a if item % 2]
#     even = [item for item in a if item % 2 == 0]
#     print('Even :\n',even)
#     print('Odd :\n',odd)
# except:
#     print('Enter corect value')


#Palindrom
# word = input('Enter a word :')
# def isPalindrom(x):
#     return x == x[::-1]
# print(isPalindrom(word))

#Dictionar 
# dict = {"class": {
#     "student": {
#         "name": "Mihai",
#         "marks": {
#             "physics": 70,
#             "history": 80
#         }
#     }
# }
# }
# print(dict["class"]['student']['marks']['history'])

# dict = {
#     'emp1':{'name':"George",
#             "salary":7500},
#     'emp2':{'name':"Mihai",
#             "salary":8000},
#     'emp3':{'name':"Andrei",
#             "salary":6500}
# }
# for emp in len(dict)-1:
#     for date in len(dict[2])-1:
#         if dict[emp][date] =='Andrei':
#             print("Andrei")

marks = {
    1 : 'sad',
    2 : 'ok',
    (3,4): 'not bad',
    (5,6) : "excelent"
}
grade = int(input('Grade ? '))
try:
    print(marks[grade])
except KeyError:
    print('Enter valid grade')