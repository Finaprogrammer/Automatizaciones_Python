import openpyxl
from openpyxl.styles import Font, PatternFill, alignment
from openpyxl.utils import get_column_letter
import os

def cargar_inventario():
    try:
        # Obtener la ruta del archivo actual
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "inventario_tecnologia.xlsx")
        
        # Cargar el archivo de inventario
        wb = openpyxl.load_workbook(ruta_archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de inventario en la carpeta actual.")
        return None, None
    
    ws = wb.active
    ws.title = "Inventario principal"

    return wb, ws


def automatizacion_inventario():
    """Automatizar la creación de un archivo Excel con productos tecnológicos."""
    wb, ws = cargar_inventario()
    if not wb:
        return
    
    # Guardar el archivo actualizado
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo_v2 = os.path.join(ruta_actual, "inventario_tecnologia_v2.xlsx")
    wb.save(ruta_archivo_v2)
    print("\nProceso de automatización finalizado. Archivo guardado como 'inventario_tecnologia_v2.xlsx'.")

if __name__ == '__main__':
    automatizacion_inventario()






