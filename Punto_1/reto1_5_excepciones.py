def mismos_caracteres(lista):
    try:
        agrupados = {}
        if not lista:
            raise ValueError("La lista no puede estar vacía.")
        for palabra in lista:
            clave = "".join(sorted(palabra))
            if clave in agrupados:
                agrupados[clave].append(palabra)
            else:
                agrupados[clave] = [palabra]
        resultado = []
        for grupo in agrupados.values():
            if len(grupo) > 1:
                resultado.extend(grupo)
        return print(resultado)
    except (ValueError) as e:
        print(f"Error: {e}")

mismos_caracteres(["amor", "roma", "perro", "maro", "arpa", "capa"])