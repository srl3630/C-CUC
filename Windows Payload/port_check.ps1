$mactemp = Get-CimInstance win32_networkadapterconfiguration | select description, macaddress | where {$_.MACAddress -ne $null } | where {$_.Description -match "Ethernet" } | where {$_.Description -NotMatch "vmware" }
$mac = $mactemp[0].macaddress

$port = 0;
$tempVal = [convert]::toint32("$($mac[0])$($mac[1])",16)
$port= $port+$tempval
$tempVal = [convert]::toint32("$($mac[3])$($mac[4])",16)
$port= $port+$tempval
$tempVal = [convert]::toint32("$($mac[6])$($mac[7])",16)
$port= $port+$tempval
$tempVal = [convert]::toint32("$($mac[9])$($mac[10])",16)
$port= $port+$tempval
$tempVal = [convert]::toint32("$($mac[12])$($mac[13])",16)
$port= $port+$tempval
$tempVal = [convert]::toint32("$($mac[15])$($mac[16])",16)
$port= $port+$tempval

$path = Convert-Path .
New-Item "$($path)\port.txt" -type file -force -value $port