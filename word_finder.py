from funcs import *

def main():
   
   puzzle = get_puzzle()
   
   words = get_words()

   print('Puzzle:\n', puzzle)

   for word in words:

   	if search_word() == None:
   		print 


   pass
   



if __name__ == '__main__':
   main()