#!/usr/bin/sh

rm -rf dist build *.spec
pyinstaller src/*.py --onefile --name wikilibs_parser
cp dist/wikilibs_parser ..
rm -rf dist build *.spec