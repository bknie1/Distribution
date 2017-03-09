# Name: 		Assignment 3 : Letter Distribution
# Description : Counts letter occurrences in argument input text file.
# Author:		Brandon Knieriem

#LIB##############################################################################

import sys
import os
import curses.ascii

#DECLARATIONS####################################################################

total_letters = 0

#FX###############################################################################
# Iterates through the book, filtering white space, and tallies each ASCII val.
def Read_File(file_name) :
	with open(file_name) as file :
		for line in file : 						# Reads line.
			for letter in line : 				# Reads character value from line.
				if not letter.isspace() : 		# Filters white space.
					letter = letter.lower()		# Sanitization.
					#if ord(letter)
					Tally_Value(letter)			# Hit! Process it.
#--------------------------------------------------------------------------------#
def Sanitize_Input(value) :
	return
#--------------------------------------------------------------------------------#
# Add increment array slot via ASCII index (left adjusted).
# Ex. a = 97. array[0] = a's ascii value - 97 constant.
def Tally_Value(char) :
	if ord(char) > 160 : print(char)
	global total_letters
	total_letters += 1
#--------------------------------------------------------------------------------#
def Print_Wiki() :
	print("Wiki Letter Frequency:")
	i = 97
	while i < 123 :
		print(chr(i), "=")
		i += 1

#--------------------------------------------------------------------------------#
def Print_Result() :
	print("Total number of letters:", total_letters)
#--------------------------------------------------------------------------------#
# Error handling template.
def Throw_Fatal(error_text) :
	print("Error:", error_text)
	sys.exit(1)

#MAIN#############################################################################

# Argument Filtering
arg_num = len(sys.argv)
if arg_num != 2 : Throw_Fatal("Invalid arguments.")
file = sys.argv[1]
if os.path.isfile(file) == False or file.endswith(".txt") == False :
	Throw_Fatal("Invalid file.")

# File Processing
Read_File(file)
Print_Result()

#Print_Wiki()
#print("Total Letter Count:", total_letters)