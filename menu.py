import argparse
import subprocess
import hashlib
from datetime import datetime
import platform
import os
import subprocess
import login as mix

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description="Indicar los parametros para poder acceder al script")

# Agregar argumentos de entrada
parser.add_argument('argum1', type=str, help="Tipo de lenguaje (escribir su numero) 1-Poweshell, 2-Bash o 3-Python")
parser.add_argument('--accion', type=str, choices=['menu', 'script'], default='def', help="Entrar a un menú escribir menú")

# Parsear los argumentos de entrada
args = parser.parse_args()

def generar_hash_archivo(file_path):
    hash_SHA_256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_SHA_256.update(chunk)
    return hash_SHA_256.hexdigest()


def conect():
    mix.main()

def main():
    so = platform.system() 
    if args.accion=="menu":
        if so == "Windows":
            if args.argum1=="1":
                print
            elif args.argum1=="2":
                print("No se puede ejecutar en este sistema operativo")
            elif args.argum1=="3":
                conect()
    elif so == "Linux":
            if args.argum1=='1':
                print("No se puede ejecutar en este sistema operativo")
            elif args.argum1=='2':
                op = input("Script a ejecutar")
                if op=="1": 
                    process = subprocess.Popen(['bash', "C:\Users\aiisd\OneDrive\Documentos\finalfainal\network_monitor (1).sh"],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        text=True)

                opciones = "2"  
                stdout, stderr = process.communicate(input=opciones)

                print("Salida del script:")
                print(stdout)
                with open("Monitoreo_red.txt", "w", encoding="utf-8") as archivo:
                    archivo.write(stdout)
                print(f"Consulta guardada en Monitoreo_red.txt")
                nombre_archivo = f"Monitoreo_red.txt" #aqui ponemos el nombre del script 
                hash_resultado = generar_hash_archivo(nombre_archivo)
                print(f"Tarea ejecutada: nombre del sript")
                print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Hash del reporte: {hash_resultado}")
                print(f"Ubicación del archivo: {os.path.abspath(nombre_archivo)}")
                
                if op=="2":
                    process = subprocess.Popen(['bash', "C:\Users\aiisd\OneDrive\Documentos\finalfainal\pia 1 (1).sh"],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        text=True)

                opciones = "2"  
                stdout, stderr = process.communicate(input=opciones)

                with open("Reporte_puertos.txt", "w", encoding="utf-8") as archivo:
                    archivo.write(stdout)
                print(f"Consulta guardada en Reporte_puertos.txt")
                nombre_archivo = f"Reporte_puertos.txt" #aqui ponemos el nombre del script 
                hash_resultado = generar_hash_archivo(nombre_archivo)
                print(f"Tarea ejecutada: nombre del sript")
                print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Hash del reporte: {hash_resultado}")
                print(f"Ubicación del archivo: {os.path.abspath(nombre_archivo)}")

            elif args.argum1=='3':
                conect()

if __name__=="__main__":
    main()