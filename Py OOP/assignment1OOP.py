class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number
    def getInfo(self):
        return f"Name : {self.name} \nAddress : {self.address} \nPhone : {self.phone} \nCourse : {self.course} \nIndex : {self.index_number} \n"
    
student1 = Student("John Benson", "High Park 36", "(507) 833-3567", "Geography", "123/007")
student2 = Student("Jessica Jones", "Low Street 15", "(604) 123-4567", "Computer Science", "456/012")
student3 = Student("Mark Quinn", "Middle Avenue 25", "(905) 456-7890", "Physics", "789/345")

print(student1.getInfo())
print(student2.getInfo())
print(student3.getInfo())

