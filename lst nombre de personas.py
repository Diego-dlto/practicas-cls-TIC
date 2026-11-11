nombres=[]
nombresMayus=[]
i=0
while i<5:
    nombre=input("Ingresa tu nombre: ")
    nombres.append(nombre)
    i=i+1

for nombre in nombres:
    print(nombre)

for nombre in nombres:
    nombre=(nombre.upper())
    nombresMayus.append(nombre)

for nombre in nombresMayus:
    print(nombre)