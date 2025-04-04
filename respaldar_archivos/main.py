import shutil
from pathlib import Path
from datetime import datetime


def create_organization_folder(base_path):
    """Create a folder for the organization."""
    folders = {
        "images": [ "jpg", "jpeg", "png", "gif", "bmp"],
        "documents": ["pdf", "docx", "txt", "xlsx", "pptx"],
        "audio": ["mp3", "wav", "flac"],
        "video": ["mp4", "avi", "mkv"],
        "compressed": ["zip", "rar", "tar"],    
        "otros": []
    }

    for folder in folders:
        forlder_path = os.path.join(base_path, folder)
        if not os.path.exists(forlder_path):
            os.makedirs(forlder_path)
        return "others"


def get_folder_for_extension(extension, folders_dict):
    """determina la carpeta para una extensión dada."""
    for folder, extensions in folders_dict.items():
        if extension in extensions:
            return folder
    return "otros"  


def organize_files(base_path):
    """Organiza los archivos en carpetas según su extensión."""
    # Definir las extensiones y sus carpetas correspondientes
    folders_dict = {
        "images": ["jpg", "jpeg", "png", "gif", "bmp"],
        "documents": ["pdf", "docx", "txt", "xlsx", "pptx"],
        "audio": ["mp3", "wav", "flac"],
        "video": ["mp4", "avi", "mkv"],
        "compressed": ["zip", "rar", "tar"],
        # Agregar más categorías según sea necesario
    }

    # Crear las carpetas de organización si no existen
    create_organization_folder(base_path)

    # Recorrer todos los archivos en la carpeta base
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        #ignorar carpetas y archivos ocultos
        if os.path.isdir(file_path) and not filename.startswith('.'):
            # Obtener la extensión del archivo
            extension = os.path.splitext(filename)

            #determinar la carpeta para la extensión
            dest_folder = get_folder_for_extension(extension, folders_dict)
            destination_path = os.path.join(base_path, dest_folder)

            #mover archivo
            try:
                shutil.move(file_path, destination_path)
                print(f"Moviendo {filename} a {dest_folder}")
            except Exception as e:
                print(f"Error moviendo {filename}: {e}")
        #generar reporte
        if log:
            print("reporte de archivos movidos")
            print(f"fecha: {datetime.now("%Y-%m-%d %H:%M:%S")}")
            print(f"archivo: {filename}")
            print(f"carpeta: {dest_folder}")
            print(f"ruta: {destination_path}")
            for entry in log:
                print(entry)
        else:
            print("No se encontraron archivos para mover.")
    except exception as e:
        print(f"error durante la organizacion de archivos: {e}")
    
if __name__ == "__main__":
    # solicitar la ruta de la carpeta a organizar
    directory = input("Ingrese la ruta de la carpeta a organizar: ")
    #si no se especifica la ruta, se usa la carpeta actual
    if not directory:
        directory = os.getcwd()
    #verificar si la carpeta existe
    if not os.path.exists(directory):
        print(f"La carpeta {directory} no existe.")
        exit(1)
    #confirmar acción
    confirm = input(f"¿Está seguro de que desea organizar la carpeta {directory}? (s/n): ")
    if confirm.lower() == 's':
        organize_files(directory)
    else:
        print("Acción cancelada.")
        exit(0)
    


        



    

    