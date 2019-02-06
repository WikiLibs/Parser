#!/usr/bin/python3.6

import sys
import os
import re

comments = ['<!--', '-->']
is_comments = False
depth = 0
output = []


def open_file(file_name):
    if os.path.isfile(file_name) == False:
        sys.stderr.write("ERROR : file not found\n")
        exit(84)
    file = open(file_name, 'r')
    tmp = file.read()
    return tmp


def epur_line_from_comments(string):
    global depth
    global output

    if '<tr' in string and '</tr>' in string or depth > 0:
        output.append(string[0:string.find('<!--')] +
                      string[string.find('-->') + 3:len(string)])


def check_comments(mode, string):
    global is_comments

    if comments[mode] in string and mode == 0:
        is_comments = True
        if comments[1] in string:
            epur_line_from_comments(string)
    elif comments[mode] in string and mode == 1:
        is_comments = False


def check_tr(string):
	global depth
	global output

	if '<tr' in string:
		depth += 1
		if "<tr" in string and '</tr>' not in string:
			output.append(string)
	if '</tr>' in string and depth > 0:
		output.append(string)
		depth -= 1
	elif '<tr' in string and '</tr>' in string:
		output.append(string)


def pushSymbol(json):
    print(json)


def getBetweenTwoChar(string, sub1, sub2):
	tab = []
	searching = False
	tmp = ""

	for i in range(len(string)):
		if string[i] == sub1:
			searching = True
			tmp = ""
			continue
		if string[i] == sub2:
			searching = False
			tmp = re.sub(' +', ' ', tmp).strip()
			if len(tmp) > 0:
				tab.append(tmp)
			continue

		if searching:
			tmp += string[i]

	return tab


def catTr(tab):
	newTab = []
	tmp = ""
	adding = False

	for elem in tab:
		if "<tr" in elem:
			tmp = ""
			adding = True
		tmp += elem
		if "</tr" in elem:
			newTab.append(re.sub(' +', ' ', tmp).strip())
			adding = False

	return newTab


def main():
	global comments
	global is_comments
	global depth
	global output

	if len(sys.argv) == 1:
		print("USAGE\n\tpython parser.py [file...]\n\t\t[file]: .html files")
		exit(84)

	for filename in sys.argv[1:]:
		depth = 0
		depth_o = depth
		output = []
		is_comments = False
		file_content = open_file(filename).split('\n')

		for i in file_content:
			check_comments(0, i)
			if not is_comments:
				check_tr(i)
				if depth > 0 and depth_o == depth:
					output.append(i)
				depth_o = depth
			check_comments(1, i)

		f = open("data_parsed.txt", "a")
		f.write("BEGIN ####################################################################\n")
		output = catTr(output)
		for i in output:
			tmpTab = getBetweenTwoChar(i, ">", "<")
			for i in range(len(tmpTab)):
				if i != 0:
					f.write(" ")
				f.write(tmpTab[i])
			f.write("\n")
			#f.write(i + "\n")
		f.write("END ######################################################################\n")


if __name__ == '__main__':
	main()
