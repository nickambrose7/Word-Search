# Put your functions in here.
# Feel free to run your design past me before beginning to implement.

def get_puzzle():
	'''
	gets input from user and converts into a list within a list representing the puzzle
	'''
	pass

def get_words():
	'''
	Gets input from user and converts into a list of words
	'''
	pass

def search_word(word, puzzle):
	'''
	Searches the puzzle for a specified word.
	Loop through the list of words and call this function each time to find all words.
	This function returns none or direction, row, and col of the word.

	'''
	pass

def find_first_letter(puzzle, word):
	'''
	searches the puzzle for the first letter of the specified word.
	Once first letter is found, returns row and col location so that searching can begin.
	'''
	pass

def check_row(row, word):
	'''
	Use .find to check for word in row
	Returns true and 'forward' if word is in row, else returns false
	'''
	pass

def check_row_backward(row, word):
	'''
	Use .find to check for word in row
	Returns true and 'backward' if word is in row, else returns false
	'''
	pass


def check_col_down(col, word):
	'''
	Use .find to check a col for word
	Returns true and 'down' if word is in col, else returns false
	'''
	pass


def check_col_up(col, word):
	'''
	Use .find to check a col for word
	Returns true and 'up' if word is in col, else returns false
	'''
	pass


def check_diagonal(row, col, word):
	'''
	Add one to row and col to increment diagonally
	Be carful of indexing outside of the puzzle when adding one to row and col
	return true and diagonal if word is in diagonal, else return false
	'''
	pass







        
   
   
