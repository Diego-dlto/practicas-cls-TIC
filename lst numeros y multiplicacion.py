numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("ingresa un numero: "))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿por cuanto deseas multiplicar?: "))

for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)

print("numeros originales: ", numeros)
print("resultados: ", resultados)

#buscar un numero en la lista resultados
numBuscar=int(input("Que numero desea buscar: "))
if numBuscar in resultados:
    print("El numero si se encuentra en resultados")
else:
    print("El numero no esta en la lista de resultados")

