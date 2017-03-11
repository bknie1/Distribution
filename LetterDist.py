# Name: 		Assignment 3 : Letter Distribution
# Description : Counts letter occurrences in argument input text file.
# Author:		Brandon Knieriem

#LIB##############################################################################

import sys
import os
import curses.ascii

#DECLARATIONS####################################################################

wiki_file = "official.txt" # For easy file swapping.
total_letters = 0
occurrences = [0] * 26
stats = []

#FX###############################################################################
def Read_Wiki_File() :
	global stats
	with open(wiki_file) as file :
		for line in file :
			stats.append(line.rstrip())
#--------------------------------------------------------------------------------#
# Iterates through the book, filtering white space, and tallies each ASCII val.
def Read_Arg_File(file_name) :
	with open(file_name) as file :
		for line in file : 						# Reads line.
			for letter in line : 				# Reads character value from line.
				Sanitize_Input(letter)
#--------------------------------------------------------------------------------#
def Sanitize_Input(ch) :
	if not ch.isspace() : 						# Filters white space.
		ch = ch.lower()							# Sanitizes for range.
		if ord(ch) >= 97 and ord(ch) <= 123 : 	# Within lower alpha range.
			Tally_Value(ch)						# Hit! Process it.
#--------------------------------------------------------------------------------#
# Add increment array slot via ASCII index (left adjusted).
# Ex. a = 97. array[0] = a's ascii value - 97 constant.
def Tally_Value(ch) :
	global total_letters
	global occurrences
	total_letters += 1
	target = ord(ch) - 97 # Left adjustment: 0/a - 25/z.
	occurrences[target] += 1
#--------------------------------------------------------------------------------#
def Print_Result() :
	global occurrences
	global stats
	print("Total number of letters:", total_letters)
	k = 97
	p = 1
	mod = 1 # Adjust for column formatting.
	for i in occurrences :
		letter = chr(k)
		text_avg = round((i/total_letters * 100), 2)
		global_avg = float(stats[k - 97])
		difference = text_avg - global_avg
		print(letter, sep='', end=' = ')
		print("%10d" % i, sep='', end='\t')
		print("Average - Text: %4.3f" % text_avg, sep='', end='%\t')
		print("Global: %4.3f" % global_avg, sep='', end='%\t')
		print("Difference: %4.3f" % difference, sep='', end='%')
		if not (p) % mod: print('\n')
		p += 1
		k += 1
#--------------------------------------------------------------------------------#
def Print_Wiki() :
	print("Wiki Letter Frequency:")
	i = 97
	while i < 123 :
		print(chr(i), "=")
		i += 1
#--------------------------------------------------------------------------------#
# Error handling.
def Throw_Fatal(error_text) :
	print("Error:", error_text)
	sys.exit(1)

#MAIN#############################################################################

# Argument Filtering
arg_num = len(sys.argv)
if arg_num != 2 : Throw_Fatal("Invalid arguments.")
file = sys.argv[1]
if not os.path.isfile(file) or not file.endswith(".txt"):
	Throw_Fatal("Invalid file.")

# File Processing
Read_Wiki_File()
Read_Arg_File(file)
Print_Result()