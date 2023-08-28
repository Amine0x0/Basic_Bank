#!/bin/bash

venv_dir="env"

if [ -d "$venv_dir" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    echo "Wait until the environment is fully created ..."
    python3 -m venv "$venv_dir"
    source "$venv_dir/bin/activate"
    pip install pyfiglet
fi

clear
python3 bank_prog.py

