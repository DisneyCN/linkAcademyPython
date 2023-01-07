from number import *
Romania = Lotto()
print('Romania: ', Romania.generator())
Italia = Lotto(90)
print('Italia : ', Italia.generator())
Polonia = Lotto(80,20)
print('Polonia: ', Polonia.generator())

Player1 = Player(Italia)
print(Player1.choose())

def corectNum(pl,lotto):
    return pl and lotto
print(corectNum(Player1.choose(),Italia.generator()))
    