# Connect Four game V1.0 

from games import Board
from time import sleep

def startGame():
	
	print('Welcome to connect 4!!')
	print('Enter a letter from A to G in order to make your move.')
	print('Play against another player or against the computer. Have fun!')
	input('Press enter to continue')
	print('======================')
	mainGame()

def mainGame():

	# Creating a Board object from the games.py file
	game = Board(6,7)

	COLUMMNS = 'A B C D E F G'.split()
	players = ['X','O']

	# Asking the player for a rival and checking input
	rival = input('Choose your rival. Another player [1], The computer [2]: ')
	while rival not in ['1','2']:
		rival = input('Wrong input. Choose another player [1] or the computer [2]: ')
	
	game.display()
	
	while True:

		if rival == '1':
			
			currentPlayer = players[0]
			print(f'Its player {currentPlayer} turn')

			move = input(f'Select a column where you want to place an {currentPlayer}. Choose between A, B, C, D, E, F or G: ').upper()

			move = checkMove(game,move,currentPlayer)
			placeMove(game,move,currentPlayer)

			if checkWinColumn(game,move,currentPlayer) or checkWinRow(game,move,currentPlayer) or checkWinDiagonal(game,move,currentPlayer):
				
				print(f'{currentPlayer} wins')
				playAgain()
				
			elif checkTie(game,move):
				
				print('It is a tie!!')
				playAgain()

			del players[0]
			if players == []:
				players = ['X','O']

		elif rival == '2': 
			# Code for when the rival is the computer
			return

def checkMove(game,move,currentPlayer):
	
	while True:
		try:
			while game.board[move+'6'] != '-':
				move = input(f'That column is full. Choose another one: ').upper()
			break
		except:
			move = input(f'Choose a valid number to place an {currentPlayer}: ').upper()
	return move

def placeMove(game,move,currentPlayer):
	
	chosenColumn = turnColumn(game,move)
	
	for element in chosenColumn:
		if game.board[element] == '-':
			game.board[element] = currentPlayer
			break

	game.display()

def checkWinColumn(game,move,currentPlayer):

	chosenColumn = turnColumn(game,move)
	counter = 0

	for cord in chosenColumn:
		if game.board[cord] == currentPlayer:
			counter += 1
			if counter == 4:
				return True
		else:
			counter = 0

def checkWinRow(game,move,currentPlayer):

	chosenRow = turnRow(game,move)
	counter = 0

	for cord in chosenRow:
		if game.board[cord] == currentPlayer:
			counter += 1
			if counter == 4:
				return True
		else:
			counter = 0

def checkWinDiagonal(game,move,currentPlayer):

	chosenDiagonals = turnDiagonal(game,move)
	counter = 0

	for diagonal in chosenDiagonals:
		for cord in diagonal:
			if game.board[cord] == currentPlayer:
				counter += 1
				if counter == 4:
					return True
			else:
				counter = 0
		counter = 0


def checkTie(game,move):
	
	for cord in game.board:
		if game.board[cord] == '-':
			return False

	return True

def turnColumn(game,move):

	# Returns a list of the keys corresponding to the column chosen in the current turn

	chosenColumn = []
	for cord in game.board:
		if cord[0] == move:
			chosenColumn.append(cord)
	return chosenColumn

def turnRow(game,move):

	# Returns a list of the keys corresponding to the row chosen in the current turn

	chosenColumn = turnColumn(game,move)
	counter = 0
	chosenRow = []

	for cord in chosenColumn:
		if game.board[cord] == '-':
			rowNumber = counter
			break
		else:
			rowNumber = 6
		counter += 1
	
	for cord in game.board:
		if cord[1] == str(rowNumber):
			chosenRow.append(cord)

	return chosenRow

def turnDiagonal(game,move):

	chosenDiagonals = []

	upDiagonals = [['A3','B4','C5','D6'],['A2','B3','C4','D5','E6'],['A1','B2','C3','D4','E5','F6'],['B1','C2','D3','E4','F5','G6'],['C1','D2','E3','F4','G5'],['D1','E2','F3','G4']]
	downDiagonals = [['A4','B3','C2','D1'],['A5','B4','C3','D2','E1'],['A6','B5','C4','D3','E2','F1'],['B6','C5','D4','E3','F2','G1'],['C6','D5','E4','F3','G2'],['D6','E5','F4','G3']]
	
	allDiagonals = []
	allDiagonals.extend(downDiagonals)
	allDiagonals.extend(upDiagonals)
	
	chosenColumn = turnColumn(game,move)
	chosenRow = turnRow(game,move)

	for colElem in chosenColumn:
		for colRow in chosenRow:
			if colRow == colElem:
				chosenCell = colRow
				break

	for diagonal in allDiagonals:
		for cord in diagonal:
			if cord == chosenCell:
				chosenDiagonals.append(diagonal)

	return chosenDiagonals

def playAgain():

	ans = input('Do you want to play again? YES [1], NO [2]: ')
	while ans not in ['1','2']:
		ans = input('Select [1] to play again or [2] to exit: ')
	
	if ans == '1':
		mainGame()
	else:
		exit()

if __name__ == '__main__':
	startGame()