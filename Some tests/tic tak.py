import tkinter as tk

# Cream fereastra principala
root = tk.Tk()
root.title("Brad de Craciun")

# Citim marimea bradului de la tastatura
marime = int(input("Introduceti marimea bradului (un numar intreg): "))

# Construim bradul
for i in range(marime):
    # Cream o eticheta pentru a afisa o linie de caractere '*' colorate in verde
    label = tk.Label(root, text='*' * (2*i + 1), fg='green')
    # Afisam eticheta
    label.pack()

# Cream o eticheta pentru a afisa baza bradului colorata in rosu
label = tk.Label(root, text='*', fg='red')
# Afisam eticheta
label.pack()

# Construim cadourile
for i in range(marime):
    # Cream o eticheta pentru a afisa o linie de caractere '*' colorate in albastru
    label = tk.Label(root, text='*' * (2*i + 1), fg='blue')
    # Afisam eticheta
    label.pack()

# Afisam fereastra principala
root.mainloop()