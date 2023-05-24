#!/bin/bash

PY_INTERPRETER=python
REQS_INSTALLED=""
INSTALLED_FILE=dependencies_installed.flag

if ! command -v $PY_INTERPRETER &> /dev/null
then
    echo "$PY_INTERPRETER not found in PATH"
    echo "Please install Python 3 and add it to your PATH environment variable."
    exit 1
fi

if ! $PY_INTERPRETER --version 2>&1 | grep -q "Python 3"
then
    echo "$PY_INTERPRETER is not a Python 3 interpreter."
    echo "Please run this script with a Python 3 interpreter."
    exit 1
fi

echo "Checking dependencies..."
if [ -f "$INSTALLED_FILE" ]
then
    echo "Dependencies are already installed."
    REQS_INSTALLED=1
else
    echo "Installing dependencies..."
    $PY_INTERPRETER -m pip install -r requirements.txt || {
        echo "An error occurred during installation. Press any key to exit."
        exit 1
    }
    echo "Dependencies successfully installed. Creating flag file..."
    echo "Installed on $(date) $(time)" > "$INSTALLED_FILE"
fi

echo "Running the script..."
python main.py &
exit