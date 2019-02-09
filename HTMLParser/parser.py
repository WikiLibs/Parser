#!/usr/bin/python3.6

import sys
import os
import re

comments = ['<!--', '-->']
is_comments = False
depth = 0
output = []
trTab = []


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

def getTabNb(string):
	tmp = ""
	for i in range(len(string)):
		if string[i].isdigit():
			tmp += string[i]
		else:
			break
	
	if len(tmp) > 0:
		tabs = ""
		nb = int(tmp)
		while nb > 0:
			tabs += "\t"
			nb -= 1
		return tabs
	else:
		return ""

def getBetweenTwoSep(string, sub1, sub2):
	tab = []
	searching = False
	tmp = ""
	tab.append(getTabNb(string))

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

def catTr(tab, i, recur):
	global trTab
	found = False
	index = i
	tmp = ""

	while index < len(tab):
		if "<tr" in tab[index]:
			if found == True:
				index = catTr(tab, index, recur + 1) + 1
				continue
			else:
				found = True
				tmp = ""
		tmp += tab[index] + " "
		if "</tr" in tab[index]:
			tmp = str(recur) + re.sub(' +', ' ', tmp).strip()
			trTab.append(tmp)
			return index
		index += 1
	return 0


def main():
	global comments
	global is_comments
	global depth
	global output
	global trTab

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
		'''for tmp in output:
			print("1:", tmp)'''
		#output = catTr(output)
		catTr(output, 0, 0)
		for tmp in trTab:
			print("2:", tmp)
		for i in trTab:
			tmpTab = getBetweenTwoSep(i, ">", "<")
			for i in range(len(tmpTab)):
				if i > 1:
					f.write(" ")
				f.write(tmpTab[i])
			f.write("\n")
		f.write("END ######################################################################\n")


if __name__ == '__main__':
	main()
