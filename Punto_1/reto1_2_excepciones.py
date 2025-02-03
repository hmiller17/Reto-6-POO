def es_palindromo(palabra):
    try:
        if not isinstance(palabra, str):
            raise TypeError("La entrada debe ser una cadena de texto.")
        if not palabra:
            raise ValueError("La palabra no puede estar vacía.")
        if palabra.isdigit():
            raise ValueError("No se permiten números, ingrese solo palabras.")
        palabra = palabra.lower()
        for i in range(len(palabra) // 2):
            if palabra[i] != palabra[len(palabra) - 1 - i]:
                return print("No es palindromo")
        return print("Es palindromo")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


palabra = input("Ingrese una palabra: ")
es_palindromo(palabra)
