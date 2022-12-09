amount = int(input("Enter amount : "))
print('Tens : %d\nFives : %d\nTwo\'s : %d \nOnes : %d' % (amount // 10,amount % 10 // 5,amount % 5 // 2,amount % 10 // 5 % 5 // 1))