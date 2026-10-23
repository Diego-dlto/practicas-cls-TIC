#solicitar una calificacion
calif=float(input("Ingresa tu calificacion: "))
if calif==10:
    print("Exelente!!!")
elif calif==9:
    print("Muy bien")
elif calif==8:
    print("Bien")
elif calif==7:
    print("Puedes mejorar")
elif calif==6:
    print("Ay mijo")
else:
    print("Chanclazoooo")

#solicitar una temperatura
temp=float(input("Ingresa la temperatura: "))
if temp>40:
    print("Hace mucho calor")
elif temp>=30 and temp<40:
    print("Esta templado")
elif temp>=20 and temp<30:
    print("Esta fresco")
elif temp<20:
    print("hace frio")
else:
    print("no valido")

#solicitar sexo tipo cadena
#solicitar edad tipo entero
print("¿Puedes sacar cartilla militar?")
sexo=input("Ingrese su sexo: ")
edad=int(input("Ingrese su edad: "))
if sexo=="hombre" and edad>=18:
    print("Puedes sacar la cartilla militar")
else:
    print("no puedes sacar la cartilla militar")