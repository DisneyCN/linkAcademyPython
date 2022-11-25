def inputList():
    global a, b
    a = [int(item) for item in input("Enter the list a items : ").split()]
    b = [int(item) for item in input("Enter the list b items : ").split()]

sum = []

def sumElements(a,b):
    global sum
    for i in range(len(a)):
        sum.append(a[i]+b[i])
    print(sum)

while True:
    inputList()
    if len(a) == len(b):
        sumElements(a,b)
        break
    else:
        print('Lenght of list must be equal \nWrite again!')
        continue