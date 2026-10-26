print("Bonos del epmleado")
nombreEmpleado=input("Ingrese su nombre: ")
pagoXhra=float(input("Ingre la cantidad que gana por hora: "))
hraXmes=float(input("Ingrese la cantidad de horas trabajadas al mes: "))
sueldo=pagoXhra*hraXmes
print("Su sueldo mensual es de: $", sueldo)
if sueldo>=100 and sueldo<=300:
    bono=500
    print("Su bono es de: $", bono)

elif sueldo>300 and sueldo<=1500:
    bono=1700
    print("Su bono es de: $", bono)

elif sueldo>1500 and sueldo<=3000:
    bono=3500
    print("Su bono es de: $", bono)

elif sueldo>3000 and sueldo<=8000:
    bono=8500
    print("Su bono es de: $", bono)

elif sueldo>8000:
    bono=10000
    print("Su bono es de: $", bono)

else:
    print("no valido")
    bono=0
    
sueldobono=sueldo+bono
print("Su sueldo junto con el bono es de: $", sueldobono)
