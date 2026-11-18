#Listas
alumnos=["juanito", "angelito"]
#Diccionarios
alumno1={
    "nombre":"juanito",
    "edad":15,
    "promedio":8.2
}
alumno2={
    "nombre":"angelito",
    "edad":18,
    "promedio":10
}
#consultar valores
#forma 1
print("nombre: ", alumno1["nombre"])
#forma 2
print("Nombre: ", alumno1.get("nombre"))
#Modificar/Editar algun campo
alumno1["nombre"]="pedrito"
print("nombre: ", alumno1.get("nombre"))
#Mostrar CLAVE:VALOR
for clave, valor in alumno1.items():
    print(clave, ":", valor)
