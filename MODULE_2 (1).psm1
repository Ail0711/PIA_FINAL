#USO DEL SISTEMA
<#
.SYNOPSIS
Muestra los archivos ocultos de una carpeta especificada

.DESCRIPTION
La función `Get-HiddenFile` muestra en la pantalla los archivos ocultos de la carpeta ya especificada

.PARAMETER PATHH
Es donde se almacena la ruta de acceso a la carpeta que deseamos ver

.EXAMPLE
Por favor, ingrese la ruta de la carpeta donde desea buscar archivos ocultos: 'Ruta de acceso'

Archivos ocultos en ''Ruta de acceso'':
C:\Ruta\De\Acceso\archivo.ini
C:\Ruta\De\Acceso\archivo.txt

#>


# funcion para obtener los archivos ocultos 
function Get-HiddenFiles {
    param (
        [string]$Pathh
    )
    Get-ChildItem -Path $Pathh -Force -File | Where-Object { $_.Attributes -match "Hidden" }

     try {
        # Verifica si la carpeta existe
        if (-Not (Test-Path -Path $Pathh)) {
            throw "La carpeta especificada no existe: $Pathh"
        }

        # Listar solo los archivos ocultos
        $hiddenfiles = Get-ChildItem -Path $Pathh -Force -File | Where-Object { $_.Attributes -match "Hidden" }

        if ($hiddenfiles) {
            Write-Output "Archivos ocultos en '$Pathh':"
            $hiddenfiles | ForEach-Object { Write-Output $_.FullName }
        } else {
            Write-Output "No se encontraron archivos ocultos en '$Pathh'."
        }
    } catch {
        Write-Error "Ocurrió un error: $_"
    }



}

# variable para ingresar la ruta de la carpeta para luego mandarla a la funcion
$Path = Read-Host "Por favor, ingrese la ruta de la carpeta donde desea buscar archivos ocultos"

# Llamamos a la funcion diciendole que la variable Path corresponde al valor Pathh de la funcion
Get-HiddenFiles -Pathh $Path
