#!/bin/bash

#Conexiones de red activas
monitor_network() {
    local protocol=$1
    local port=$2

    echo "Monitoreando conexiones activas en el puerto $port con el protocolo $protocol..."
    # Verificar no se encuentran conexiones
    if ! netstat -anp "$protocol" | grep ":$port"; then
        echo "Error: No se encontraron conexiones activas en el puerto $port con el protocolo $protocol."
        return 1  
    fi
    return 0  
}

#Genera un reporte 
generate_report() {
    local protocol=$1
    local port=$2
    local report_file="network_report_$(date +%Y%m%d_%H%M%S).txt"

    echo "Generando reporte en $report_file..."
    # Verificar si netstat falla o no encuentra conexiones para el reporte
    if ! netstat -anp "$protocol" | grep ":$port" > "$report_file"; then
        echo "Error: No se pudo generar el reporte. No se encontraron conexiones activas."
        return 1  
    fi

    echo "Reporte generado con éxito: $report_file"
    return 0  
}

#Estado del monitoreo
view_monitor_status() {
    if [[ -z "$protocol" || -z "$port" ]]; then
        echo "Estado del monitoreo: No se han definido parámetros. Cambie los parámetros de entrada primero."
    else
        echo "Estado del monitoreo: Protocolo = $protocol, Puerto = $port"
    fi
}

# Función para cambiar parámetros de entrada con validación
change_parameters() {
    read -p "Protocolo (tcp/udp): " protocol
    read -p "Puerto a monitorear: " port
    
    # Validar que el protocolo ingresado sea válido
    if [[ "$protocol" != "tcp" && "$protocol" != "udp" ]]; then
        echo "Error: Protocolo no válido. Solo se permite 'tcp' o 'udp'."
        return 1  
    fi

    # Validar que el puerto ingresado sea un número entre 1 y 65535
    if ! [[ "$port" =~ ^[0-9]+$ ]] || ((port < 1 || port > 65535)); then
        echo "Error: Puerto no válido. Debe ser un número entre 1 y 65535."
        return 1  
    fi

    return 0  
}

# Función para el menú
menu() {
    local protocol port
    while true; do
        echo "----------------------------"
        echo "   MENÚ  "
        echo "----------------------------"
        echo "1) Monitorear conexiones"
        echo "2) Generar reporte"
        echo "3) Ver estado del monitoreo"
        echo "4) Definir o cambiar parametros"
        echo "5) Salir"
        echo "----------------------------"
        read -p "Seleccione una opción: " option

        case $option in
            1)
                # Validación de parametros
                if [[ -z "$protocol" || -z "$port" ]]; then
                    echo "Error: Protocolo o puerto no definidos. Cambie los parámetros de entrada primero."
                else
                    monitor_network "$protocol" "$port"
                    if [[ $? -ne 0 ]]; then
                        echo "Error durante el monitoreo de red."
                    fi
                fi
                ;;
            2)
                # Validación de parametros
                if [[ -z "$protocol" || -z "$port" ]]; then
                    echo "Error: Protocolo o puerto no definidos. Cambie los parámetros de entrada primero."
                else
                    generate_report "$protocol" "$port"
                    if [[ $? -ne 0 ]]; then
                        echo "Error durante la generación del reporte."
                    fi
                fi
                ;;
            3)
                
                view_monitor_status
                ;;

            4)
                change_parameters
                ;;

            5)
                echo "Saliendo..."
                break
                ;;
            *)
                echo "Opción no válida. Inténtelo de nuevo."
                ;;
        esac
    done
}

menu
