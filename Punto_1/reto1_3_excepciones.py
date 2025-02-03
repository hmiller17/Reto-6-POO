def primos(numeros):
    n_primos = []
    numeros = list(numeros)
    for i in numeros:
        try:
            i = int(i)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            n_primos.append(i)
    return print(n_primos)

numeros = str(input("Ingrese varios numeros: "))
primos(numeros)