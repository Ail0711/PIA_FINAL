from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import sys
from datetime import datetime
import hashlib

private_key =rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def menuasyc():
    print("\nCifrado Asimetrico")
    print("1. Cifrar un mensaje de texto")
    print("2. Cifrar un archivo de texto")
    print("3. Salir")

def generar_hash_archivo(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def asyc():
    while True:
        menuasyc()
        op=input("--->")
        if op=="1":
            cif_mensaje()
        elif op == "2":
            cif_file()
        elif op == "3":
            break
                
def cif_mensaje():
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
    )
    public_key = private_key.public_key()

    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Guardar la clave pública en un archivo
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    # Leer el mensaje del usuario
    message = input("Ingresa el mensaje a cifrar: ").encode()

    # Cifrar el mensaje con la clave pública
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    resultado = ciphertext
    with open("Cif_asyc.txt", "wb") as archivo:
            archivo.write(resultado)
    print(f"Consulta guardada en Cif_asyc.txt")
    
    nombre_archivo = f"Cif_asyc.txt" #aqui ponemos el nombre del script 
    hash_resultado = generar_hash_archivo(nombre_archivo)
    print(f"Tarea ejecutada: Cif_asyc.txt")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hash del reporte: {hash_resultado}")
    print(f"Ubicación del archivo: {os.path.abspath(nombre_archivo)}")

def cif_file():
    file_path = input("Ingresa la ruta del archivo que deseas cifrar: ")
    with open(file_path, 'rb') as f:
                plaintext = f.read()

    ciphertext = public_key.encrypt(
                plaintext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)
    hash_resultado = generar_hash_archivo(encrypted_file_path)
    print(f"Tarea ejecutada: {encrypted_file_path}")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hash del reporte: {hash_resultado}")
    print(f"Ubicación del archivo: {os.path.abspath(encrypted_file_path)}")

def cifrar_archivo(input_file, output_file, desplazamiento):
    try:
        # Abre el archivo de entrada en modo lectura
        with open(input_file, 'r', encoding='utf-8') as archivo_entrada:
            texto = archivo_entrada.read()  # Lee todo el contenido del archivo
        
        # Llama a la función de cifrado César para cifrar el texto leído
        texto_cifrado = cifrar_cesar(texto, desplazamiento)
        
        # Abre el archivo de salida en modo escritura
        with open(output_file, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto_cifrado)  # Escribe el texto cifrado en el archivo de salida
        
        # Mensaje de confirmación
        print(f'El archivo "{input_file}" ha sido cifrado y guardado como "{output_file}".')
        hash_resultado = generar_hash_archivo(output_file)
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Hash del reporte: {hash_resultado}")
        print(f"Ubicación del archivo: {os.path.abspath(output_file)}")
    except FileNotFoundError:
        # Manejo de errores si el archivo de entrada no se encuentra
        print(f'Lo siento, no se pudo encontrar el archivo "{input_file}".')

def menuces():
    while True:
        opc=input("1. Encriptar un archivo\n2. Desencriptar un archivo")
        if opc == "1":
            # Solicita al usuario el nombre del archivo de texto a cifrar
            input_file = input("Introduce el nombre del archivo de texto (incluyendo la extensión .txt): ")
            # Solicita al usuario el desplazamiento para el cifrado
            desplazamiento = int(input("Introduce el desplazamiento para el cifrado (un número entero): "))
            # Define el nombre del archivo de salida, añadiendo "_cifrado" al nombre original
            output_file = f"{input_file.split('.')[0]}_cifrado.txt"
            cifrar_archivo(input_file, output_file, desplazamiento)
        elif opc == "2":
            file = input("Archivo a desencriptar: ")
            with open(file, "r", encoding="utf-8") as archivo:
                contenido_cifrado = archivo.read()
            
            desplazamiento = int(input("Ingresa el valor de desplazamiento: "))
            contenido_desencriptado = desencri_cesar(contenido_cifrado, desplazamiento)

            with open("archivo_desencriptado.txt", "w", encoding="utf-8") as archivo:
                archivo.write(contenido_desencriptado)
            
            nombre_archivo = f"Info_api.txt" #aqui ponemos el nombre del script
            print("El archivo ha sido desencriptado y guardado como 'archivo_desencriptado.txt'.")
            hash_resultado = generar_hash_archivo(nombre_archivo)
            print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Hash del reporte: {hash_resultado}")
            print(f"Ubicación del archivo: {os.path.abspath(nombre_archivo)}")

        elif opc == "3":
            break
        else:
            print("Opcion invalida, intente otra vez")

def desencri_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            # Determinar si la letra es mayúscula o minúscula
            limite = 65 if letra.isupper() else 97
            # Desencriptar la letra
            resultado += chr((ord(letra) - limite - desplazamiento) % 26 + limite)
        else:
            # Mantener caracteres no alfabéticos sin cambios
            resultado += letra
    return resultado

def cifrar_cesar(texto, desplazamiento):
    # Inicializa una cadena vacía para almacenar el resultado cifrado
    resultado = ""
    
    for letra in texto:
        # Cifrar mayúsculas
        if letra.isupper():
            # Aplica el desplazamiento y ajusta el valor para que se mantenga dentro del rango de letras mayúsculas
            resultado += chr((ord(letra) + desplazamiento - 65) % 26 + 65)
        # Cifrar minúsculas
        elif letra.islower():
            # Aplica el desplazamiento y ajusta el valor para que se mantenga dentro del rango de letras minúsculas
            resultado += chr((ord(letra) + desplazamiento - 97) % 26 + 97)
        else:
            # No cifrar caracteres que no son letras
            resultado += letra  
    return resultado
def menu():
    print("\nCifrado")
    print("1. Cifrado Asimetrico")
    print("2. Cifrado Cesar")
    print("3. Salir")

#If para hacer uso de la funcion 
def main():
    while True:
        menu()
        opcion=input("--->")
        if opcion == "1":
            asyc()
        elif opcion=="2":
            menuces()
        elif opcion== "3":
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__=="__main__":
    main()
