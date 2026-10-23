#programa para calcular areas
#area cuadrado; lado x lado
print("Calcular el area de un cuadrado")
lado=float(input("Ingrese su lado: "))
areaCuadrado=lado*lado
print("El area del cuadrado es: ", areaCuadrado)
#area de un triangulo 
print("Calcular el area de un triangulo")
base=float(input("Ingrese su base: "))
altura=float(input("Ingrese su haltura: "))
areaTriangulo=(base*altura)/2
print("El area del triangulo es: ", areaTriangulo)
#area de un trapecio
print("Calcular el area de un trapecio")
basemenor=float(input("ingrese su base menor: "))
basemayor=float(input("ingrese su base mayor: "))
haltura=float(input("ingrese su altura: "))
areaTrapecio= ( basemenor + basemayor) * haltura / 2
print("El area del trapecio es: ", areaTrapecio)
#area de un circulo
print("Calcular el area de un circulo")
radio=float(input("Ingrese el radio del circulo: "))
areaCirculo= (radio*radio) * 3.1415926535
print("el area del circulo es: ", areaCirculo)
#area pentagono
print("calcular el area de un pentagono regular")
ladopent=float(input("ingrese el lado de pentagono: "))
perimetro= ladopent * 5
print("El valor del perimetro es de: ", perimetro)
apotema=float(input("Ingrese la apotema del pentagono: "))
areaPentagono= (perimetro * apotema ) / 2
print("El area del pentagono es de: ", areaPentagono)