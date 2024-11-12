def desencriptar_cesar(texto, desplazamiento):
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

# Leer el contenido del archivo cifrado
file = input("Archivo a desencriptar: ")
with open(file, "r", encoding="utf-8") as archivo:
    contenido_cifrado = archivo.read()

# Desencriptar el contenido
desplazamiento = int(input("Ingresa el valor de desplazamiento: "))
contenido_desencriptado = desencriptar_cesar(contenido_cifrado, desplazamiento)

# Guardar el contenido desencriptado en un nuevo archivo
with open("archivo_desencriptado.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido_desencriptado)

print("El archivo ha sido desencriptado y guardado como 'archivo_desencriptado.txt'.")
