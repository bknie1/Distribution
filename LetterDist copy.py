# Name: 		Assignment 3 : Letter Distribution
# Description : Counts letter occurrences in argument input text file.
# Author:		Brandon Knieriem
# Notes:
# 	- Russian: Insignificant deviation. The least amount of deviation.
# 	- English: Little deviation.
# 	- Spanish: Very little deviation.
# 	- French: Little deviation.
# 	- American: Very little deviation.
# 	- Irish: Very little deviation.
# 	Twain and Hugo tied for the highest deviation. (0.021%)

#LIB##############################################################################

import sys
import os
import curses.ascii

#DECLARATIONS####################################################################

wiki_file = "official.txt" # For easy file swapping.
wiki = {}
stats = []
book_shelf = {}
total_error = 0

#FX###############################################################################
def Read_Wiki_File() :
	global stats
	with open(wiki_file) as file :
		for line in file :
			stats.append(line.rstrip())
#--------------------------------------------------------------------------------#
def Process_Book(file) :
	global book_shelf # Dictionary for each book dictionary by name.
	book = {} # Dictionary containing letters, occurrences.
	letters = []
	occurrences = []
	print("\nText Name:", file, end='\n\n')
	letters = Read_Arg_File(file)

	total_letters, occurrences = Tally_Value(letters)
	book['Letters'] = total_letters
	book['Occurrences'] = occurrences
	book_error = Calculate_Book(total_letters, occurrences)
	book['Error'] = book_error

	#Print_Dictionary(book)
	#Print_Dictionary(book_shelf)

	book_shelf[file] = book # Add new entry
#--------------------------------------------------------------------------------#
# Iterates through the book, filtering white space, and tallies each ASCII val.
def Read_Arg_File(file_name) :
	letters = []
	with open(file_name) as file :
		for line in file :
			for letter in line :
				if not letter.isspace() : 	# Filters white space.
					letter = letter.lower()	# Sanitizes for ASCII alpha range.
					if ord(letter) >= 97 and ord(letter) <= 122 :
						letters.append(letter)
	return letters
#--------------------------------------------------------------------------------#
# Add increment array slot via ASCII index (left adjusted).
# Ex. a = 97. array[0] = a's ascii value - 97 constant.
def Tally_Value(letters) :
	dict_letter = {}
	total_letters = 0
	occurrences = [0] * 26
	for i in letters :
		total_letters += 1
		try :
			occurrences[ord(i) - 97] += 1 # Left adjustment: 0/a - 25/z. Tally up.
		except :
			error = "Value:", i, "ASCII:", ord(i)
			Throw_Fatal(error)
	return total_letters, occurrences
#--------------------------------------------------------------------------------#
def Calculate_Book(total_letters, occurrences) :
	global total_error
	global stats
	book_error = 0
	k = 97
	for i in occurrences :
		letter = chr(k)
		text_avg = round((i/total_letters * 100), 2)
		global_avg = float(stats[k - 97])
		deviation = text_avg - global_avg
		book_error += deviation

		print(letter, sep='', end=' = ')
		print("%10d" % i, sep='', end='\t')
		print("Average - Text: %4.3f" % text_avg, sep='', end='%\t')
		print("Global: %4.3f" % global_avg, sep='', end='%\t')
		print("Deviation: %4.3f" % deviation, sep='', end='%\n')

		k += 1
	print("Book Letter Count:", total_letters, end='\n')
	print("Book Deviation: %.3f" % book_error, end='%\n')
	print("\n-------------------------------------------------------------------------")
	total_error += book_error
	return book_error
#--------------------------------------------------------------------------------#
def Print_Dictionary(dictionary) :
	#print(dictionary.keys())
	#print(dictionary.values())
	#print(dictionary.items())
	for k, v in dictionary.items():
		print (k, ':', v)
		print("-------------------------------------------------------------------------")
#--------------------------------------------------------------------------------#
def Print_Total_Result() :
	global total_error
	print("Total Deviation: %.3f" % total_error, end='%\n')
	print("-------------------------------------------------------------------------")
#--------------------------------------------------------------------------------#
# Error handling.
def Throw_Fatal(error_text) :
	print("Error:", error_text)
	sys.exit(1)

#MAIN#############################################################################
book_shelf = {}
try :
	Read_Wiki_File()
except :
	Throw_Fatal("Official statistics file missing.")

# Argument Reading and *.txt File Filtering
for arg in sys.argv :
	if os.path.isfile(arg) and arg.endswith(".txt") :
		try : Process_Book(arg)
		except : Throw_Fatal("Argument file.")
Print_Total_Result()
Print_Dictionary(book_shelf)