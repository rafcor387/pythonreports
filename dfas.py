import os

def quitar_comillas(input_file, output_file):
    try:
        with open(input_file, 'r') as f_input:
            contenido = f_input.read()
        
        #contenido_sin_comillas = contenido.replace('"', '')
        contenido_sin_comillas = contenido.replace(';', ',')

        with open(output_file, 'w') as f_output:
            f_output.write(contenido_sin_comillas)

        print("Comillas dobles eliminadas con éxito.")
    except FileNotFoundError:
        print("El archivo especificado no se encontró.")

def seleccionar_archivo():
    while True:
        ruta = input("Introduce la ruta del archivo o deja en blanco para navegar por el sistema: ")
        if not ruta:
            ruta = input("Introduce la ruta del directorio a explorar: ")
            if not os.path.isdir(ruta):
                print("La ruta especificada no es un directorio válido.")
                continue
            print("Archivos en el directorio:")
            archivos = os.listdir(ruta)
            for i, archivo in enumerate(archivos):
                print(f"{i+1}. {archivo}")
            indice_archivo = int(input("Selecciona el número del archivo que deseas: ")) - 1
            if indice_archivo < 0 or indice_archivo >= len(archivos):
                print("Selección inválida.")
                continue
            ruta = os.path.join(ruta, archivos[indice_archivo])
        if not os.path.isfile(ruta):
            print("La ruta especificada no corresponde a un archivo.")
            continue
        return ruta

# Seleccionar el archivo de entrada
archivo_entrada = seleccionar_archivo()

# Generar el nombre del archivo de salida
nombre_salida = os.path.splitext(archivo_entrada)[0] + "_sin_comillas.csv"

# Llamar a la función para quitar las comillas dobles
quitar_comillas(archivo_entrada, nombre_salida)
