# Importam libraria de culori
from termcolor import colored

# Citim marimea bradului de la tastatura
marime = int(input("Introduceti marimea bradului (un numar intreg): "))

# Construim bradul
for i in range(marime):
    # Afisam o linie de caractere '*' colorate in verde
    print(colored('*' * (2*i + 1), 'green'))

# Afisam baza bradului colorata in rosu
print(colored(' ' * (marime - 1) + '*', 'red'))

# Afisam cadourile colorate in albastru
for i in range(marime):
    # Afisam o linie de caractere '*' colorate in albastru
    print(colored('*' * (2*i + 1), 'blue'))