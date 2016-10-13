import collections
import copy
from collections import OrderedDict
from treelib import Node, Tree

pieces = {'n':28,'k':58,'R':11, 'K': 51,'N':71}
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7
# h = 8
board = collections.OrderedDict()

board = OrderedDict((('18', 0), ('28','n'),('38',0),('48',0),('58','k'),('68',0),('78',0),('88',0),
	('17', 0), ('27', 0),('37',0),('47',0),('57',0),('67',0),('77',0),('87',0),
	('16', 0), ('26', 0),('36',0),('46',0),('56',0),('66',0),('76',0),('86',0),
	('15', 0), ('25', 0),('35',0),('45',0),('55',0),('65',0),('75',0),('85',0),
	('14', 0), ('24', 0),('34',0),('44',0),('54',0),('64',0),('74',0),('84',0),
	('13', 0), ('23', 0),('33',0),('43',0),('53',0),('63',0),('73',0),('83',0),
	('12', 0), ('22', 0),('32',0),('42',0),('52',0),('62',0),('72',0),('82',0),
	('11', 'R'), ('21', 0),('31',0),('41',0),('51','K'),('61',0),('71','N'),('81',0)))
def GetColRow(brd,piece):
	for key,val in brd.items():
		if val == piece:
			return key
	return -1
def movePiece(pieceType,currentBoard,piece,move):
	# GET CURRENT POSITION OF PIECE
	results = GetColRow(currentBoard,piece)
	currentPos = list(str(results))
	if (currentPos == -1):
		return -1
	col = int(currentPos[0])
	row = int(currentPos[1])
	
	## MOVING FOR 'n' or 'N' (KNIGHT)	
	#################
	# K N I G H T
	#################
	if (pieceType == "knight"):
		### 8 Possible Moves ### 
		# Move One: Up Left
		if (move == "m1"):
			newRow = row+2
			newCol = col-1
		# Move Two: Up Right
		elif(move == "m2"):
			newRow = row+2
			newCol = col+1
		# Move Three: Down Left
		elif(move == "m3"):
			newRow = row-2
			newCol = col-1
		# Move Four: Down Right
		elif(move == "m4"):
			newRow = row-2
			newCol = col+1
		# Move Five: Right Right
		elif(move == "m5"):
			newRow = row-1
			newCol = col+2
		# Move Six: Right Left
		elif(move == "m6"):
			newRow = row+1
			newCol = col+2
		# Move Seven: Left Left
		elif(move == "m7"):
			newRow = row-1
			newCol = col-2
		# Move Seven: Left Right
		elif(move == "m8"):
			newRow = row+1
			newCol = col-2
		else:
			return -1
	## MOVING FOR 'R' (ROOK) 
	#################
	# R O O K
	#################
	elif(pieceType == "rook"):
		if(move == "m1"):
			newRow = row
			newCol = col+1
		elif(move == "m2"):
			newRow = row
			newCol = col+2
		elif(move == "m3"):
			newRow = row
			newCol = col+3		
		elif(move == "m4"):
			newRow = row
			newCol = col+4		
		elif(move == "m5"):
			newRow = row
			newCol = col-1		
		elif(move == "m6"):
			newRow = row
			newCol = col-1		
		elif(move == "m7"):
			newRow = row
			newCol = col-2		
		elif(move == "m8"):
			newRow = row
			newCol = col-3		
		elif(move == "m9"):
			newRow = row
			newCol = col-4		
		elif(move == "m10"):
			newRow = row+1
			newCol = col		
		elif(move == "m11"):
			newRow = row+2
			newCol = col		
		elif(move == "m12"):
			newRow = row+3
			newCol = col		
		elif(move == "m13"):
			newRow = row+4
			newCol = col		
		elif(move == "m14"):
			newRow = row-1
			newCol = col		
		elif(move == "m15"):
			newRow = row-2
			newCol = col		
		elif(move == "m16"):
			newRow = row-3
			newCol = col		
		elif(move == "m17"):
			newRow = row-4
			newCol = col

	## MOVING FOR 'k' or 'K' (KING) 
	#################
	# K I N G
	#################
	elif(pieceType == "king"):
		# Left
		if(move == "m1"):
			newRow = row
			newCol = col-1
		# Right
		elif(move == "m2"):
			newRow = row
			newCol = col+1
		# Up
		elif(move == "m3"):
			newRow = row+1
			newCol = col
		# Down		
		elif(move == "m4"):
			newRow = row-1
			newCol = col	
		# Right Up Diagonal	
		elif(move == "m5"):
			newRow = row+1
			newCol = col+1
		# Right Down Diagonal		
		elif(move == "m6"):
			newRow = row-1
			newCol = col+1		
		# Left Down Diagonal
		elif(move == "m7"):
			newRow = row-1
			newCol = col-1
		# Left Up Diagonal		
		elif(move == "m8"):
			newRow = row+1
			newCol = col-1	
		else:
			return -1
	 
	if (newCol > 8 or newRow > 8 or newCol < 0 or newRow <0):
		return -1
	else:
		newVal = int(str(newCol)+str(newRow)) 
	if (isEmpty(newVal) and (newCol<=8 and newRow <=8) and (newCol > 0 and newRow >0)):
		#new board
		tmpBoard1 = copy.deepcopy(currentBoard)
		tmpBoard1[str(col)+str(row)]  = 0 
		tmpBoard1[str(newVal)] = piece
		return tmpBoard1	
	else:
		return -1

def printBoard(brd):
	index = 1
	for key,val in brd.items():
		if (val == 0):
			val = '.'
		if (index % 8 == 0):
			print(val)
		else:
			print(val, end="")
		index = index+1
