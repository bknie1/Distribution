# Assignment 3

In this program you will be performing an analysis of a set of books to determine how well the distribution of letters in these texts corresponds to that found by other researchers. A chart of letter frequencies in the English language can be found at https://en.wikipedia.org/wiki/Letter_frequency .

Your program should use command line arguments to input the names of several books that should be analyzed. There are ten such books that I got from Project Gutenberg given above. These are all long texts, so that the sample size for the analysis will be reasonable. For each book, you should read in the text and count how many times each letter occurs in the text. You can ignore all numbers and symbols that you find in the text, and upper and lower case letters should be considered the same for the counting process. You should then compute the occurrence percentages for each letter in each book to generate a frequency table like that mentioned above. Use a dictionary to store this information.

Once you have a letter frequency table for each book, you can generate some reports. First, print out a table showing the difference in frequency values from that observed in each book to that in the wikipedia table. Sum up the absolute value of each letter's error to get a total error, which should also be printed for each book. Rank the books by this total error amount, from that which is closest to the given table, to that which is the most different from the table. You should then determine whether the nationality of the book author has any effect on the difference in letter frequency. From the books I have provided there are American, Russian, French, Spanish, English and Irish authors.

Second, you should sort each of the tables from most frequent to least frequent. You should then compare each book's sorted listing to that of a sorted version of the wikipedia table. You should determine whether each letter is in the same position, or if not, how many positions difference there is up or down in the ranking. Print out another table containing these changes in ranking as positive and negative values. Sum up the absolute value of each letter's change in position to get a total error, which should also be printed for each book. Rank the books by this total change amount, from that which is closest to the given table, to that which is the most different from the table. 

For the final analysis, begin with the sorted versions of the letter frequencies. You will look at these orderings in four groups: positions 1-6, 7-12, 13-19 and 20-26. For each sorted list, compute the set of letters for each of these groupings for each book. Then, using set intersection, determine which letters are present within these four groups across all of the books. Print this information out. Then, using set union, analyze two groupings: 1-12 and 13-26, to see which letters are always within these two groupings across all books. Print this information out.

Submit your commented source code here, along with the produced reports for all of the books I have supplied. You can run additional reports on books of your choosing as well.
