# tarea_diccionarios.py
# Tarea: Diccionarios en Python
# Fase 1: Diccionario con datos ficticios
# Fase 2: Diccionario con datos ingresados por el usuario

print("=== FASE 1: Diccionario con datos ficticios ===")

# --- 1) Crear un diccionario con datos ficticios ---
informacion_personal = {
    "nombre": "Ana Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Diseñadora"
}
print("\nDiccionario creado inicialmente:")
print(informacion_personal)

# --- 2) Acceder y modificar valores ---
print("\nCiudad actual:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"
print("Ciudad modificada:", informacion_personal["ciudad"])

informacion_personal["profesion"] = "Ingeniera de Software"
print("Profesión actualizada:", informacion_personal["profesion"])

# --- 3) Verificar existencia de claves ---
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 99 876 5432"
    print("Se agregó la clave 'telefono':", informacion_personal["telefono"])

# --- 4) Eliminar la clave edad ---
informacion_personal.pop("edad", None)
print("Clave 'edad' eliminada.")

# --- 5) Imprimir el diccionario final ---
print("\nDiccionario final con datos ficticios:")
print(informacion_personal)


# =====================================================
# FASE 2: Interacción con el usuario
# =====================================================
print("\n\n=== FASE 2: Ahora ingresa nuevos datos ===")

# --- 1) Crear un diccionario con datos ingresados ---
nombre = input("Ingresa un nombre: ")
edad = input("Ingresa la edad: ")
ciudad = input("Ingresa la ciudad: ")
profesion = input("Ingresa la profesión: ")

info_usuario = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad,
    "profesion": profesion
}
print("\nDiccionario creado con tus datos:")
print(info_usuario)

# --- 2) Acceder y modificar valores ---
print("\nCiudad actual:", info_usuario["ciudad"])
nueva_ciudad = input("Ingresa una ciudad diferente: ")
info_usuario["ciudad"] = nueva_ciudad
print("Ciudad modificada:", info_usuario["ciudad"])

nueva_profesion = input("Ingresa una nueva profesión: ")
info_usuario["profesion"] = nueva_profesion
print("Profesión actualizada:", info_usuario["profesion"])

# --- 3) Verificar existencia de claves ---
if "telefono" not in info_usuario:
    telefono = input("Ingresa un número de teléfono ficticio: ")
    info_usuario["telefono"] = telefono
    print("Se agregó la clave 'telefono':", info_usuario["telefono"])

# --- 4) Eliminar la clave edad ---
info_usuario.pop("edad", None)
print("Clave 'edad' eliminada.")

# --- 5) Imprimir el diccionario final ---
print("\nDiccionario final con tus datos:")
print(info_usuario)
