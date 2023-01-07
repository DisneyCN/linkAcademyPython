import functools

class Produs:
    count= 1
    def __init__(self,name,description, price):
        self.__id = Produs.count
        Produs.count += 1
        self.__name = name
        self.__description = description
        self.__price = price
        
    def __str__(self):
        return f"Produs no. {self.id}"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def price(self):
        return self.__price
    
    
    @name.setter
    def setName(self,name):
        if not isinstance(name,str):
            raise TypeError('Incorrect value')
        if len(name) < 3:
            raise ValueError("It's too short")
        self.__name = name
        
    @description.setter
    def setDescription(self,description):
        if not isinstance(description,str):
            raise TypeError('Incorrect value')
        if len(description) < 10:
            raise ValueError("It's too short")
        self.__description = description
        
    @price.setter
    def setPrice(self,price):
        if not isinstance(price,float):
            raise TypeError('Incorrect value')
        if price <=0:
            raise ValueError("It's too cheap")
        self.__price = price

    def __eq__(self, __o: object) -> bool:
        return self.id==__o.id and self.description==__o.description and self.name==__o.name 

class Blugi(Produs):
    pass


class Command:
    count=0
    def __init__(self,*prodList):
        self.__id = Command.count
        Command.count += 1
        self.__prodList = list(prodList)

    
    @property
    def prodList(self):
        return self.__prodList
    
    @prodList.setter
    def setProdList(self,prodList):
        self.__prodList = prodList
        
    def __iadd__(self,other):
        self.__prodList.append(other)
        return self
    
    def __isub__(self,other):
        self.__prodList.pop(other)

    def __str__(self):
        return f'List : {self.__prodList}'
    
    def __int__(self):
        a = list(map(lambda x: x.price,self.__prodList))
        return functools.reduce(lambda x,y: x + y,a)
    
    def transport(self):
        if int(self) > 130:
            return "Free"
        else:
            return "Pay"
    
if __name__ == '__main__':
    Prod1=Produs('Cloth',"Comfortable for gym",120)
    Prod2=Produs('Shoes',"For comfortable running",140)
    c1 = Command(Prod1)
    c1 += Prod2
    print(c1.transport())