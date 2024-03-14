def validar_edad(edad):
        try:
            if (int(edad) > 0):
                return True
            else:
                return False
        except ValueError:
            return False