from profesional import Profesional
from validar import validar_edad

class Procesos:
    def __init__(self):
        self.__listaProfesional = []
        self.__listaIngenieros = []
        self.__listaAbogados = []
        self.__listaOtrasProfesiones = []

    def Get_ListaP(self):
        return self.__listaProfesional

    def Porcentaje(self):
        porcentaje_ingenieros = (len(self.__listaIngenieros) / len(self.__listaProfesional)) * 100
        porcentaje_abogados = (len(self.__listaAbogados) / len(self.__listaProfesional)) * 100
        porcentaje_otras_profesiones = (len(self.__listaOtrasProfesiones) / len(self.__listaProfesional)) * 100
        print(f"Porcentaje de ingenieros: {porcentaje_ingenieros}%")
        print(f"Porcentaje de abogados: {porcentaje_abogados}%")
        print(f"Porcentaje de otras profesiones: {porcentaje_otras_profesiones}%\n")

    def promedio_ingeniero(self):
        if not self.__listaIngenieros:
            print("\nNo hay ingenieros registrados.")
            return
        contador_ingeniero = len(self.__listaIngenieros)
        suma_sueldos_ingeniero = sum(profesional.GetSueldo() for profesional in self.__listaIngenieros)
        promedio_I = suma_sueldos_ingeniero / contador_ingeniero
        print(f'\nEl sueldo promedio de los ingenieros es {promedio_I}')

    def promedio_abogado(self):
        if not self.__listaAbogados:
            print("No hay abogados registrados.")
            return
        contador_abogado = len(self.__listaAbogados)
        suma_sueldos_abogado = sum(profesional.GetSueldo() for profesional in self.__listaAbogados)
        promedio_A = suma_sueldos_abogado / contador_abogado
        print(f'El sueldo promedio de los abogados es {promedio_A}')

    def promedio_otras(self):
        if not self.__listaOtrasProfesiones:
            print("No hay otras profesiones registradas.")
            return
        contador_otras = len(self.__listaOtrasProfesiones)
        suma_sueldos_otras = sum(profesional.GetSueldo() for profesional in self.__listaOtrasProfesiones)
        promedio_O = suma_sueldos_otras / contador_otras
        print(f'El sueldo promedio de las otras profesiones es {promedio_O}')

    def Encuesta(self):
        print('\n¡Bienvenido a la encuesta!\n')
        nombre = input('Ingrese su nombre:')
        c = 1
        while c == 1:
            try:
                edad = int(input('Ingrese su edad:'))
                if validar_edad(edad):
                    c = 0
                else:
                    print('Edad invalida')
            except ValueError:
                print('Error, ingrese un numero entero mayor a 0.')
        
        sexo = input('Ingrese sexo (Masculino o Femenino):')
        profesion = input('¿Cuál es su profesión? (Ingeniero - Abogado - Otra):')
        sueldo = int(input('Ingrese su sueldo:'))
        vasija = Profesional(profesion, sueldo, nombre, edad, sexo)
        self.__listaProfesional.append(vasija)
        
        if profesion.lower() == 'ingeniero':
            self.__listaIngenieros.append(vasija)
        elif profesion.lower() == 'abogado':
            self.__listaAbogados.append(vasija)
        else:
            self.__listaOtrasProfesiones.append(vasija)
