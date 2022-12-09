# Vehicle class definition
class Vehicle(object):
    type = "car" 
    wheels = 4
    def getCarAtr(self, mark, year):
        self.mark = mark
        self.year = year

# Driver class definition
class Driver(object):
    type = "Person"
    def getName(self, name):
        self.name = name
    
# Info card class definition
class infoCard(Driver,Vehicle):
    type = "Info card "
    def __init__(self,name,mark,year):
        super().getName(name)
        super().getCarAtr(mark, year)
    def __str__(self):
        return 'info card: \n{self.name} drive {self.mark} produced in {self.year} year'.format(self=self)

# Create info card for diver Jim     
Jim = infoCard("Jim", "Ford",  1995)
print(Jim)
# Create info card for diver Kansas
Kansas = infoCard("Kansas", "BMW", 2005)
print(Kansas)





    
            
