# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertiram.
Las posibles franquicias son las siguientes: 
# Apple,
# Dunkin Donnuts, 
# Ikea o 
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

A) Programar el boton "Cargar voto" para poder ingresar los siguientes datos:
    * nombre del encuestado.
    * edad (no menor a 18)
    * esta empleado (SI - NO)
    * voto (APPLE, DUNKIN, IKEA, TACO)   

En esta opción, se ingresará un voto a la vez.

B) Al presionar el boton mostrar se deberan listar todos los datos de los encuestados y su posición en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar qué informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal y restele el primer numero. Debera realizar ese informe. 
    En caso de que la resta de negativa, tome el valor positivo de esa resta. 

    Informe 2- Tome el ultimo numero de su DNI Personal y restarselo al numero 9. En caso de que la resta de 9, realizara 
    el informe 7. En caso de que la resta de 8, realizara el informe 6. En caso de que la resta de 3, realizara el informa 4.
    
    Informe 3- Si su DNI personal termina en un numero par, realizará el informe 9. En caso contrario realizar el informe 8.

    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    

    #! 0) - Nombre y situación laboral de las personas que votaron por IKEA con menor edad.
    #! 1) - Nombre y voto, de las personas desempleadas con mayor edad.
    #! 2) - Cuál es la empresa con mas votos.
    #! 3) - Cual es la empresa con menos votos.
    #! 4) - Porcentaje de personas que votaron por TACO, siempre y cuando su edad no se encuentre 
            entre 18 y 25.  
    #! 5) - Porcentaje de personas que no votaron por APPLE, siempre y cuando este empleado o su edad 
            se encuentre entre los 33 y 40.
    #! 6) - Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad este entre 25 y 
            50 años inclusive.
    #! 7) - Cantidad de encuestados con empleo que votaron por APPLE, cuya edad no supere los 35 años.
    #! 8) - Nombre y edad de las personas que votaron DUNKIN o IKEA, cuya edad supere la edad promedio 
            de los que votaron por esas empresas.
    #! 9) - Nombre y edad de las personas empleadas que votaron por DUNKIN, cuya edad este por debajo 
            de la edad promedio de las personas empleadas.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Inversiones - ENCUESTA")
        self.minsize(320, 200)

        self.label_title = customtkinter.CTkLabel(master=self, text="UTN IT - INVERSIONES", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar encuesta", command=self.btn_cargar_encuesta_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

        self.edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 29, 27]
        
        self.trabaja = ["SI", "NO", "NO", "NO", "SI", "NO", "SI", "NO", 
                        "NO", "NO", "SI", "NO", "NO", "NO", "SI", "SI", "SI", 
                        "NO", "SI", "SI"]
        
        self.votos = ["APPLE", "DUNKIN", "IKEA", "APPLE", "TACO", "DUNKIN", "TACO", "APPLE", "TACO", "APPLE",
                    "IKEA", "APPLE", "DUNKIN", "DUNKIN", "APPLE", "IKEA", "APPLE", "DUNKIN", "IKEA", "TACO"]    
        

        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        
    def btn_mostrar_todos_on_click(self):
        contador = 0
        for i in range(len(self.nombres)):
            nombre = self.nombres[i]
            edad = self.edades[i]
            trabaja = self.trabaja[i]
            votos = self.votos[i]
            contador += 1
            print(f"{contador} - {nombre} - {edad} - {trabaja} - {votos}")

    def btn_mostrar_informe_1(self):
        mayor_edad = self.edades[0]

        for i in range(len(self.edades)):
            nombre = self.nombres[i]
            edad = self.edades[i]
            empleado = self.trabaja[i]
            voto = self.votos[i]

            if(empleado == "NO"):
                if(edad >= mayor_edad):
                    mayor_edad = edad
                    
            print(f"{nombre} y voto {voto}")

    def btn_mostrar_informe_2(self):
        cantidad = 0

        for i in range(len(self.nombres)):
            empleado = self.trabaja[i]
            votos = self.votos[i]
            edad = self.edades[i]

            if(empleado == "NO"):
                if(votos == "DUNKIN" or votos == "IKEA"):
                    if(edad > 25 and edad < 50):
                         cantidad += 1
        if(cantidad != 0):
            print(f"las personas son : {cantidad}")

    def btn_mostrar_informe_3(self):
        cantidad = 0 
        edades = 0
        promedio_edad = 0

        for i in range(len(self.nombres)):
             voto = self.votos[i]
             edad = self.edades[i]

             if(voto == "DUNKIN" or voto == "IKEA"):
                  cantidad += 1
                  edades += edad

        if(cantidad != 0):
            promedio_edad = edades / cantidad

        for i in range(len(self.nombres)):
            edad = self.edades[i]
            nombre = self.nombres[i]

            if(promedio_edad < edad):
                print(f"{nombre} y tiene {edad} años")


    def btn_cargar_encuesta_on_click(self):
        flag_nombre = True
        while(flag_nombre):
                nombre = prompt("nombre", "ingresar nombre")
                if(nombre is None or nombre == ""):
                    alert("error", "error")
                elif(nombre.isnumeric()):
                    alert("error", "error")
                else:
                    flag_nombre = False
                    self.nombres.append(nombre)
        flag_edad = True
        while(flag_edad):
                edad = prompt("ingresara edad", "edad")
                if(edad is None or edad == ""):
                    alert("error", "error")
                elif(edad.isdigit()):
                    edad = int(edad)
                    if(edad < 18):
                        alert("error", "error")
                    else:
                        flag_edad = False
                        self.edades.append(edad)
        empleado = prompt("esta empleado", "esta empleado?")
        while(empleado != "NO" and empleado != "SI"):
                empleado = prompt("esta empleado", "esta empleado?")
        self.trabaja.append(empleado)
        voto = prompt("voto", "voto a (APPLE, DUNKIN, IKEA, TACO) ")
        while(voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA" and voto != "TACO"):
                voto = prompt("voto", "voto a (APPLE, DUNKIN, IKEA, TACO) ")
        self.votos.append(voto)


if __name__ == "__main__":
    app = App()
    app.mainloop()