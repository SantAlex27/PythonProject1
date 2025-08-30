# Programa: Búsqueda en una matriz 3x3

# Definimos la matriz 3x3 con valores numéricos
matriz = [
    [5, 12, 9],
    [7, 15, 3],
    [20, 8, 11]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # recorrer filas
        for j in range(len(matriz[i])):   # recorrer columnas
            if matriz[i][j] == valor:
                return (i, j)  # devuelve posición (fila, columna)
    return None

# Pedir al usuario el número a buscar
valor_buscado = int(input(" Ingresa el número que deseas buscar en la matriz: "))

# Mostrar la matriz
print("\nMatriz:")
for fila in matriz:
    print(fila)

# Realizar la búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
if resultado:
    print(f"\n El valor {valor_buscado} fue encontrado en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"\n El valor {valor_buscado} no fue encontrado en la matriz")
