# Put your functions in here.
# Feel free to run your design past me before beginning to implement.

def get_puzzle():
	'''
	gets input from user and converts into a list within a list representing the puzzle
	'''
	user_input = input() #We do not need to prompt user for input

	puzzle = [] 

	for i in range(0, len(user_input), 10): #range 0 to 100, counting by ten ex.) [0, 9, 19,.....,99]
		
		if i == 9: #so that we start from 0

			partial_string = user_input[:i + 1] #take a slice of the user input starting at first letter (0, inclusive) going to tenth letter (10, exclusive)

			puzzle.append(partial_string) #appends the new partial string to the puzzle at spot 0

		else:

			new_list = user_input[i:i + 10] #now we can start at i and go to i +10

			puzzle.append(new_list)

	return puzzle
			


def get_words(): 
	'''
	Gets input from user and converts into a list of words
	'''

	user_input = input()

	words = []

	beginning = 0 #need this for first round in loop 

	for i in range(len(user_input)):

		if user_input[i] == ' ': #this code shows why order is so important

			end = i #Set end equal to the index of the space

			word = user_input[beginning:end] 

			words.append(word)

			beginning =  i + 1 #set our beginning equal to our previous end to set us up for the next time this loop runs. Must add one so that we start at the first letter not the space.

	return words



def find_word(word, puzzle):
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

	for i in puzzle:

		for j in puzzle:

			if puzzle[i][j] == word[0]:

				row = i

				col = j

				return (row, col)


def check_row(puzzle, row, word):
	'''
	Use .find to check for word in row
	Returns true and 'forward' if word is in row, else returns false
	'''
	pass

def check_row_backward(puzzle, row, word):
	'''
	Use .find to check for word in row
	Returns true and 'backward' if word is in row, else returns false
	'''
	pass


def check_col_down(puzzle, col, word):
	'''
	Use .find to check a col for word
	Returns true and 'down' if word is in col, else returns false
	'''
	pass


def check_col_up(puzzle, col, word):
	'''
	Use .find to check a col for word
	Returns true and 'up' if word is in col, else returns false
	'''
	pass


def check_diagonal(puzzle, row, col, word):
	'''
	Add one to row and col to increment diagonally
	Be carful of indexing outside of the puzzle when adding one to row and col
	return true and diagonal if word is in diagonal, else return false
	'''
	pass







        
   
   
