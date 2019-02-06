#!/usr/bin/python3.6

import sys
import os

comments = ['<!--', '-->']
is_comments = False
depth = 0
output = []

def open_file(file_name) :
        if os.path.isfile(file_name) == False:
                sys.stderr.write("file not found\n")
                exit(84)
        file = open(file_name, 'r')
        tmp = file.read();
        return tmp

def epur_line_from_comments(string) :
        global depth
        global output

        if '<tr' in string and '</tr>' in string or depth > 0 :
                output.append(string[0:string.find('<!--')] + \
                      string[string.find('-->') + 3:len(string)])

def check_comments(mode, string) :
        global is_comments

        if comments[mode] in string and mode == 0:
                is_comments = True
                if comments[1] in string :
                        epur_line_from_comments(string)
        elif comments[mode] in string and mode == 1:
                is_comments = False

def check_tr(string) :
        global depth
        global output

        if '<tr' in string :
                depth += 1
        if '</tr>' in string and depth > 0:
                output.append(string)
                depth -= 1
        elif '<tr' in string and '</tr>' in string :
                output.append(string)

if len(sys.argv) > 1 :
        for filename in sys.argv[1:] :
                depth = 0
                depth_o = depth
                output = []
                is_comments = False
                file_content = open_file(filename).split('\n')
                data_parsed = []

                for i in file_content :
                        check_comments(0, i)
                        if not is_comments :
                                check_tr(i)
                                if depth > 0 and depth_o == depth:
                                        output.append(i)
                                depth_o = depth
                        check_comments(1, i)

                f = open("data_parsed.txt", "a")
                f.write("BEGIN ####################################################################\n")
                for i in output :
                        f.write(i + "\n")
                f.write("END ######################################################################\n")
        print("html was parsed and output is in data_parsed.txt")

#python parser.py u_test/hard_test u_test/Vector2_8h.html
