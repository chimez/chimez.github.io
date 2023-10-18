#!/usr/bin/env bash

python3 -m venv nikola 
source nikola/bin/activate
python -m pip install -U pip setuptools wheel
python -m pip install -U "Nikola[extras]"
nikola plugin -i orgmode
