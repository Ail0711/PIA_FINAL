import requests
from datetime import datetime
from colorama import Fore, Style
import os
import hashlib

api_url = "https://api.abuseipdb.com/api/v2/check"
api_key = "3a269b21f9049e75e55de50b53c351748d489ad57bf611cad8224b1acacf2e5fc13ae022cce5e81f"

output_file = "reporte_abuso_ip.txt"

def menu ():
    print(Fore.GREEN + "Abuse IP" + Fore.YELLOW + 
          "\nElige una opcion\n1. Busqueda por archivo de texto\n2. Regresar al script principal"
           + Style.RESET_ALL)


def generar_hash_archivo(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def ip_txt():
    doc=input(Fore.YELLOW + "Nombre del documento: "+ Style.RESET_ALL)
    documento = open(doc,'r')
    documento = documento.read().split('\n')
    with open(output_file, "w") as file:
        for ip in documento:
            response = requests.get(
                api_url,
                headers={"Key": api_key, "Accept": "application/json"},
                params={"ipAddress": ip}
            )
            if response.status_code == 200:
                data = response.json()
                file.write(f"Información sobre {ip}:\n{data}\n\n")
            else:
                file.write(f"No se pudo obtener información para {ip}. Status code: {response.status_code}\n\n")
    print(f"El reporte ha sido generado y guardado en{output_file}")
    hash_resultado = generar_hash_archivo(output_file)
    print(f"Tarea ejecutada: {output_file}")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hash del reporte: {hash_resultado}")
    print(f"Ubicación del archivo: {os.path.abspath(output_file)}")
# Ejecutar la función
def main():
    while True:
        menu()
        opcion = input("-------> ")

        if opcion == "1":
            ip_txt()
        elif opcion == "2":
            print("Regresando al script principal")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__=="__main__":
     main()
