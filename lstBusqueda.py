nombres=["Angel", "Karla", "Luis", "Mateo", "Maria", "Luis", "Karla"]
print(f"Los nombres que tienen son: {nombres}")
nombreBuscar=input("¿Que nombre desea buscar?: ")
encontrado=False
contador=0
i=0 
while i <len(nombres):
    if nombres[i]==nombreBuscar:
        encontrado=True
        contador=contador+1
        print("Encpontrado en la posicion: ", i)
    i+=1
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece", contador, "veces")

if contador==2:
    nombres.remove(nombreBuscar)
    print("El nompre aparece dos veces ya fue correjido")
else:
    print("No encontrado")

print(nombres)