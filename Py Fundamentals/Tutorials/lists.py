# list=['Marco',3,(1993,12),{'gender':'Male'}]
# for item in list :
#     print(type(item),' : ', item)
    
matrice = [[1, 200, 3],
           [20, 5, 6],
           [7, 8, 9]]
matrice.append([3,5,9])
del matrice[2]
matrice.sort()
print(matrice)