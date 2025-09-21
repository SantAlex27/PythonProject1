"""
CalculoDescuento.py
Ejercicio: función para calcular descuento y mostrar monto final.
"""

from typing import Tuple

def calcular_descuento(monto_total: float, porcentaje: float = 10.0) -> float:
    """
    Calcula y devuelve el monto del descuento aplicado al monto_total.
    - monto_total: valor total de la compra (ej. 150.00)
    - porcentaje: porcentaje de descuento (ej. 10.0 para 10%)
    Retorna: monto del descuento (float)
    """
    if monto_total < 0:
        raise ValueError("El monto total no puede ser negativo.")
    descuento = monto_total * (porcentaje / 100.0)
    return descuento

def aplicar_descuento(monto_total: float, porcentaje: float = 10.0) -> Tuple[float, float]:
    """
    Devuelve una tupla (descuento, total_a_pagar).
    """
    descuento = calcular_descuento(monto_total, porcentaje)
    total_a_pagar = monto_total - descuento
    return round(descuento, 2), round(total_a_pagar, 2)

if __name__ == "__main__":
    # Ejemplo con valores fijos (como antes)
    monto1 = 150.00
    descuento1, final1 = aplicar_descuento(monto1)
    print(f"Compra 1: monto = {monto1:.2f} | descuento (10%) = {descuento1:.2f} | total a pagar = {final1:.2f}")

    monto2 = 250.50
    porcentaje2 = 20.0
    descuento2, final2 = aplicar_descuento(monto2, porcentaje2)
    print(f"Compra 2: monto = {monto2:.2f} | descuento ({porcentaje2:.0f}%) = {descuento2:.2f} | total a pagar = {final2:.2f}")

    # 🔽 Parte interactiva 🔽
    print("\n--- Cálculo Interactivo ---")
    try:
        monto_input = float(input("Ingresa el monto de la compra: "))
        porcentaje_input = input("Ingresa el porcentaje de descuento (deja vacío para 10): ")

        # Si el usuario no escribe nada, se usa 10 por defecto
        if porcentaje_input.strip() == "":
            porcentaje_input = 10.0
        else:
            porcentaje_input = float(porcentaje_input)

        d, t = aplicar_descuento(monto_input, porcentaje_input)
        print(f"Descuento = {d:.2f} | Total a pagar = {t:.2f}")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")