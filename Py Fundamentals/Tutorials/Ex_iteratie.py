def convert(string1):
    list_1 = list(string1.split(','))
    return list_1

string = input('string = ')
list_ = convert(string)

string = ""
for item in list_:
    item = int(item) ** 2
    string=string + "," +  str(item)

print('string = "' + string[1:] +'"')