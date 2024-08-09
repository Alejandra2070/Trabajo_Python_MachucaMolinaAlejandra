#importamos date para que se agregue automaticamente la fecha cuando se solicita
from datetime import date
#importamos json para trabajar con el
import json
######################################

#Hacemos definiciones e importamos los json
def abrirArchivo():
    miJson=[]
    with open("medicamentos.json", encoding="utf-8") as openfile:
        miJson= json.load(openfile)
        return miJson
archivo=abrirArchivo()

def guardarArchivo(miData):
    with open("medicamentos.json","w") as outfile:
        json.dump(miData,outfile)
#####################################
def abrirArchivo2():
    miJson2=[]
    with open("ventas.json", encoding="utf-8") as openfile:
        miJson2= json.load(openfile)
        return miJson2
archivo2=abrirArchivo2()

def guardarArchivo2(miData):
    with open("ventas.json","w") as outfile:
        json.dump(miData,outfile)
#####################################
def abrirArchivo3():
    miJson3=[]
    with open("compras.json", encoding="utf-8") as openfile:
        miJson3= json.load(openfile)
        return miJson3
archivo3=abrirArchivo3()

def guardarArchivo3(miData):
    with open("compras.json","w") as outfile:
        json.dump(miData,outfile)
######################################
def abrirArchivo4():
    miJson4=[]
    with open("proveedores.json", encoding="utf-8") as openfile:
        miJson4= json.load(openfile)
        return miJson4
archivo4=abrirArchivo4()

def guardarArchivo4(miData):
    with open("proveedores.json","w") as outfile:
        json.dump(miData,outfile)
######################################
def abrirArchivo5():
    miJson5=[]
    with open("pacientes.json", encoding="utf-8") as openfile:
        miJson5= json.load(openfile)
        return miJson5
archivo5=abrirArchivo5()

def guardarArchivo5(miData):
    with open("pacientes.json","w") as outfile:
        json.dump(miData,outfile)
######################################
def abrirArchivo6():
    miJson6=[]
    with open("empleados.json", encoding="utf-8") as openfile:
        miJson6= json.load(openfile)
        return miJson6
archivo6=abrirArchivo6()

def guardarArchivo6(miData):
    with open("empleados.json","w") as outfile:
        json.dump(miData,outfile)
######################################

#creamos un menú para facilitar la realización del programa
print("#################################")
print("-------BIENVENIDOSSSSS!-------")
print("#################################")
print("-------------Menú-------------")
print("""
    1. Registrar ventas
    2. Registrar compras
    5. Salir del programa
      """)

#elegir cual de las opciones va a realizar
opc=int(input("Elige una de las opciones de nuestro menú: "))
miInfo=[]
if (opc==1):
    
    miInfo=abrirArchivo2() #abrimos la libreria
    #ingresar la información de la venta
    fechaR = str(date.today())
    nombreCR = input("Ingresa el nombre del paciente: ")
    direccionR = int(input("Ingresa la dirección del paciente: "))
    nombreER = input("Ingresa el nombre del empleado que realizó la venta: ")
    cargoER = input("Ingresa el cargo del empleado que realizó la venta: ")
    booleano = True
    #se crea un booleano facilitar la ejecución del programa.
    while booleano==True:
        nombrePR = input("Ingresa el nombre del producto vendido: ")
        cantidadPR = int(input("Ingresa la cantidad vendida del producto: "))
        precioPR = int(input("Ingresa el precio del producto vendido: "))
        #información para guardar la venta
        registroR = {
            "fechaVenta": fechaR,
            "paciente":{
                "nombre": nombreCR,
                "direccion": direccionR,
            },
            "empleado":{
                "nombre": nombreER,
                "cargo": cargoER,
            },
            "medicamentosVendidos":{
                "nombreMedicamento": nombrePR,
                "cantidadVendida": cantidadPR,
                "precio": precioPR
            }
        }
        #abrir la libreria para guardar la información de la venta
        miInfo = abrirArchivo2()
        miInfo[0]["info"].append(registroR)
        guardarArchivo2(miInfo)
        otro=int(input("Deseas agregar otro medicamento?(1. Si/ 2. No): "))
        if otro==1:
            booleano=True
        else:
            booleano=False
    
    #una vez guardada, se le informa al usuario
    print("La venta se guardó correctamente.")
elif(opc==2):
    miInfo=abrirArchivo3() #abrir la libreria
    #pedir la información de la compra
    fechaPro = str(input(date.today()))
    nombreProR = input("Ingresa el nombre del proveedor: ")
    contactoPro = int(input("Ingresa el contacto del proveedor: "))
    nombrePro = input("Ingresa el nombre del producto: ")
    cantidadPro = int(input("Ingresa la cantidad del producto vendido: "))
    precioPro = int(input("Ingresa el precio de la compra: "))
    #información de la compra realizada
    registro = {
        "fechaCompra": fechaPro,
        "proveedor":{
            "nombre": nombreProR,
            "contacto": contactoPro,
        },
        "medicamentosComprados":{
            "nombreMedicamentos": nombrePro,
            "cantidadComprada": cantidadPro,
            "precioCompra": precioPro
        } 
    }
    #abrir la libreria y guardar la información en ella
    miInfo = abrirArchivo3()
    miInfo[0]["compras"].append(registro)
    guardarArchivo3(miInfo)
    #se informa que la compra ya se guardó
    print("La compra se realizó correctamente.")
elif(opc==3):
    print("Muchas gracias por utilizar nuestro programa. Vuelve pronto.")

#Desarrollado por Alejandra Machuca Grupo T2 CampusLands