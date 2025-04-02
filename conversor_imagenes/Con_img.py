import os
from PIL import Image

def listar_formatos_soportados():
    """
    Lista los formatos de imagen soportados por PIL.
    """
    return Image.registered_extensions()

def convertir_imagen(ruta_imagen, formato_salida, carpeta_destino=None):
    """
    Convierte una imagen a un formato específico.
    args:
        ruta_imagen (str): Ruta de la imagen de entrada.
        formato_salida (str): Formato de salida deseado (ej. 'JPEG', 'PNG').
        carpeta_salida (str): Ruta de la carpeta de salida.
    returns:
        str: Ruta de la imagen convertida.
    """
    try:
        # Verificar si la imagen existe
        if not os.path.isfile(ruta_imagen):
            raise FileNotFoundError(f"La imagen {ruta_imagen} no existe.")

        #abrir la imagen
        imagen = Image.open(ruta_imagen)

        #obtener informacion de la imagen
        nombre_archivo = os.path.basename(ruta_imagen)
        nombre_base = os.path.splitext(nombre_archivo)[0]

        # Crear la carpeta de salida si no existe
        if carpeta_destino is None:
            carpeta_destino = os.path.dirname(ruta_imagen)
        os.makedirs(carpeta_destino, exist_ok=True)
        
        #crear la ruta de salida
        formato_salida = formato_salida.upper()
        ruta_salida = os.path.join(carpeta_destino, f"{nombre_base}.{formato_salida.lower()}")
        
        #guardar la imagen convertida
        imagen.save(ruta_salida, formato_salida)
        print(f"Imagen convertida y guardada en: {ruta_salida}")
        return ruta_salida
        
    except Exception as e:
        print(f"Error al convertir la imagen: {e}")
        return None

def convertir_imagenes_en_carpeta(carpeta_entrada, formato_salida, carpeta_destino=None):
    """
    Convierte todas las imágenes en una carpeta a un formato específico.
    args:
        carpeta_entrada (str): Ruta de la carpeta de entrada.
        formato_salida (str): Formato de salida deseado (ej. 'JPEG', 'PNG').
        carpeta_destino (str): Ruta de la carpeta de salida.
    """
    # Verificar si la carpeta de entrada existe
    if not os.path.isdir(carpeta_entrada):
        raise FileNotFoundError(f"La carpeta {carpeta_entrada} no existe.")
    #extensiones soportadas
    formatos_soportados = listar_formatos_soportados()

    #contador de imagenes convertidas
    contador_convertidas = 0

    #recorrer todos los archivos de la carpeta
    for archivo in os.listdir(carpeta_entrada):
        ruta_archivo = os.path.join(carpeta_entrada, archivo)
        if os.path.isfile(ruta_archivo):
            #verificar si la imagen es soportada
            _, extension = os.path.splitext(archivo)
            if extension.lower() in formatos_soportados:
                #convertir la imagen
                convertir_imagen(ruta_archivo, formato_salida, carpeta_destino)
                contador_convertidas += 1

    # Crear la carpeta de salida si no existe
    if carpeta_destino is None:
        carpeta_destino = os.path.dirname(carpeta_entrada)
    
    # Listar todos los archivos en la carpeta de entrada
    for archivo in os.listdir(carpeta_entrada):
        ruta_archivo = os.path.join(carpeta_entrada, archivo)
        if os.path.isfile(ruta_archivo):
            convertir_imagen(ruta_archivo, formato_salida, carpeta_destino)
    return contador_convertidas




def main():
    """
    Función principal para ejecutar el script.
    """
    print("Bienvenido al conversor de imágenes.")
    # Listar formatos soportados
    listar_formatos = listar_formatos_soportados()
    print("Formatos soportados por PIL:")
    for formato in listar_formatos:
        print(f"- {formato}")
    #menu opciones
    print("Opciones:")
    print("1. Convertir una imagen")    
    print("2. Convertir todas las imágenes en una carpeta")
    opcion = input("Seleccione una opción (1 o 2): ")
    if opcion == "1":
        ruta_imagen = input("Ingrese la ruta de la imagen: ")
        formato_salida = input("Ingrese el formato de salida (ej. 'JPEG', 'PNG'): ")
        carpeta_destino = input("Ingrese la carpeta de destino (dejar vacío para usar la misma carpeta): ")
        if carpeta_destino.strip() == "":
            carpeta_destino = None
        convertir_imagen(ruta_imagen, formato_salida, carpeta_destino)
    elif opcion == "2":
        carpeta_entrada = input("Ingrese la ruta de la carpeta de entrada: ")
        formato_salida = input("Ingrese el formato de salida (ej. 'JPEG', 'PNG'): ")
        carpeta_destino = input("Ingrese la carpeta de destino (dejar vacío para usar la misma carpeta): ")
        if carpeta_destino.strip() == "":
            carpeta_destino = None
        contador_convertidas = convertir_imagenes_en_carpeta(carpeta_entrada, formato_salida, carpeta_destino)
        print(f"Se han convertido {contador_convertidas} imágenes.")
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
