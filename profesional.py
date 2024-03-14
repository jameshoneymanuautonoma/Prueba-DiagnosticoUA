from persona import Persona

class Profesional(Persona):

    def __init__(self,profesion,sueldo, nombre, edad, sexo):
        super().__init__(nombre, edad, sexo)
        self.__profesion= profesion
        self.__sueldo= sueldo
    
    def SetProfesion(self,profesion):
        self.__profesion= profesion
    def SetSueldo(self,Sueldo):
        self.__sueldo= Sueldo
    
    def GetProfesion(self):
        return self.__profesion
    def GetSueldo(self):
        return self.__sueldo