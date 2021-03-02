# Put your functions in here.
# Feel free to run your design past me before beginning to implement.





puzzle = ["WAQHGTTWEE",
			 "CBMIVQQELS",
			 "AZXWKWIIIL",
			 "LDWLFXPIPV",
			 "PONDTMVAMN",
			 "OEDSOYQGOB",
			 "LGQCKGMMCT",
			 "YCSLOACUZM",
			 "XVDMGSXCYZ",
			 "UUIUNIXFNU"]



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

		elif i == len(user_input) - 1: #this elif statement allows us to get the last word in the user_input

			word = user_input[beginning:len(user_input)]

			words.append(word)

	return words


	

def find_first_letter(puzzle, word):
	'''
	searches the puzzle for the first letter of the specified word.
	Once first letter is found, returns row and col location so that searching can begin.
	'''

	r_c_list = [] #list of all the rows and columns that the letter is in

	for i in range(0, 10):

		for j in range(0, 10):

			if puzzle[i][j] == word[0]:

				r_c_list.append([i, j])

	return r_c_list




def check_row(puzzle, row, col, word): #Only reason I'm inculding row AND col is to make it easier if we find the word.
	'''
	Use .find to check for word in row
	Returns true and 'forward' if word is in row, else returns false
	'''

	row_list = puzzle[row]

	row_string = ''.join(row_list) #creates a string out of a list so that we can use .find

	word_slice = row_string[col:(col + len(word))] 
	'''
	this word_slice is to combat a bug I ran into. 
	If a row/col contained the first letter of the word I was looking for, 
	but it was not the word, yet the word was in the row, I would return the
	row and col of the letter, but not the first letter in the word. To avoid this,
	I am only searching the length of the word so that I know my first letter is the 
	first letter of the actual word, not just a coincidence.
	'''

	num = word_slice.find(word) #.find returns the index of the first occurance of the substring, else returns -1.

	if num == 0:

		return (True, 'FORWARD', row, col)

	else:

		return False #Shows the word in not in the row.



def check_row_backward(puzzle, row, col, word):
	'''
	Use .find to check for word in row
	Returns true and 'backward' if word is in row, else returns false
	'''

	row_list = puzzle[row]

	row_string = ''.join(row_list)

	rev_word = word[::-1]

	word_slice = row_string[(col - len(word) +1):col + 1] #adjust b/c backwards

	num = word_slice.find(rev_word)

	if num != -1: #find will return -1 if word is not found

		return (True, 'BACKWARD', row, col)

	else:

		return False #Shows the word in not in the row.



def check_col_down(puzzle, row, col, word):
	'''
	Use .find to check a col for word
	Returns true and 'down' if word is in col, else returns false
	'''

	col_list = []

	for i in range(10):

		col_list.append(puzzle[i][col]) #we want the row to change and the col to stay the same

	col_string = ''.join(col_list) #same process as usual once we make the string

	word_slice = col_string[row:(row + len(word))]

	num = word_slice.find(word)

	if num != -1:

		return (True, 'DOWN', row, col)

	else:

		return False


def check_col_up(puzzle, row, col, word):
	'''
	Use .find to check a col for word
	Returns true and 'up' if word is in col, else returns false
	'''
	col_list = []

	for i in range(10):

		col_list.append(puzzle[i][col]) #we want the row to change and the col to stay the same

	col_string = ''.join(col_list) #same process as usual once we make the string

	rev_word = word[::-1]

	word_slice = col_string[(row - len(word) + 1):row + 1]

	num = word_slice.find(rev_word)

	if num != -1:

		return (True, 'UP', row, col)

	else:

		return False 


def check_diagonal(puzzle, row, col, word):
	'''
	Add one to row and col to increment diagonally
	Be carful of indexing outside of the puzzle when adding one to row and col
	return true and diagonal if word is in diagonal, else return false
	'''

	diag_list = [] 

	for i in range(10):

		if (i + row) <= 9 and (i + col) <= 9: #make sure we stay within indexes

			diag_list.append(puzzle[row + i][col +i]) #this is how we move diagonally, rest of code is the same

	diag_string = ''.join(diag_list)

	num = diag_string.find(word)

	if num != -1:

		return (True, 'DIAGONAL', row, col)

	else:

		return False 




def search_word(word, puzzle):
	'''
	Searches the puzzle for a specified word.
	Loop through the list of words and call this function each time to find all words.
	This function returns none or direction, row, and col of the word.

	'''



	row_col_list = find_first_letter(puzzle, word) #list within list, all rows and cols of first letter in word.


	for i in range(len(row_col_list)):

		row = row_col_list[i][0]

		col = row_col_list[i][1]

	
		if check_row(puzzle, row, col, word):

			return (check_row(puzzle, row, col, word))
		
		elif check_row_backward(puzzle, row, col, word):

			return (check_row_backward(puzzle, row, col, word))
		
		elif check_col_down(puzzle, row, col, word):

			return (check_col_down(puzzle, row, col, word))
		
		elif check_col_up(puzzle, row, col, word):

			return (check_col_up(puzzle, row, col, word))

		elif check_diagonal(puzzle, row, col, word):

			return (check_diagonal(puzzle, row, col, word))

	return None

	







        
   
   
