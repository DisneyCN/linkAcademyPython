def convertTuple(tup):
    str=''
    for item in tup:
        str = str + " " + item
    return str

tuples = ('Hello', 'my', 'friend','!')
str = convertTuple(tuples)
print(str)