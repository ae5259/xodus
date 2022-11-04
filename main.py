#! /usr/bin/env python

import os
import sys
from utils import xodo_text
from utils import colors

commands = ['list','add','done','current','guide','clear']

def add_todo(xodo):
	with open("xodo.txt","rt") as r_file:
		#reading file
			r = r_file.read()
			with open("xodo.txt","wt") as w_file:
				# checking if file is empty
				if len(r.strip())==0:
					# adding todo
					w_file.write("1." + xodo + '\n')
					# log message
					print(f"{colors.OKGREEN}XoDo has been added successfully!\n{colors.ENDC}List xodos: xodo list")
				else:
					# if it's not empty, get existing xodos
					exist_xodos = r
					# writing new xodo
					w_file.write(exist_xodos + str(len(exist_xodos.split('\n'))) + "." + xodo + '\n')
					# log message
					print(f"{colors.OKGREEN}XoDo has been added successfully!\n{colors.ENDC}List xodos: xodo list")




def main():
	# command validation
	try:
		command = sys.argv[1]
	except IndexError:
		print(xodo_text)
		#stop program
		return

	# if file does not exist, create it
	if not os.path.exists("xodo.txt"):
		os.popen("echo > xodo.txt")


	# command not found
	if command not in commands:
		print(f"{colors.FAIL}Command {command} is not found.\n\n{colors.ENDC}Guide: xodo guide")

	# adding xodo
	if command == "add":
		xodo = input("Enter your xodo: ")
		add_todo(xodo)


main()