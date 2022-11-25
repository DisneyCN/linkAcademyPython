#Creez functie 
def convert(string1):
    list_1 = list(string1.split(','))
    return list_1

string = input('string = ')
list_ = convert(string)
listPow =[]
for item in list_:
    listPow.append(str(int(item) ** 2))
    
string=','.join(listPow)
print('string = "' + string +'"')