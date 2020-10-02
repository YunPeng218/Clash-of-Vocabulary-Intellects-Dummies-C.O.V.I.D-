### psphelper.py ###

import os

## Helpful Functions

# Read a list of quotes from a file
# 	filename - the name of the file from which quotes are read. 
def readQuotesFromFile(filename):
	quotes = list()
	f = open(filename, "r")
	for line in f:
		quotes.append(line.strip().upper())
	f.close()
	return quotes


# Convert an alphabet to underscore. Non-alphabets are ignored.
# 	letter - the letter to convert
# 
# * this function assumes letter to be a single character.
def alphaToUnderscore(letter):
	if (letter.isalpha()):
		return '_'
	else:
		return letter

# Clear the command prompt screen
def clearScreen():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

# Show the quote screen
# 	quote - the quote string to be displayed on the quote screen
#	screenwidth - the width of quote screen (excluding borders).
def showQuoteScreen(quote, screenwidth):
 
	### Definition of screen width and inner width
	#
	# |             screen width             |
	# | |           inner width            | |
	# v v                                  v v
	# +--------------------------------------+
	# | H e y ,  I  a m  i r o n m a n .     |
	# | I  a m  n o t  g r o o t .           |
	# +--------------------------------------+

	# Insert space to separate the letters in each word in the quote
	q = quote.split()
	q1 = [" ".join(word) for word in q]

	# Auto reset screen width if it is too small to contain the quote
	max_word_length = None
	for w in q1:
		w_length = len(w)
		if max_word_length is None or max_word_length < w_length:
			max_word_length = w_length
	
	max_word_length += 4
	if max_word_length > screenwidth:
		screenwidth = max_word_length

	# See definition above
	innerwidth = screenwidth - 4

	# Constants
	SPACE = "   "
	SPACE_LENGTH = len(SPACE)
	DASH_LINE = "".ljust(screenwidth - 2, '-')

	# Insert SPACE to the letter-spaced quotes
	quoteSpaced = SPACE.join(q1)

	# Top border
	print("+{0}+".format(DASH_LINE))

	start = 0
	while True:
		remaining = len(quoteSpaced) - start
		
		# Haven't cover last letter (i.e. not last line)
		if innerwidth < remaining:
			
			# Find the last occurrence of SPACE within the subquote in [start:start+innerwidth+SPACE_LENGTH]
			# End should point to the letter after the last SPACE.
			limit = start + innerwidth + SPACE_LENGTH
			end = quoteSpaced.rfind(SPACE, start, limit)

			# Print
			print("| {0:<{1}} |".format(quoteSpaced[start:end], innerwidth))
			
			# Update start
			start = end + SPACE_LENGTH
		# Last line
		else:
			print("| {0:<{1}} |".format(quoteSpaced[start:], innerwidth))
			break

	# Bottom border
	print("+{0}+".format(DASH_LINE))
	
#  Test
if __name__ == "__main__":

	quote = str(input("Enter quote: "))
	screenwidth = int(input("Enter screenwidth: "))

	showQuoteScreen(quote, screenwidth)