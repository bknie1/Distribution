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
book_shelf = []
total_error = 0

#FX###############################################################################
def Read_Wiki_File() :
	global stats
	global wiki
	c = 97

	# Global Stats for Comparison
	with open(wiki_file) as file :
		for line in file :
			stats.append(line.rstrip())

	# Dictionary of Wiki Stats
	wiki['Source'] = wiki_file
	for i in stats :
		wiki[chr(c)] = i
		c += 1
#--------------------------------------------------------------------------------#
def Process_Book(file) :
	global book_shelf # Dictionary for each book dictionary by name.
	book = {} # Dictionary containing letters, occurrences.
	letters = []
	occurrences = []
	book['Source'] = file
	letters = Read_Arg_File(file)
	book = Tally_Value(letters, book)
	book_error = Calculate_Book(book)
	#book['Error'] = book_error

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
def Tally_Value(letters, book) :
	total_letters = 0
	occurrences = [0] * 26
	for i in letters :
		total_letters += 1
		try :
			occurrences[ord(i) - 97] += 1 # Left adjustment: 0/a - 25/z. Tally up.
		except :
			error = "Value:", i, "ASCII:", ord(i)
			Throw_Fatal(error)
	book['Letters'] = total_letters
	c = 97
	for i in occurrences :
		book[chr(c)] = i
		c += 1
	#book['Occurrences'] = occurrences
	return book
#--------------------------------------------------------------------------------#
def Calculate_Book(book) :
	total_letters = book.get('Letters')
	global total_error
	global wiki # A - Z
	book_error = 0
	k = 97
	i = 0
	while i < 26 :
		text_avg = round((book.get(chr(k))/total_letters * 100), 2)
		global_avg = float(wiki.get(chr(k)))
		deviation = text_avg - global_avg
		book['x' + chr(k)] = text_avg
		book['σ' + chr(k)] = round(deviation, 3)
		book_error += deviation

		# print(letter, sep='', end=' = ')
		# print("%10d" % i, sep='', end='\t')
		# print("Average - Text: %4.3f" % text_avg, sep='', end='%\t')
		# print("Global: %4.3f" % global_avg, sep='', end='%\t')
		# print("Deviation: %4.3f" % deviation, sep='', end='%\n')

		k += 1
		i += 1

	book['Book Deviation'] = round(book_error, 3)
	total_error += book_error
	Print_Book(book)
	return book_error
#--------------------------------------------------------------------------------#
def Print_Book(book) :
	global wiki
	print("Source:", book.get('Source'))
	k = 0
	while k < 26 :
		letter = chr(k + 97)
		count = book.get(letter)
		text_avg = book.get('x' + chr(k + 97))
		global_avg = float(wiki.get(chr(k + 97)))
		deviation = book.get('σ' + letter)

		print(letter, sep='', end=' = ')
		print("%10d" % count, sep='', end='\t')
		print("M-Text: %4.3f" % text_avg, sep='', end='%\t')
		print("M-Global: %4.3f" % global_avg, sep='', end='%\t')
		print("Deviation: %4.3f" % deviation, sep='', end='%\n')


		#book_p = dictionary.get(chr(k)) / dictionary.get('Total' * 100, 2)
		#official_p = wiki.get(chr(k + 97))
		#print(dictionary.get(chr(k + 97)))
		k += 1
#--------------------------------------------------------------------------------#
def Print_Total_Result() :
	global total_error
	print("-------------------------------------------------------------------------")
	print("Total Deviation in all Text: %.3f" % total_error, end='%\n')
	print("-------------------------------------------------------------------------")
#--------------------------------------------------------------------------------#
# Error handling.
def Throw_Fatal(error_text) :
	print("Error:", error_text)
	sys.exit(1)

#MAIN#############################################################################
book_shelf = {}
#try :
Read_Wiki_File()
#except :
	#Throw_Fatal("Official statistics file missing.")

# Argument Reading and *.txt File Filtering
for arg in sys.argv :
	if os.path.isfile(arg) and arg.endswith(".txt") :
		Process_Book(arg)
		#except : Throw_Fatal("Argument file.")
Print_Total_Result()
#Print_Dictionary(book_shelf)