#Programa que agrega peliculas a una lista
#ponerle nombre a mi lista
peliculas=[]
#preguntar cuantas peliculas va agregar
cantPelis=int(input("cuantas peliculas vas a agregar: "))
#valor inicial para el while
i=0
#Mientras i sea menor a cantidad ejecuta:
while i<cantPelis:
    #preguntar peliculas
    pelis=input("Ingresa pelicula: ")
    #agrega pelicula a la lista
    peliculas.append(pelis)
    #muestra la lista
    print(peliculas)
    i+=1
#busca la pelicula en la lista
#pregunta la pelicula a buscar
peliBuscar=input("Que pelicula busca: ")
if peliBuscar in peliculas:
    print("si esta")
else:
    print("no esta pero dejame la agrego")
    peliculas.append(peliBuscar)
    print(peliculas)
#lo extra
#solicitar una pelicula para borrar
peliBorrar=input("Que pelicula desea borrar: ")
#borra la pelicula
peliculas.remove(peliBorrar)
#muestra la lista
print(peliculas)