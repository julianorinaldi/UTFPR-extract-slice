#!/bin/bash

set -e

if [ ! -d "extract-slice-venv" ]; then
    python3.12 -m venv extract-slice-venv
fi

source ./extract-slice-venv/bin/activate

pip install -r requirements.txt