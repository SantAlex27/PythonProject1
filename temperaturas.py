# temperaturas.py

"""
Este programa calcula el promedio de temperaturas por ciudad
durante varias semanas. Utiliza una función en Python para
hacer los cálculos y muestra los resultados en pantalla.
"""

def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperatura de varias ciudades.

    Parámetros:
    temperaturas (dict): Diccionario con ciudades como llaves
                         y listas de temperaturas semanales como valores.

    Retorna:
    dict: Diccionario con ciudades como llaves y promedios de temperaturas como valores.
    """
    promedios = {}
    for ciudad, valores in temperaturas.items():
        promedio = sum(valores) / len(valores)
        promedios[ciudad] = promedio
    return promedios


def main():
    # Datos de ejemplo: 3 ciudades con temperaturas durante 4 semanas
    datos_temperaturas = {
        "Quito": [15, 16, 14, 15],
        "Guayaquil": [28, 29, 30, 31],
        "Cuenca": [12, 13, 11, 12]
    }

    # Llamar a la función
    resultados = calcular_promedios(datos_temperaturas)

    # Mostrar resultados
    print("=== Promedios de Temperatura por Ciudad ===")
    for ciudad, promedio in resultados.items():
        print(f"{ciudad}: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
