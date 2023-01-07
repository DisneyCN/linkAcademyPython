import random 
class Lotto:
    def __init__(self,end:int = 49,num:int = 6):
        self.end = end
        self.num = num
        
    def generator(self):
        generatedNum =  set()
        while len(generatedNum) < self.num:
            generatedNum.add(random.randint(1,self.end))
        return generatedNum
            
class LottoRomania(Lotto):
        def __init__(self):
            super(Lotto,self).__init__(6,49)
            
class LottoItalia(Lotto):
    def __init__(self):
            super(Lotto,self).__init__(6,90)
        
class LottoPolonia(Lotto):
    def __init__(self):
            super(Lotto,self).__init__(20,80)

class Player:
    def __init__(self,lotto):
        self.totalNum = lotto.end
        self.noOfchoose = lotto.num
        self.playerNum = set()
    def __str__(self):
        return self.playerNum
    def choose(self):
        while len(self.playerNum)< self.noOfchoose:
            if len(self.playerNum) != 0:   
                print("Player numbers : {}".format(self.playerNum))
            new = int(input("Enter the number : "))
            if new in range(self.totalNum):
                self.playerNum.add(new)
        return self.playerNum