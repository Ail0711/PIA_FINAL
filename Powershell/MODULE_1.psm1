<#
.SYNOPSIS
Hashes de los archivos de una carpeta especificada.

.DESCRIPTION
Esta función revisa todos los archivos de una carpeta y calcula el hash de cada archivo utilizando el algoritmo SHA256. Mediante la API de VirusTotal,
este realiza una consulta del estado de cada hash obtenido.

.PARAMETER folderPath
La ruta completa de la carpeta a la que se obtendran los hashes del archivo.
.PARAMETER apikey
La ApiKey obtenida de la Api VirusTotal al registrarse.

.EXAMPLE
Get-VirusTotalReport -folderPath C:\MyFiles -apikey s8dk2h0q...

.EXAMPLE
$information = Get-VirusTotalReport -folderPath C:\MyFiles -apikey s8dk2h0q...

.NOTES
Para evitar errores debe asegurarse de que la apikey no haya caducado.
#>
function Get-VirusTotalReport {
    param(
        [Parameter(Mandatory)][string]$folderPath = $(Read-Host "Ingresa la ruta de la carpeta: "),
        [Parameter(Mandatory)][string]$apiKey = $(Read-Host "Ingresa tu apikey: ")
    )

    $url = "https://www.virustotal.com/vtapi/v2/file/report"
    $algorithm = "SHA256"

    $verifyingPath = (Test-Path -Path $folderPath)

    if ($verifyingPath) {
        try {
            $listFiles = Get-ChildItem -Path $folderPath -File
            foreach ($file in $listFiles) {
                $hash = Get-FileHash $file.FullName -Algorithm $algorithm

                try {
                    $params = @{
                        apikey = $apiKey
                        resource = $hash.Hash
                    }

                    $response = Invoke-RestMethod -Uri $url -Method Get -Body $params
                    Write-Host "El archivo " $file

                    Write-Host "Respuesta completa de VirusTotal: $($response | Out-String)"

                    foreach ($info in $response.PSObject.Properties) {
                        Write-Host "$($info.Name): $($info.Value)"
                    }

                } catch {
                    Write-Error "Error al realizar la solicitud a la API de VirusTotal: $_"
                }

                Start-Sleep -Seconds 3
            }
        } catch {
            Write-Error "Error al obtener el hash de los archivos: $_"
        }
    } else {
        Write-Host "No existe la carpeta especificada."
    }
}
