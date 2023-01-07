# Create Marks class
class Marks:
    def __init__(self, object:str, mark:list):
        self.object = object
        self.mark = mark
    def __str__(self):
        return str(self.object) + " " + str(self.mark)


# Create Faculty class
class Faculty:
    def __init__(self, definition:str, adress:str):
        self.definition = definition
        self.adress = adress
        
    def __str__(self):
        return f'\nFaculty : \n Name - {self.definition} \n Adress - {self.adress}'
# Create Student class
class Student:
    def __init__(self, name:str, age:int, faculty:Faculty):
        self.name = setName(name)
        self.age = setAge(age)
        self.faculty = setFaculty
    def __str__(self):
        return f'Student : \n Name - {self.name} \n Age - {self.age} {self.faculty}'
    # Create setter for Name property
    def setName(self, name:str):
        if len(name) in range(3,20):
            self.name = name
    # Create getter for Name property
    def getName(self) -> str:
        return self.name
    # Create setter for Age property
    def setAge(self,age:int):
        if isinstance(age, int):
            if age in range(16,21):
                self.age = age
    # Create getter for Age property
    def getAge(self) -> int:
        return self.age
    # Create setter for Faculty property
    def setFaculty(self,faculty:Faculty):
        if isinstance(faculty, Faculty):
            self.faculty = faculty
    # Create getter for Faculty property
    def getFaculty(self) -> Faculty:
        return self.faculty
# Create Faculty object
computerSience = Faculty("Computer sience ", "Iasi")
# Create Student object
Std1 = Student(name="Tom", age=32, faculty=computerSience)
print(Std1)

