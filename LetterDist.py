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

#DECLARATIONS####################################################################

wiki_percent = "percent.txt" # For easy file swapping.
wiki_frequency = "frequency.txt" # Same.
wiki = {}
book_shelf = []
total_error = 0

#FX###############################################################################
def Read_Wiki_Files() :
	percents = []
	frequency = []
	global wiki
	c = 97

	# Global Stats for Comparison
	with open(wiki_percent) as file :
		for line in file :
			percents.append(line.rstrip())

	with open(wiki_frequency) as file :
		for line in file :
			frequency.append(line.rstrip())

	# Dictionary of Wiki Stats
	wiki['Source'] = wiki_percent
	for i in percents :
		wiki[chr(c)] = i
		c += 1

	wiki['Frequency'] = frequency
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

	#Print_Book(book)
	book_shelf.append(book) # Add new entry
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

	return book
#--------------------------------------------------------------------------------#
# Calculates averages, deviation, and the margin of error.
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

		k += 1
		i += 1

	book['Book Deviation'] = round(book_error, 3)
	total_error += book_error
	Sort_Book(book)
	return book_error
#--------------------------------------------------------------------------------#
# Sorts the occurrences of each letter by frequency.
def Sort_Book(book) :
	sorted_book = {} # Temporary, small dictionary for sorting.
	sorted_letters = []

	i = 0
	while i < 26 :
		char = chr(i + 97)
		count = book.get(chr(i + 97))
		sorted_book[char] = count
		i += 1

	letters = [(value, key) for key, value in sorted_book.items()]
	letters.sort()
	letters.reverse()
	letters = [(key, value) for value, key in letters]
	for i in letters :
		sorted_letters.append(i[0])

	book['Frequency'] = sorted_letters
#--------------------------------------------------------------------------------#
# def Compare_Frequencies() :
# 	global book_shelf
# 	frequencies = {}
# 	one_six = set
# 	seven_twelve = set
# 	thirt_ninet = set
# 	twen_twensix = set

# 	for book in book_shelf :
# 		frequency = book.get('Frequency')
# 		one_six += frequency[0:6]
# 		#seven_twelve.union(frequency[6:11])
# 		#thirt_ninet.union(frequency[12:18])
# 		#twen_twensix.union(frequency[19:25])
#--------------------------------------------------------------------------------#
# Strictly for printing the sorted frequency list.
def Print_Sorted(sorted_letters) :
	print("\nSorted by Frequency:\n")
	for i in sorted_letters :
		print(i)
	print("\n")
#--------------------------------------------------------------------------------#
# Prints the dictionary for a given book. Name, Letter count, Occurrences, Deviation.
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
		frequency_list = book.get('Frequency')

		print(letter, sep='', end=' = ')
		print("%10d" % count, sep='', end='\t')
		print("M-Text: %4.3f" % text_avg, sep='', end='%\t')
		print("M-Global: %4.3f" % global_avg, sep='', end='%\t')
		print("Deviation: %4.3f" % deviation, sep='', end='%\n')
		k += 1

	print("\nBook Letter Frequency (Descending)")
	k = 1
	for i in book.get('Frequency') :
		print(k, "\t", i)
		k += 1
	k = 1
	print("\nOfficial Letter Frequency (Descending)")
	for i in wiki.get('Frequency') :
		print(k, "\t", i)
		k += 1
#--------------------------------------------------------------------------------#
def Print_Shelf() :
	global book_shelf
	for book in book_shelf :
		Print_Book(book)
#--------------------------------------------------------------------------------#
# Calculates the total amount of error based on book arguments.
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
try : Read_Wiki_Files()
except : Throw_Fatal("Official statistics file missing.")

# Argument Reading and *.txt File Filtering
for arg in sys.argv :
	if os.path.isfile(arg) and arg.endswith(".txt") :
		Process_Book(arg)
		#except : Throw_Fatal("Argument file.")
Print_Shelf()
#Compare_Frequencies()
Print_Total_Result()