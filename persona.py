class Persona:
    def __init__(self,nombre, edad, sexo):
        self.__nombre= nombre
        self.__edad= edad
        self.__sexo=sexo

    def SetNombre(self,nombre):
        self.__nombre=nombre
    def SetEdad(self,edad):
        self.__edad= edad
    def SetSexo(self,sexo):
        self.__sexo= sexo

    def GetNombre(self):
        return self.__nombre
    def GetEdad(self):
        return self.__edad
    def GetSexo(self):
        return self.__sexo