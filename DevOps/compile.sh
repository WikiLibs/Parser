#!/bin/bash

rm -rf dist build *.spec
pip3 install pyinstaller
pyinstaller Parser/Src/*.py --onefile --name wikilibs_parser
cp dist/wikilibs_parser .
rm -rf dist build *.spec