#!/bin/bash

rm -rf dist build *.spec
pip3 install pyinstaller
pip3 install pytest
pip3 install pytest-cov
pyinstaller Parser/*.py --onefile --name wikilibs_parser
cp dist/wikilibs_parser .
rm -rf dist build *.spec
rm -rf `find . -name "__pycache__"`
