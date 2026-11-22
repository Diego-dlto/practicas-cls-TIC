#programa de venta/renta de DVD´S de videojuegos
#requisito 1 menu de opciones
print("----/VENTA/RENTA DE DVDs/----")
opmenu=0
while opmenu != 6:
    print("Menu de opciones")
    print("1. Reguistrar algun DVD") 
    print("2. Eliminar algun DVD")
    print("3. Mostrar todos los DVDs registrados")
    print("4. Buscar un DVD en especifico")
    print("5. finalizar la compra")
    print("6. salir del programa")
    opmenu=int(input("Que desea hacer "))
    nombrDvd=0
    precioDvd=0
    cantDvd=0
    if opmenu == 1:
        print("--/registrar un dvd/--")
        nombrDvd=input("Ingrese el nombre del DVD: ")
        precioDvd=input("Ingrese el precio del DVD: ")
        cantDvd=input("Ingrese la cantidad de DVD´S que se agregaran: ")
    elif opmenu== 2:
        print("--/Eliminar un dvd/--")
    elif opmenu== 3:
        print("--/Mostrar todos los dvds registrados/--")
    elif opmenu== 4:
        print("--/Buscar un dvd en especifico/--")
    elif opmenu== 5:
        print("--/Finalizar la compra/--")
    elif opmenu==6:
        print("--/Saliendo del programa/--")
