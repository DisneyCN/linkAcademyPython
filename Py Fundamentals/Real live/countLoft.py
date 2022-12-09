dataName = ['incalzire', 'lumina', 'gaz', 'apa', 'transport gunoi', 'curatenie scara']
data=[]
rooms = []

for item in range(len(dataName)):
    data.append(float(input('Dati datele de la {} :'.format(dataName[item]))))

for item in range(3):
    rooms.append(int(input('Nr persoane camera {} : '.format(item+1))))
count = sum(rooms)

heating = data[0]/3
data.pop(0)
result = sum(data)/count

print('-'*10,'Results','-'*10)
print('Tolal :',round(float(sum(data)+heating*3),2))
for item in range(3):
    print(f'Camera {item+1} : {round(result*rooms[item]+heating,2)}' )
