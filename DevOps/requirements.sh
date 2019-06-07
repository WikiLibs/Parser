#!/bin/bash

pip3 install pyinstaller
pip3 install pytest
pip3 install pytest-cov
pip3 install doxypypy
pip3 install requests

OS=`awk -F= '$1=="ID" { print $2 ;}' /etc/os-release`
if [ $OS = "ubuntu" ] || [ $OS = "fedora" ]; then
    sudo apt-get install doxygen
fi
