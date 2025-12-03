#!/usr/bin/bash

DIRECTORY="venv"

# Create Environment if directory doesn't exist
if [ ! -d $DIRECTORY ]; then
    echo "Virtual environment not found... Creating environment"
    python3 -m venv venv
fi

if [[ -z "$VIRTUAL_ENV" ]]; then

    # Activate Virtual environment
    echo "Activating virtual environment..."
    if [ -d "venv" ]; then
        if [ -f "venv/bin/activate" ]; then
            source venv/bin/activate
        elif [ -f "venv/Scripts/activate" ]; then
            # Common path for Windows Git Bash
            source venv/Scripts/activate
        else
            echo "Error: Virtual environment activation script not found."
            exit 1
        fi
        pip install -r requirements.txt
    fi

fi

export FLASK_APP=flask_site:create_application
export FLASK_ENV=development

echo "FLASK_APP set to: $FLASK_APP"
echo "FLASK_ENV set to: $FLASK_ENV"

echo "Starting Flask Server..."
flask run