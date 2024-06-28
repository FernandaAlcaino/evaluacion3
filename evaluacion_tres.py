import json

with open ("biblioteca.json" , "r") as file:
    file =json.load(file)

for datos in file:
    print(file["Autor"])
for datos in file:
    print(file["Categoria"])
for datos in file:
    print(file["Libro"])
for datos in file:
    print(file["Usuario"])
for datos in file:
    print(file["Prestamo"])




def menu1():
    print("*************************")
    print("********Mundo Libro******")
    print("*************************")
    print("1 - Mantenedor de categorias")
    print("2 - Reportes ")
    print("0 - Salir")

def mantenedor_categorias():
    print("***********************************")
    print("********Mantenedor categorias******")
    print("***********************************")
    print("1 - Agregar categoria")
    print("2 - Editar categoria  ")
    print("3 - eliminar categoria")
    print("4 - Buscar categoria")
    print("5 - Volver ")
   
def agregar_id():
  id  = int(input("ingrese el ID del autor: "))
  return id 
def agregar_nombre():
    nombre = str(input("ingresar nombre: "))
    return nombre 
def agregar_nacionalidad():
    nacionalidad = str(input("ingresa una nacionalidad: "))
    return nacionalidad



while True:
    menu1()

    opc =int(input("ingrese una opcion: "))

    if opc == 1:
        mantenedor_categorias()
        while True:
            opc =int(input("ingrese una opcion: "))
            if opc == 1:
                agregar_id()
                agregar_nombre()
                agregar_nacionalidad()
                for datos in enumerate:
                    print(file["Autor"]) + 1
            

            

