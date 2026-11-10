nombres=[]
nombreMayus=[]
i=0
while i<5:
    nombre=input("Ingresa tu nombre: ")
    nombres.append(nombre)
    i=i+1

for nombre in nombres:
    print(nombre)

for nombre in nombres:
    nombreMayus=(nombre.upper())
print(nombreMayus)