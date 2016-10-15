import collections
import copy
import chess
from collections import OrderedDict
from treelib import Node, Tree

board = chess.Board()
board.clear_board()
board.set_piece_at(chess.E1,chess.Piece(chess.KING,True))
board.set_piece_at(chess.A1,chess.Piece(chess.ROOK,True))
board.set_piece_at(chess.G1,chess.Piece(chess.KNIGHT,True) )
board.set_piece_at(chess.E8,chess.Piece(chess.KING, False))
board.set_piece_at(chess.B8,chess.Piece(chess.KNIGHT,False))

Level0List   = [board]
tree = Tree()
tree.create_node('currentBoard','currentBoard',data=board)
index = 0

def addPossMovesByList(listOfBoards,nodeName,parentNodeName):
	index = 0
	i2    = 0
	newGenBrd = [] 
	
	for b in listOfBoards:
		for move in b.legal_moves:
			currentMove = chess.Move.from_uci(move.uci())
			brd = copy.deepcopy(b)
			brd.push(currentMove)
			newGenBrd.append(brd)
			# check if it's root of tree
			if (parentNodeName == "currentBoard"):		
				boardName = parentNodeName
			else:
				boardName = parentNodeName+'_'+str(index);
			tree.create_node(nodeName+'_'+str(i2),nodeName+'_'+str(i2),parent=boardName,data=brd)
			i2 = i2+1
		index = index+1
	return newGenBrd

brdList = addPossMovesByList(Level0List,"LevelOne","currentBoard")
#brdList = addPossMovesByList(brdList,"LevelTwo","LevelOne")
#brdList = addPossMovesByList(brdList,"LevelThree","LevelTwo")
#tree.show()
