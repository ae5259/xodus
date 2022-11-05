#! /usr/bin/env python

import time
import os
import sys
from utils import xodo_text, guide_text
from utils import colors
from utils import done_xodo, current_xodo, unfinished_xodo

commands = ['list','add','done','current','guide','clear']

def add_todo(xodo):
	with open("xodo.txt","rt") as r_file:
		#reading file
			r = r_file.read()
			with open("xodo.txt","wt") as w_file:
				# checking if file is empty
				if len(r.strip())==0:
					# adding todo
					w_file.write("1." + xodo + unfinished_xodo + '\n')
					# log message
					print(f"{colors.OKGREEN}XoDo has been added successfully!\n{colors.ENDC}List xodos: xodus list")
				else:
					# if it's not empty, get existing xodos
					exist_xodos = r
					# writing new xodo
					w_file.write(exist_xodos + str(len(exist_xodos.split('\n'))) + "." + xodo + unfinished_xodo + '\n')
					# log message
					print(f"{colors.OKGREEN}XoDo has been added successfully!\n{colors.ENDC}List xodos: xodus list")


def xodo_list():
	with open('xodo.txt','rt') as file:
		xodos = file.read().strip()
		if len(xodos)==0:
			print("No xodos!")
			print(f"{colors.OKGREEN}To add xodo -> xodus add")
			return
		print(xodos) 


def xodo_guide():
	print(guide_text)

def mark_current_xodo(xodo_id):
	with open("xodo.txt","rt") as file:
		r = file.read().strip()
		if len(r.split())==0:
			print(f"{colors.FAIL}No xodos found.\n\n{colors.ENDC}Guide: xodus guide")
		else:
			xodo = r.split('\n')[int(xodo_id)-1]
			new_xodo = xodo.replace(unfinished_xodo, current_xodo)
			r = r.replace(r.split('\n')[int(xodo_id)-1], new_xodo)
			with open('xodo.txt',"w+") as f:
				f.write(r)
			print(f"Current xodo is: {colors.OKGREEN}{new_xodo}")
def main():
	# if file does not exist, create it
	if not os.path.exists("xodo.txt"):
		os.popen("echo > xodo.txt")


	# command validation
	try:
		command = sys.argv[1]
	except IndexError:
		print(xodo_text)
		#stop program
		return

	if command == "current":
		time.sleep(1)
		try:
			id = sys.argv[2]
		except IndexError:
			print("Not enough arguments.")
			return
		mark_current_xodo(id)

	# command not found
	if command not in commands:
		print(f"{colors.FAIL}Command {command} is not found.\n\n{colors.ENDC}Guide: xodus guide")

	# adding xodo
	if command == "add":
		xodo = input("Enter your xodo: ")
		add_todo(xodo)

	if command == 'list':
		time.sleep(1)
		xodo_list()

	if command == "guide":
		xodo_guide()

main()