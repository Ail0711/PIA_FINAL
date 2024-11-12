# Función para verificar el uso del CPU
function cpu_usage {
    param (
        [int]$CPU_THRESHOLD = 80,
	[string]$ReportPath
    )
    $cpuLoad = Get-WmiObject -Class Win32_Processor | Select-Object -ExpandProperty LoadPercentage
    $cpuUsage = [math]::Round([double]$cpuLoad, 2)
    
    Write-Host "Uso del CPU: $cpuUsage%" | Out-File -FilePath $ReportPath -Append
    
    if ($cpuUsage -gt $CPU_THRESHOLD) {
        Write-Host "ALERTA: El uso del CPU está por encima del $CPU_THRESHOLD%" | Out-File -FilePath $ReportPath -Append
    }
}

# Función para verificar el uso de la memoria
function memory_usage {
    param (
        [int]$MEMORY_THRESHOLD = 80,
	[string]$ReportPath
    )
    $memInfo = Get-WmiObject Win32_OperatingSystem
    $totalMem = $memInfo.TotalVisibleMemorySize
    $freeMem = $memInfo.FreePhysicalMemory
    $usedMem = (($totalMem - $freeMem) / $totalMem) * 100
    $usedMem = [math]::Round($usedMem, 2)
    
    Write-Host "Uso de la memoria: $usedMem%" | Out-File -FilePath $ReportPath -Append
    
    if ($usedMem -gt $MEMORY_THRESHOLD) {
        Write-Host "ALERTA: El uso de la memoria está por encima del $MEMORY_THRESHOLD%" | Out-File -FilePath $ReportPath -Append
    }
}

# Función para verificar el uso del disco
function disk_usage {
    param (
        [int]$DISK_THRESHOLD = 80,
	[string]$ReportPath
    )
    $disk = Get-PSDrive -Name C
    $usedDisk = ($disk.Used / ($disk.Used + $disk.Free)) * 100
    $usedDisk = [math]::Round($usedDisk, 2)
    
    Write-Host "Uso del disco: $usedDisk%" | Out-File -FilePath $ReportPath -Append
    
    if ($usedDisk -gt $DISK_THRESHOLD) {
        "ALERTA: El uso del disco está por encima del $DISK_THRESHOLD%" | Out-File -FilePath $ReportPath -Append
    }
}

# Función para verificar el uso de la red
function network_usage {
    param (
        [int]$NETWORK_THRESHOLD = 1000, # En KB/s
	[string]$ReportPath
    )
    $netStats = Get-NetAdapterStatistics
    $receivedBytes = 0
    $netStats | ForEach-Object { $receivedBytes += $_.ReceivedBytesPersec }
    
    $netUsageKB = [math]::Round($receivedBytes / 1KB, 2)
    
    "Uso de la red: $netUsageKB KB/s" | Out-File -FilePath $ReportPath -Append
    
    if ($netUsageKB -gt $NETWORK_THRESHOLD) {
        "ALERTA: El uso de la red está por encima del $NETWORK_THRESHOLD KB/s" | Out-File -FilePath $ReportPath -Append
    }
}

# Función principal para verificar el uso del sistema
function Check_System_Usage {
    param (
        [int]$CPU_THRESHOLD = 80,
        [int]$MEMORY_THRESHOLD = 80,
        [int]$DISK_THRESHOLD = 80,
        [int]$NETWORK_THRESHOLD = 1000,
	[string]$ReportPath
    )

    Write-Host "Verificando el uso del sistema..." | Out-File -FilePath $ReportPath -Append
    
    # Llamada a las funciones de verificación individuales
    cpu_usage -CPU_THRESHOLD $CPU_THRESHOLD -ReportPath $ReportPath
    memory_usage -MEMORY_THRESHOLD $MEMORY_THRESHOLD -ReportPath $ReportPath
    disk_usage -DISK_THRESHOLD $DISK_THRESHOLD -ReportPath $ReportPath
    network_usage -NETWORK_THRESHOLD $NETWORK_THRESHOLD -ReportPath $ReportPath
}

# Llamada a la función principal
$ReportPath = Read-Host "Por favor, ingrese la ruta completa donde desea guardar el reporte"
Check_System_Usage -ReportPath $ReportPath
