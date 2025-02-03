class ValorInvalidoException(Exception):
    def __init__(self, message):
        super().__init__(message)

def operaciones_basicas(operacion ):
    cadena = operacion.replace(",","")
    cadena = list(cadena)
    for i in range(0,len(cadena)-1):
        if not cadena[i].isdigit():
            raise ValueError("Caracteres no válidos.")
    if "+" in cadena:
        print(int(cadena[0]) + int(cadena[1]))
    elif "-" in cadena:
        print(int(cadena[0]) - int(cadena[1]))
    elif "*" in cadena:
        print(int(cadena[0]) * int(cadena[1]))
    elif "/" in cadena:
        if int(cadena[1]) == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        print(int(cadena[0]) / int(cadena[1]))
    else:
        raise ValorInvalidoException("Operador no válido.")

try:
    operacion = str(input("Ingrese 2 números y el signo operador separados por una coma: "))
    operaciones_basicas(operacion)
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValorInvalidoException as e:
    print(f"Error: {e}")