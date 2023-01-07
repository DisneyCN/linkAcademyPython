# Vehicle class definition
# Vehicle constructor
class Vehicle:
    # Initializes the vehicle
    def __init__(self, brand:str, consumptions:float, mileage:float , fuel:float , maxFuel:float, expenses:float =0, fuelPrice:float =10):
        self.brand = brand # Marca
        self.consumptions = consumptions # Consumul
        self.mileage = mileage # Kilometri parcursi
        self.fuel = fuel # Combustibil
        self.maxFuel = maxFuel # Rezervor
        self.expenses = expenses # Suma cheltuita pe masina
        self.fuelPrice = fuelPrice # Pretul conbustibilului

    # Adds a fuel 
    def addFuel(self, fuel):
        self.fuel += fuel
        if self.maxFuel < self.fuel:
            print(f"You poured {self.fuel-self.maxFuel} liters more fuel and they were lost")
            self.fuel = self.maxFuel

        
    def showFuel(self):
        return "You have " + str(self.fuel) + " fuel remaining."
    
    # Adds a mileage 
    def addMileage(self, mileage):
        self.mileage += mileage
        self.fuel = float(self.fuel) - float(mileage) / float(self.consumptions)
         
    def showMileage(self):
        return str(self.mileage) + " mileage."
    
    # Show expenses
    def showExpenses(self):
        self.expenses = self.fuel * self.fuelPrice + self.expenses + (self.mileage / self.consumptions) * self.fuelPrice
        return "You spend $" + str(self.expenses) + " for fuel in total."

    def __str__(self): 
        return "Brand: %s\nConsumptions: %.2f\nMileage: %.2f\nFuel: %.2f\nFuel Price: %.2f\nExpenses: %.2f " % (self.brand, self.consumptions, self.mileage, self.fuel, self.fuelPrice, self.expenses)
# create object car 
MyCar = Vehicle(input('Brand: '), float(input('Consumptions: ')), float(input('Mileage: ')), float(input('Fuel: ')), float(input('Maximum fuel: ')), float(input('Expenses: ')))
# loop choose option
while True:
    option = input("Select your option: \n 1. Add Fuel\n 2. Show Fuel \n 3. Add Mileage\n 4. Show Mileage\n 5. Show Expenses\n 6. Show all info about car and exit\n")
    if option == "1":
        MyCar.addFuel(float(input('Fuel: ')))
    elif option == "2":
        print(MyCar.showFuel())
    elif option == "3":
        MyCar.addMileage(float(input('Mileage: ')))
    elif option == "4":
        print(MyCar.showMileage())
    elif option == "5":
        print(MyCar.showExpenses())
    elif option == "6":
        print(MyCar)
        exit()
        

