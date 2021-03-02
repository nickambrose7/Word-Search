from funcs import *

def main():
   
   puzzle = get_puzzle()
   
   words = get_words()

   print('Puzzle:\n')

   for i in range(len(puzzle)):

   	print(puzzle[i])

   	if i == len(puzzle) - 1:

   		print('\n')


   for word in words:

   	if search_word(word, puzzle) == None:
   		
   		print(word + ': word not found')

   	elif search_word(word, puzzle)[0]:

   		print(word + ': (' + search_word(word, puzzle)[1] + ')' + ' row: ' + str(search_word(word, puzzle)[2]) + ' column: ' + str(search_word(word, puzzle)[3]))

         
   



if __name__ == '__main__':
   main()