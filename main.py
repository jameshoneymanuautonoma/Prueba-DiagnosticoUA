#                                                              ================= Preguntas =================


#1.
#-Abstracción: Es la capacidad de obtener y aislar toda la información  y cualidades de un objeto que no nos parezcan relevantes,para poder encapsularlos.

#-Encapsulamiento: reunir todos los elementos pertenecientes a una identidad del objeto que se encapsula en una clase. 

#-Ocultación: características de cada objeto deben estar ocultos hacia el exterior, solo el que puede modificar las características del objeto. 

#-Polimorfismo: es un concepto fundamental que comparte características a un objeto. Se puede aplicar tantos objetos como a funciones, por lo que podemos hablar de objetos.

#-Herencia: heredan todas las características de un objeto ya  establecido. 

#2. 
#Propiedad y comportamiento que comparte a un objeto concreto.Por ejemplo, cuando consideramos a una clase "Persona",ésta puede contener atributos como nombre,edad y sexo.

#3. 
#Cualquier cosa que se puede tocar, que debe tener características y que tenga comportamiento.Tal como por ejemplo un Ferrari es un objeto,por lo que podemos definir una clase de auto de color rojo y sus funciones e métodos son las siguientes: acelerar , girar y frenar.



from procesos import Procesos

procesos = Procesos()

def main():
    bandera = 1
    while bandera == 1:
        print('''\n=====_Encuesta Python_=====
    1-. Realizar encuesta
    2-. Finalizar el programa''')
        c=1
        while c==1:
            try:
                opcion=int(input('ingrese una opcion: '))
                if int(opcion >=0) and int(opcion <= 2):
                    c=0
                else:
                    print('opcion invalida')
            except ValueError:
                print('Ingrese una opcion nuevamente entre 1 y 2')
            if opcion == 1:        
                procesos.Encuesta()
            elif opcion ==2:
                bandera = 0               
                procesos.promedio_ingeniero()
                procesos.promedio_abogado()
                procesos.promedio_otras()
                procesos.Porcentaje()
                print('\a¡Hasta la próxima!\n')
        

main()