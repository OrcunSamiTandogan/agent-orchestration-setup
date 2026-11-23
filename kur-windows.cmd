@echo off
setlocal DisableDelayedExpansion
where wsl.exe >nul 2>&1
if errorlevel 1 goto no_wslg
wsl.exe -d Ubuntu-24.04 --exec /usr/bin/test -d /mnt/wslg
if errorlevel 1 goto no_wslg
pushd "%~dp0" || goto failed
wsl.exe -d Ubuntu-24.04 -- bash ./masaustune-kur.sh
set "AA_RESULT=%ERRORLEVEL%"
if not "%AA_RESULT%"=="0" goto failed_in_source
echo Agent Orchestration Setup is installed. Opening the app...
echo To open it again, run ac-windows.cmd from this folder.
call .\ac-windows.cmd
set "AA_RESULT=%ERRORLEVEL%"
popd
exit /b %AA_RESULT%

:failed_in_source
popd
goto failed

:no_wslg
echo Ubuntu-24.04 or WSLg is not ready. See docs\windows.md.
pause
exit /b 1

:failed
echo Installation failed. See docs\windows.md.
pause
exit /b 1
