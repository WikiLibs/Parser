mkdir Wrapper-C/Windows/mybins
cd Wrapper-C/Windows/mybins
../bin2c.exe -b ../../../wikilibs_parser.exe mybin
cd ../..
./run.sh
cp build/Windows/Wrapper_Windows ../wikilibs_parser_wrapper_windows
cd ..