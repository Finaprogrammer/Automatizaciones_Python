import os
import datetime
import zipfile

def crear_nombre_backup():
    """
    Genera un nombre único para el archivo de respaldo basado en la fecha y hora actual.
    """
    fecha_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_{fecha_hora}.zip"

def crear_backup(ruta_directorio, ruta_respaldo):
    """
    Crea un archivo zip de respaldo del directorio especificado"
    args:
        ruta_directorio (str): Ruta del directorio a respaldar.
        ruta_respaldo (str): Ruta donde se guardará el archivo zip de respaldo.
    """
    # Verifica si la ruta del directorio existe
    if not os.path.exists(ruta_directorio):
        raise FileNotFoundError(f"La ruta del directorio '{ruta_directorio}' no existe.")
    #verificar que las carpetas existen
    if not os.path.exists(ruta_respaldo):
        raise FileNotFoundError(f"La ruta del respaldo '{ruta_respaldo}' no existe.")
    
    # Genera un nombre de archivo para el respaldo
    nombre_backup = crear_nombre_backup()
    ruta_zip = os.path.join(ruta_respaldo, nombre_backup)
    
    # Crea un archivo zip y agrega el contenido del directorio
    with zipfile.ZipFile(ruta_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for carpeta_raiz, _, archivos in os.walk(ruta_directorio):
            for archivo in archivos:
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                #guardar la ruta relativa en el zip
                ruta_relativa = os.path.relpath(ruta_archivo, start=ruta_directorio)
                zipf.write(ruta_archivo, ruta_relativa)
                print(f"Agregando {ruta_relativa} al respaldo.")
    # Retorna la ruta del archivo zip creado
    
    print(f"Backup creado exitosamente: {ruta_zip}")
    return ruta_zip

def main():
    # Define las rutas de los directorios a respaldar y donde se guardará el respaldo
    ruta_directorio = input("Ingrese la ruta del directorio a respaldar: ")
    ruta_respaldo = input("Ingrese la ruta donde se guardará el respaldo: ")
    
    if not ruta_respaldo:
        ruta_respaldo = "./backup"
    # Crea el respaldo  
    ruta_respaldo = crear_backup(ruta_directorio, ruta_respaldo)

    if ruta_respaldo:
        print(f"\t tamaño del archivo: {os.path.getsize(ruta_respaldo)/(1024*1024):.2f} MB")
        print("Respaldo completado.")
if __name__ == "__main__":
    main()