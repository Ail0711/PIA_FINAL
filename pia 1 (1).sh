#!/bin/bash

menu() {
    echo "Seleccione una opcion:"
    echo "1.- Escanear puertos"
    echo "2.- Generar reporte"
    echo "3.- Volver a escanear"
    echo "4.- Salir"
}

scan_ports() {
    read -p "Ingrese la dirección IP o el dominio: " direccion
    read -p "Ingrese el rango de puertos: " rango
    nmap -p $rango $direccion > result.txt
    if [ $? -eq 0 ]; then
        echo "Escaneo completado. Resultados guardados en result.txt"
    else
        echo "Error al realizar el escaneo."
    fi
}

gen_report() {
    if [ -f result.txt ]; then
        cat result.txt | grep "open" > reporte.txt
        echo "Reporte generado en reporte.txt"
    else
        echo "No se encontró el archivo de resultados. Realice un escaneo primero."
    fi
}

rescan() {
    scan_ports
}

main() {
    while true; do
        mostrar_menu
        read -p "Seleccione una opción: " opcion
        case $opcion in
            1)
                scan_ports
                ;;
            2)
                gen_report
                ;;
            3)
                rescan
                ;;
            4)
                echo "Salida"
                exit 0
                ;;
            *)
                echo "Opción no válida"
                ;;
        esac
    done
}


main
