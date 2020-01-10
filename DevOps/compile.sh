#!/bin/bash

pyinstaller Parser/*.py PyQt/*.py --onefile --name wikilibs_parser
cp dist/wikilibs_parser .
rm -rf dist build *.spec
rm -rf `find . -name "__pycache__"`
