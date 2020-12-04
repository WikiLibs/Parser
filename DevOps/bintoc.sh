#!/bin/sh

./bintoc/build/bintoc wikilibs_parser output.h
tail -n +3 output.h > output1
mv output1 output.h
head -n -17 output.h > output1
mv output1 output.h

