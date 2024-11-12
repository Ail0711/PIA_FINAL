import sys
import logging
import modulo2 as shodan
import Abuse_data as abuse
import scanning as scann
import modulo5 as crypt
import hashes as has

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='Report_acces.log', 
                    filemode='a')

def user(para):
    while True:
        entrada1 = input(para).strip()
        if entrada1:
            return entrada1
        else:
            print("La entrada no puede estar en blanco. Por favor, intenta de nuevo.")

def menu():
    print("\nMenú de Modulos del script:")
    print("1. Shodan API")
    print("2. AbuseIPDB")
    print("3. Scanner de puertos")
    print("4. Devices IP")
    print("5. Tipos de cifrado")
    print("6. Salir")

def sho():
    shodan.iniciar_menu()

def abu():
    abuse.main()

def scanning():
    scann.main()
    
def cryptograph():
    crypt.main()

def hashess():
    has.main()

def main():
    usu = user("Usuario:\n ")
    logger=logging.getLogger(usu)
    logger.info(f'El usuario {usu} ha iniciado el script pricipal')
    while True:
        menu()
        opcion=input("--->")
        if opcion == "1":
            logger.info(f'El usuario {usu} ha iniciado el script modulo 1')
            sho()
        elif opcion=="2":
            logger.info(f'El usuario {usu} ha iniciado el script modulo 2')
            abu()    
        elif opcion=="3":
            logger.info(f'El usuario {usu} ha iniciado el script modulo 3')
            scanning()
        elif opcion=="4":
            logger.info(f'El usuario {usu} ha iniciado el script modulo 4')
            hashess()
        elif opcion=="5":
            logger.info(f'El usuario {usu} ha iniciado el script modulo 5')
            cryptograph()
        elif opcion== "6":
            logger.info(f'El usuario {usu} ha salido del script')
            sys.exit()
        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__=="__main__":
    main() 