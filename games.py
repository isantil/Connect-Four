import string

class Board:
	
	def __init__(self,rows,columns):

		self.rows = rows
		self.columns = columns	
		self.board = {}
		self.initial_values = []

		for i in range(self.rows):
			for j in range(self.columns):
				self.initial_values.append('-')
	
		self.columns_letters = string.ascii_uppercase[:self.columns]
		coordinates_list = []

		for let in self.columns_letters:
			for row in range(1,self.rows+1):
				coordinates_list.append(let+str(row))

		self.board = dict(zip(coordinates_list,self.initial_values))

	def display(self):
		
		''' The objective is to display in the following format:

	       A3 | B3 | C3 
		 ---------------
		   A2 | B2 | C2     Example for a 3x3 board
 		 ---------------
		   A1 | B1 | C1
		
		'''

		for let in self.columns_letters:
			print(' '+let+' ',end='')
		print('')

		num = self.rows

		for j in range(self.rows)[::-1]:
			for i in range(j,self.rows*self.columns,self.rows):
				print(' '+list(self.board.values())[i]+' ',end='')
			print(' '+str(num))
			num -= 1

	def reset(self):

		for val in self.board:
			self.board[val] = '-'

if __name__ == '__main__':
	test = Board(1,8)
	test.display()
	print(test.board)