
# class Student: 
#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def check(self):
#         if int(self.age) <= 19:
#             return "This student study now"
#         else:
#             return "This student studed before"
#     def __str__(self):
#         return 'Student %s is %s years old \n' % (self.name, self.age)
            
# std1 = Student(input('Enter the student name : '), input('Enter his age : '))
# print(std1,std1.check())

#Ex 1
# class Calculator: 
#     def __init__(self,nr1,nr2):
#         self.nr1 = nr1
#         self.nr2 = nr2
#     def add(self):
#         return self.nr1 + self.nr2
#     def subtract(self):
#         return self.nr1 - self.nr2
#     def multiply(self):
#         return self.nr1 * self.nr2
#     def divide(self):
#         return self.nr1 / self.nr2
#     def equal(self):
#         return self.nr1 == self.nr2
#     def greaterThan(self):
#         return self.nr1 > self.nr2

# ans = Calculator(int(input('Enter first number : ')), int(input("Enter second number : ")))
# print("add", ans.add(), "subtract", ans.subtract(), "multiply", ans.multiply(), "divide", ans.divide)

#Ex 2
# import math
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show(self):
#         return str(self.x) + "," + str(self.y)
#     def move(self,newx,newy):
#         self.x = newx
#         self.y = newy
#     def setToOrigin(self):
#         self.move(0,0)
#     def distance(self, other):
#         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
# Point1 = Point(int(input('Enter x : ')), int(input('Enter y : ')))
# print("show ",Point1.show())
# Point1.setToOrigin()
# print("show after setToOrigin ",Point1.show())
# Point1.move(int(input('Enter new x : ')), int(input('Enter new y : ')))
# print("show after move ",Point1.show())
# Point2 = Point(int(input('Enter x : ')), int(input('Enter y : ')))
# print("distance", Point1.distance(Point2))


# Ex3
# class Account:
#     def __init__(self, balance = 0):
#         self.balance = balance
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("You don't have enough money")
#         else:
#             self.balance -= amount
#     def addMoney(self, money):
#         self.balance = self.balance + money
#     def showBalance(self):
#         return self.balance
# Pers1 = Account(int(input('Enter initial balance : ')))
# while True:
#     print("Select your option : \n1.Withdraw\n2.Add Money\n3.Show Balance\n4")
#     option = int(input("Enter your option : "))
#     if option == 1:
#         Pers1.withdraw(int(input("Enter amount : ")))
#     elif option == 2:
#         Pers1.addMoney(int(input("Enter amount : ")))
#     elif option == 3:
#         print("Your balance : ",Pers1.showBalance())
#     elif option == 4:
#         break



