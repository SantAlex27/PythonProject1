# Abrimos (o creamos) el archivo my_notes.txt en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("Nota 1: Revisar el material de matemáticas.\n")
archivo.write("Nota 2: Hacer ejercicio en la tarde.\n")
archivo.write("Nota 3: Hacer tarea de Programacón.\n")

# Cerramos el archivo
archivo.close()
# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos y mostramos cada línea
linea = archivo.readline()
while linea != "":
    print(linea.strip())  # strip() quita los saltos de línea extra
    linea = archivo.readline()

# Cerramos el archivo
archivo.close()
