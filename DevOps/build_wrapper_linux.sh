mkdir Wrapper-C/Linux/mybins
cd Wrapper-C/Linux/mybins
../bin2c -b ../../../wikilibs_parser mybin
cd ../..
./run.sh
cp build/Linux/Wrapper_Linux ../wikilibs_parser_wrapper_linux
cd ..