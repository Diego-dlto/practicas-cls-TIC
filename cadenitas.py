nombre="Diego"
frase="El frio si es mental mijo si lo es"
print(nombre)
print(frase)
#mostrar el nombre en mayus
print(nombre.upper())
print(frase.upper())
#mostrar en minusculas
print(frase.lower())
#obtener caracter en posicion
letra=frase[4]
print(letra)
frase2="Ta-haciendo-frio-mijo"
print(frase2.split("-"))
nombreC="Diego de la Torre Orozco"
print(nombreC.split(" "))
#dos primeras letras del nombre
letras1=nombreC[0:2]
print(letras1)
#Remplazar en la cadena
nuevaF=frase.replace("si", "no")
print(nuevaF)
#Numero de caracteres de la cadena: largo
largoCadena=len(nuevaF)
print(largoCadena)