parentesco=input("¿Que eres mio? ")
if parentesco=="hermano" or parentesco=="hijo":
    print("Eres de mi familia")
else:
    print("No eres de mi familia")

print("¿Puedes entrar?")
edad=int(input("Ingrese su edad: "))
acompañado=input("¿Va usted acompañado? ")
permiso=input("¿Tiene usted permiso? ")
if edad>=18 or permiso=="si":
    print("puedes entrar al concierto")
elif edad>=18 or acompañado=="si":
    print("puedes entrar al concierto")
else:
    print("no puedes entar al concierto")




