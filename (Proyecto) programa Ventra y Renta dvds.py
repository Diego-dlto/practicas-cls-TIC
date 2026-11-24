#programa de venta/renta de DVD´S

print("----/VENTA/RENTA DE DVDs/----")
dvd1={
    "nombre":"nd",
    "precio":"nd",
    "cantidad":"nd"
}
dvd2={
    "nombre":"nd",
    "precio":"nd",
    "cantidad":"nd"}
dvd3={
    "nombre":"nd",
    "precio":"nd",
    "cantidad":"nd"}
dvd4={
    "nombre":"nd",
    "precio":"nd",
    "cantidad":"nd"}

opmenu=0
while opmenu != 6:
    #requisito 1 menu de opciones
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
    print("Menu de opciones")
    print("1. Reguistrar algun DVD") 
    print("2. Eliminar algun DVD")
    print("3. Mostrar todos los DVDs registrados")
    print("4. Buscar un DVD en especifico")
    print("5. finalizar la compra")
    print("6. salir del programa")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
    opmenu=int(input("Ingrese una opcion: "))
    nombrDvd=0
    precioDvd=0
    cantDvd=0
    if opmenu == 1:
        print("--/registrar un dvd/--")
        nombrDvd=input("Ingrese el nombre del DVD: ")
        precioDvd=int(input("Ingrese el precio del DVD: "))
        cantDvd=int(input("Ingrese la cantidad de DVD´S que se agregaran: "))
        dvd1=["nombre"]=nombrDvd
        dvd1=["precio"]=precioDvd
        dvd1=["cantidad"]=cantDvd





    elif opmenu== 2:
        print("--/Eliminar un dvd/--")
        elimNombre=input("Que DVD desea eliminar del registro: ")


    elif opmenu== 3:
        print("--/Mostrar todos los dvds registrados/--")
        for clave, valor in DVDs.items():
            print(clave, ":", valor)

    elif opmenu== 4:
        print("--/Buscar un dvd en especifico/--")
    elif opmenu== 5:
        print("--/Finalizar la compra/--")
    elif opmenu==6:
        print("--/Saliendo del programa/--")
    else:
        print("Opcion no valida")