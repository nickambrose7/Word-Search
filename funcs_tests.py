import unittest
from funcs import *

# here is a sample puzzle for you to use in your tests
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
		  
class TestCases(unittest.TestCase):
			 
	# add your tests here

	def test_find_first_letter0(self):

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

		self.assertEqual(find_first_letter(puzzle, 'CONE'), [[1, 0], [6, 3], [6, 8], [7, 1], [7, 6], [8, 7]])

	def test_find_first_letter1(self):

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

		self.assertEqual(find_first_letter(puzzle, 'ZOY'), [[2, 1], [7, 8], [8, 9]])

	def test_check_row0(self):

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

		self.assertEqual(check_row(puzzle, 9, 3, 'UNIX'), (True, 'FORWARD', 9, 3))

	def test_check_row1(self):

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

		self.assertEqual(check_row(puzzle, 2, 5, 'WIIIL'), (True, 'FORWARD', 2, 5))

	def test_check_row2(self):

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

		self.assertFalse(check_row(puzzle, 2, 5, 'WIIILS'), False)


	def test_check_row_backward0(self):

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

		self.assertEqual(check_row_backward(puzzle, 2, 9, 'LIIIW'), (True, 'BACKWARD', 2, 9))

	def test_check_row_backward1(self):

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

		self.assertEqual(check_row_backward(puzzle, 3, 9, 'VPIP'), (True, 'BACKWARD', 3, 9))

	def test_check_row_backward2(self):

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

		self.assertFalse(check_row_backward(puzzle, 2, 9, 'TCMZ'), False)

	def test_check_col_down0(self):

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

		self.assertEqual(check_col_down(puzzle, 1, 0, 'CALPOLY'), (True, 'DOWN', 1, 0))

	def test_check_col_down1(self):

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

		self.assertEqual(check_col_down(puzzle, 1, 9, 'SLV'), (True, 'DOWN', 1, 9))

	def test_check_col_down2(self):

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

		self.assertFalse(check_col_down(puzzle, 1, 9, 'SIV'), False)


	def test_check_col_up0(self):

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

		self.assertEqual(check_col_up(puzzle, 7, 0, 'YLOPLAC'), (True, 'UP', 7, 0))

	def test_check_col_up1(self):

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

		self.assertEqual(check_col_up(puzzle, 9, 9, 'UZMT'), (True, 'UP', 9, 9))

	def test_check_col_up2(self):

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

		self.assertFalse(check_col_up(puzzle, 9, 9, 'UZMK'), False)

	def test_check_col_up3(self):

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

		self.assertFalse(check_col_up(puzzle, 7, 0, 'YLOPLACH'), False)


	def test_check_diagonal0(self):

		puzzle = ["WAQHGTTWEE",
				 "CBMIVQQELS",
				 "APXWKWIIIL",
				 "LDEFXPIPV",
				 "PONDTMVAMN",
				 "OEDSOYQGOB",
				 "LGQCKGMMCT",
				 "YCSLOACUZM",
				 "XVDMGSXCYZ",
				 "UUIUNIXFNU"]

		self.assertEqual(check_diagonal(puzzle, 1, 0, 'CPE'), (True, 'DIAGONAL', 1, 0))

	def test_check_diagonal1(self):

		puzzle = ["WAQHGTTWEE",
				 "CBMIVQQELS",
				 "APXWKWIIIL",
				 "LDEFXPIPV",
				 "PONDTMVAMN",
				 "OEDSOYQGOB",
				 "LGQCKGMMCT",
				 "YCSLOACUZM",
				 "XVDMGSXCYZ",
				 "UUIUNIXFNU"]

		self.assertEqual(check_diagonal(puzzle, 4, 4, 'TYMU'), (True, 'DIAGONAL', 4, 4))

	def test_check_diagonal2(self):

		puzzle = ["WAQHGTTWEE",
				 "CBMIVQQELS",
				 "APXWKWIIIL",
				 "LDWFXPIPV",
				 "PONDTMVAMN",
				 "OEDSOYQGOB",
				 "LGQCKGMMCT",
				 "YCSLOACUZM",
				 "XVDMGSXCYZ",
				 "UUIUNIXFNU"]

		self.assertFalse(check_diagonal(puzzle, 1, 0, 'CPE'), False)



	def test_search_word(self):

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

		self.assertEqual(search_word('UNIX', puzzle), (True, 'FORWARD', 9, 3))

	def test_search_word1(self):

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

		self.assertEqual(search_word('XINU', puzzle), (True, 'BACKWARD', 9, 6))

	def test_search_word2(self):

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

		self.assertEqual(search_word('CALPOLY', puzzle), (True, 'DOWN', 1, 0))


	def test_search_word3(self):

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

		self.assertEqual(search_word('YLOPLAC', puzzle), (True, 'UP', 7, 0))

	def test_search_word4(self):

		puzzle = ["WAQHGTTWEE",
			 "CBMIVQQELS",
			 "APXWKWIIIL",
			 "LDELFXPIPV",
			 "PONDTMVAMN",
			 "OEDSOYQGOB",
			 "LGQCKGMMCT",
			 "YCSLOACUZM",
			 "XVDMGSXCYZ",
			 "UUIUNIXFNU"]

		self.assertEqual(search_word('CPE', puzzle), (True, 'DIAGONAL', 1, 0))

	def test_search_word5(self):

		puzzle = ["WAQHGTTWEE",
			 "CBMIVQQELS",
			 "APXWKWIIIL",
			 "LDELFXPIPV",
			 "PONDTMVAMN",
			 "OEDSOYQGOB",
			 "LGQCKGMMCT",
			 "YCSLOACUZM",
			 "XVDMGSXCYZ",
			 "UUIUNIXFNU"]

		self.assertEqual(search_word('DHFLSBJSDF', puzzle), None)



# Run the unit tests.
if __name__ == '__main__':
	unittest.main()