def isEmpty(num):
	for p in pieces:
		if(pieces[p] == num):
			return False
	return True
def possibleMoves(brd,piece):
	
	totalBoards = []
	pieceType = ""
	if (piece == 'n' or piece == 'N'):
		pieceType = "knight"
	elif(piece == 'R'):
		pieceType = "rook"
	elif(piece == 'k' or piece == 'K'):
		pieceType = "king"
	b1 = movePiece(pieceType,brd,piece,"m1")
	b2 = movePiece(pieceType,brd,piece,"m2")
	b3 = movePiece(pieceType,brd,piece,"m3")
	b4 = movePiece(pieceType,brd,piece,"m4")
	b5 = movePiece(pieceType,brd,piece,"m5")
	b6 = movePiece(pieceType,brd,piece,"m6")
	b7 = movePiece(pieceType,brd,piece,"m7")
	b8 = movePiece(pieceType,brd,piece,"m8")
	b9 = movePiece(pieceType,brd,piece,"m9")
	b10 = movePiece(pieceType,brd,piece,"m10")
	b11 = movePiece(pieceType,brd,piece,"m11")
	b12 = movePiece(pieceType,brd,piece,"m12")
	b13 = movePiece(pieceType,brd,piece,"m13")
	b14 = movePiece(pieceType,brd,piece,"m14")
	b15 = movePiece(pieceType,brd,piece,"m15")
	b16 = movePiece(pieceType,brd,piece,"m16")
	b17 = movePiece(pieceType,brd,piece,"m17")
	if (b1 is not -1):
		totalBoards.append(b1)
	if (b2 is not -1):
		totalBoards.append(b2)
	if (b3 is not -1):	
		totalBoards.append(b3)
	if (b4 is not -1):
		totalBoards.append(b4)
	if (b5 is not -1):
		totalBoards.append(b5)
	if (b6 is not -1):
		totalBoards.append(b6)
	if (b7 is not -1):
		totalBoards.append(b7)
	if (b8 is not -1):
		totalBoards.append(b8)
	if (b9 is not -1):
		totalBoards.append(b9)
	if (b10 is not -1):
		totalBoards.append(b10)
	if (b11 is not -1):
		totalBoards.append(b11)
	if (b12 is not -1):
		totalBoards.append(b12)
	if (b13 is not -1):
		totalBoards.append(b13)
	if (b14 is not -1):
		totalBoards.append(b14)
	if (b15 is not -1):
		totalBoards.append(b15)
	if (b16 is not -1):
		totalBoards.append(b16)
	if (b17 is not -1):
		totalBoards.append(b17)
	return totalBoards

tree = Tree() 
tree.create_node('originalBoard','root',data=board)

#CREATE LEVEL ONE N 
N = possibleMoves(board,'N')
index = 0
for x in N:
	tree.create_node('N'+str(index),'N'+str(index),parent='root',data=x)
	index = index+1
# CREATE LEVEL ONE R
R = possibleMoves(board,'R')
index = 0
for x in R:
	tree.create_node('R'+str(index),'R'+str(index),parent='root',data=x)
	index = index+1
# CREATE LEVEL ONE K
K = possibleMoves(board,'K')
index = 0
for x in K:
	tree.create_node('K'+str(index),'K'+str(index),parent='root',data=x)
	if (index == 0):
		printBoard(x)
	index = index+1


# CREATE LEVEL TWO for n
index = 0
for node in tree.children('root'):
	j = 0
	brd = copy.deepcopy(node.data)
	n = possibleMoves(brd,'n')
	for  d in n:
		tree.create_node('n'+str(j)+str(index),'n'+str(j)+str(index),parent=node.identifier,data=n)
		j = j +1		
	index = index+1
# CREATE LEVEL TWO for k
index = 0
for node in tree.children('root'):
	j = 0	
	brd = copy.deepcopy(node.data)
	k = possibleMoves(brd,'k')
	for  d in k :
		tree.create_node('k'+str(j)+str(index),'k'+str(j)+str(index),parent=node.identifier,data=k)
		j = j+1
	index = index+1

'''
# CREATE LEVEL THREE for N
index = 0
j = 0
i = 0
h = 0
for g in tree.children('root'):
	for node in tree.children(g.identifier):
		brd = copy.deepcopy(node.data)
		for b in brd: 
			N = possibleMoves(b,'N')
			for a in N:
				tree.create_node('N'+str(j)+str(i)+str(index)+str(h),'N'+str(j)+str(i)+str(index)+str(h),parent=node.identifier,data=a)
				print('N'+str(j)+str(i)+str(index)+str(h))
				h = h+1
			i+1
		j = j+1
	index= index+1	

# CREATE LEVEL THREE for K
index = 0
for g in tree.children('root'):
	for node in tree.children(g.identifier):
		j=0
		brd = copy.deepcopy(node.data)
		for b in brd:
			i = 0		
			K = possibleMoves(b,'K')
			for a in N:
				tree.create_node('K'+str(j)+str(i)+str(index),'K'+str(j)+str(i)+str(index),parent=node.identifier,data=a)
				i = i+1
			j+1
	index= index+1	

# CREATE LEVEL THREE for R
index = 0
for g in tree.children('root'):
	for node in tree.children(g.identifier):
		j=0
		brd = copy.deepcopy(node.data)
		for b in brd:
			i = 0		
			K = possibleMoves(b,'R')
			for a in N:
				tree.create_node('R'+str(j)+str(i)+str(index),'R'+str(j)+str(i)+str(index),parent=node.identifier,data=a)
				i = i+1
			j+1
	index= index+1	
node = tree.get_node('N_L383')
'''
a = tree.get_node('k010')
for s in a.data:
	printBoard(s)
