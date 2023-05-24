@echo off
set PY_INTERPRETER=python
set "REQS_INSTALLED="
set "INSTALLED_FILE=dependencies_installed.flag"
where /Q %PY_INTERPRETER% || (
    echo %PY_INTERPRETER% not found in PATH
    echo Please install Python 3 and add it to your PATH environment variable.
    pause
    exit /B 1
)
%PY_INTERPRETER% --version 2>&1 | findstr /i "python 3" || (
    echo %PY_INTERPRETER% is not a Python 3 interpreter.
    echo Please run this script with a Python 3 interpreter.
    pause
    exit /B 1
)
echo Checking dependencies...
if exist "%INSTALLED_FILE%" (
    echo Dependencies are already installed.
    set "REQS_INSTALLED=1"
) else (
    echo Installing dependencies...
    %PY_INTERPRETER% -m pip install -r requirements.txt || (
        echo An error occurred during installation. Press any key to exit.
        pause >nul
        exit /B 1
    )
    echo Dependencies successfully installed. Creating flag file...
    echo Installed on %date% %time% > "%INSTALLED_FILE%"
)
echo Running the script...
start /B "" pythonw.exe main.py
exit