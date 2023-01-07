class Engine:
    def __init__(self, series:str, power:float, mileage:int=0):
        self._series = series
        self._power = power
        self._mileage = mileage
        
    def __str__(self):
        return "Engine series: %s\npower : %f CP,\nmileage %d km"  % self.series,self.power,self.mileage
    
    def getSeries(self):    
        return self._series
    def getPower(self):
        return self._power
    def getMileage(self):
        return self._mileage
    
    @property
    def seria(self):
        return self._series
    @property
    def power(self):
        return self._power
    @property
    def miles(self):
        return self._mileage
    
    def __iadd__(self,km):
        if km > 0:
            self._mileage += km
        else :
            print('Enter valid mileage: %')
        return self
    
class BensingEngine(Engine):
    def __init__(self,series,power,mileage,consumptions):
        super().__init__(series,power,mileage)
        self._consumptions = consumptions
        
    def __str__(self):
        return f"Engine series: {self._series}\npower : {self._power} CP,\nmileage : {self._mileage} km \nconsumptions : {self._consumptions}"    

    
class ElectricEngine(Engine):
    def __init__(self,series,power,mileage,batery):
        super().__init__(series,power,mileage)
        self.batery = batery
    def __str__(self):
        return f"Engine series: {self._series}\npower : {self._power} CP,\nmileage : {self._mileage} km\nbatery: {self.batery}"
    
    
    
Tesla = ElectricEngine('awav',4.5,100,70)
Tesla += 50
print(Tesla)