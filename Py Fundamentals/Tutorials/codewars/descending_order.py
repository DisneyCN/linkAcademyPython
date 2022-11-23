def descending_order(num):
    finalNum = ""
    num = str(num)
    while(num):
        for item in num:
            finalNum = finalNum + max(num)
            num = num[0 : num.index(max(num)) : ] + num[num.index(max(num)) + 1 : :]
    finalNum = int(finalNum.replace(' ', ''))
    return finalNum
print(descending_order(123456789))
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
print(Descending_Order(123456789))