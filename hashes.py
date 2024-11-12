import hashlib
import logging

# Configuración del registro (módulo logging)
logging.basicConfig(filename='hash_generado.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Uso de excepciones
def generate_hash(archivo):
    try:
        # Abrir y leer el archivo
        with open(archivo, 'rb') as archivo:
            contenido = archivo.read()
            logging.info(f'Archivo leído correctamente')

            # Se crea el objeto hash SHA-256
            hash_obj = hashlib.sha256()
            # Se genera el hash
            hash_obj.update(contenido)
            hash_value = hash_obj.hexdigest()

            logging.info(f'El hash ha sido generado: {hash_value}')
            return hash_value

    except FileNotFoundError:
        logging.error(f'Error: El archivo {archivo} no fue encontrado.')
    except IOError:
        logging.error(f'Error: No se pudo leer el archivo {archivo}.')
    except Exception as e:
        logging.error(f'Error inesperado: {str(e)}')

# Entrada principal del script
def main():
    archivo_log = 'ejemplo.txt'  
    
    # Llamar a la función para generar el hash
    hash_value = generate_hash(archivo_log)
    
    if hash_value:
        print(f'Hash generado: {hash_value}')
    else:
        print('No se pudo generar el hash.')

if __name__ == "__main__":
    main()

#EQUIPO 4 
#Ailton Israel de la Cruz Salazar 
#Ximena Mitchel Gallegos Gallegos 
# NO TRABAJÓ (ABRAHAM ESTUDILLO MARTÍNEZ)