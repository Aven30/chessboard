import collections
import copy
import chess
import heuristicY
from treelib import Node, Tree


heuristicValues = {}
def maxChild(node,tree):
	maxVal = -10000
	type(node.identifier)
	for a in tree.children(node.identifier):
		if heuristicValues[a.identifier] > maxVal:
			maxVal = heuristicValues[a.identifier]
	return maxVal

def miniMaxTree(board):
	tree = Tree()
	Level0List   = [board]
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
				 
				val = heuristicY.h(brd)
				heuristicValues[boardName] = val			
				tree.create_node(nodeName+'_'+str(i2),nodeName+'_'+str(i2),parent=boardName,data=brd)
				i2 = i2+1
			index = index+1
		return newGenBrd

	brdList = addPossMovesByList(Level0List,"LevelOne","currentBoard")
	brdList = addPossMovesByList(brdList,"LevelTwo","LevelOne")
	brdList = addPossMovesByList(brdList,"LevelThree","LevelTwo")


	return tree  

