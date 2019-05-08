#!/bin/bash

rm -rf dist build *.spec
rm -rf `find . -name "__pycache__"`
rm -rf `find . -name ".pytest_cache"`
rm -rf coverage.xml
