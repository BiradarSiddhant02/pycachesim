#!/bin/bash

pyinstaller main.py --onefile --noconsole --name pycachesim
sudo cp ./dist/pycachesim /bin
