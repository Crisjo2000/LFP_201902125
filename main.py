import sys
import os
from colorama import Fore, Back, Style
from tkinter import filedialog, Tk
from tkinter.messagebox import NO, RETRY
from pynput import keyboard as kb

listaDatos = []

def PantallaInicial():
    print(Fore.GREEN + "***********************BIENVENIDO***********************")
    print(Fore.GREEN + "*                                                      *")
    print(Fore.GREEN + "*       Lenguajes Formales y de Programación           *")
    print(Fore.GREEN + "*       Sección: B-                                    *")
    print(Fore.GREEN + "*       Carnet: 201902125                              *")
    print(Fore.GREEN + "*       Nombre: Christian Josué Hernández Juárez       *")
    print(Fore.GREEN + "*                                                      *")
    print(Fore.GREEN + "********************************************************")

def MenuInicial(tecla):
    salir = False
    while salir == False:
        print(Fore.CYAN + "***********************MENÚ INICIAL***********************")
        print(Fore.CYAN + "1. Cargar archivo")
        print(Fore.CYAN + "2. Gestionar Películas")
        print(Fore.CYAN + "3. Filtrado")
        print(Fore.CYAN + "4. Ver Gráfica")
        print(Fore.RED + "0. Salir")

        op = int(input(Fore.CYAN + "Ingrese una opción: "))
        
        if op == 1:
            LeerDatos()
        elif op == 2:
            MenuGestionarPeliculas()
        elif op == 3:
            MenuFiltrado()
        elif op == 4:
            print(Fore.LIGHTGREEN_EX + "Graficando...")
            Graficar()
        elif op == 0:
            print(Fore.RED + "Usted está saliendo del programa, feliz día :D")
            sys.exit()
        else:
            print(Fore.RED + "Opción no válida, por favor ingrese un número del 0 al 4")
#LECTURA DEL ARCHIVO
def AbrirArchivo():
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title="Seleccione un archivo",
        initialdir="./",
        filetypes=[
            ("archivos LFP", "*.lfp")
        ]
    )
    if archivo is None:
        print(Fore.RED+ "No se seleccionó ningún archivo\n")
        return None
    else:
        datos = open(archivo, "r")
        print(Fore.LIGHTGREEN_EX + "Archivo cargado correctamente\n")
        return datos
#LECTURA DE LOS DATOS    
def LeerDatos():
    lineas = AbrirArchivo().readlines()
    for i in lineas:
        i = i.replace("\n", "")
        i = i.split(";")
        j = i[1].split(",")
        x = {"nombre": i[0], "actores": j, "año": i[2], "género": i[3]}
        listaDatos.append(x)

def MenuGestionarPeliculas():
    salir = False
    while salir == False:
        print(Fore.BLUE + "***********************GESTIONAR PELÍCULAS***********************")
        print(Fore.BLUE + "1. Mostrar Peliculas")
        print(Fore.BLUE + "2. Mostrar Actores")
        print(Fore.RED + "0. Retroceder")

        op = int(input(Fore.CYAN + "Ingrese una opción: "))
        #MOSTRAR PELÍCULAS
        if op == 1:
            if listaDatos is None:
                print(Fore.RED + "No hay datos cargados")
            else:
                cont = 1
                for i in listaDatos:
                    print(Fore.YELLOW + str(cont) + ". " + i["nombre"])
                    cont += 1
        #MOSTRAR ACTORES
        elif op == 2:
            if listaDatos is None:
                print(Fore.RED + "No hay datos cargados")
            else:
                cont = 1
                for i in listaDatos:
                    print(Fore.YELLOW + str(cont) + ". " + i["nombre"])
                    cont += 1
                op = int(input(Fore.BLUE + "Ingrese el número de la película que desea ver los actores: "))
                if op > len(listaDatos):
                    print(Fore.RED + "Opción no válida, por favor ingrese un número del 0 al " + str(len(listaDatos)))
                else:
                    for i in listaDatos[op-1]["actores"]:
                        print(Fore.LIGHTMAGENTA_EX, i)
        elif op == 0:
            salir = True
        else:
            print(Fore.RED + "Opción no válida, por favor ingrese un número del 0 al 2")

def MenuFiltrado():
    salir = False
    while salir == False:
        print(Fore.BLACK + "***********************FILTRADO***********************")
        print(Fore.BLACK + "1. Filtrado por actor")
        print(Fore.BLACK + "2. Filtrado por año")
        print(Fore.BLACK + "3. Filtrado por género")
        print(Fore.RED + "0. Retroceder")

        op = int(input(Fore.CYAN + "Ingrese una opción: "))
        #FILTRADO POR ACTOR
        if op == 1:
            if len(listaDatos) == 0:
                print(Fore.RED + "No hay datos cargados")
            else:
                cont = 1
                actores = []
                for i in listaDatos:
                    for j in i["actores"]:
                        if j not in actores:
                            actores.append(j)
                for i in actores:
                    print(Fore.YELLOW + str(cont) + ". " + i)
                    cont += 1
                op = int(input(Fore.BLACK + "Ingrese el número del actor que desea buscar sus películas: "))
                if op > len(actores):
                    print(Fore.RED + "Opción no válida, por favor ingrese un número del 0 al " + str(len(actores)))
                else:
                    for i in listaDatos:
                        for j in i["actores"]:
                            if j == actores[op-1]:
                                print(Fore.LIGHTMAGENTA_EX, i["nombre"])

        #FILTRADO POR AÑO
        elif op == 2:
            if len(listaDatos) == 0:
                print(Fore.RED + "No hay datos cargados")
            else:
                anio = input(Fore.BLACK + "Ingrese el año: ")
                cont = 1
                for i in listaDatos:
                    if i["año"] == anio:
                        print(Fore.LIGHTMAGENTA_EX, str(cont)+ ". "+ i["nombre"] + " - " + i["género"])
                        cont+=1
                    if cont == 1 and i["año"] != anio:
                        print(Fore.RED + "No hay películas del año " + anio)
        #FILTRADO POR GÉNERO
        elif op == 3:
            genero = input(Fore.BLACK + "Ingrese el género de película que desea buscar: ")
                
            if len(listaDatos) == 0:
                print(Fore.RED + "No hay datos cargados")
            else:
                cont = 1
                for i in listaDatos:
                    if i["género"] == genero:
                        print(Fore.LIGHTMAGENTA_EX, str(cont) + ". " + i["nombre"] + " - " + i["año"])
                        cont += 1
                    if i["género"] != genero and cont == 1:
                        print(Fore.RED + "No hay películas del género " + genero)
        elif op == 0:
            salir = True
        else:
            print(Fore.RED + "Opción no válida, por favor ingrese un número del 0 al 2")

def Graficar():
    archivoDoT = open("grafica.dot", "w")
    archivoDoT.write("digraph G {\n")
    archivoDoT.write("rankdir=LR;\n")
    archivoDoT.write('node[shape=record, fontname="Arial Black", fontsize=14]\n')

    for i in listaDatos:
        archivoDoT.write(i["nombre"]+'[color=Grey, style=filled, label="'+i["nombre"] +'|'+ i["año"]+'|'+i["género"]+'"]\n')

    for i in listaDatos:
        for j in i["actores"]:
            archivoDoT.write(i["nombre"]+'->'+ j + "\n")
    
    archivoDoT.write("} \n")
    archivoDoT.close()
    
    os.system("dot.exe -Tsvg grafica.dot -o  Grafica.svg")
    os.system("Grafica.svg")

with kb.Listener(on_press=MenuInicial) as listener:
    PantallaInicial()
    listener.join()

if __name__ == "__main__":
    PantallaInicial()