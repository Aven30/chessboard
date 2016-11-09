import chess
totalMoves = 0
#-----------------------------------------------------------------------------------------------------------
def h(board):
	return f(board)+g(board)
#-----------------------------------------------------------------------------------------------------------
def g(board):
	return len(board.move_stack)/2 # number of moves. Half will be other player's moves
#-----------------------------------------------------------------------------------------------------------	
def f(board):
	value = 500 # initial score at 500(being the best move)
	
	# IN CHECK?
	
	if(board.is_check()): 
		value = value-100
		
	# KNIGHT  
	# Is KNIGHT still there?
	knightLocation = board.pieces(chess.KNIGHT,True)
	 
	if(len(knightLocation) == 0):
		value = value - 60  # -60 if KNIGHT no longer there
	else:
		for s in knightLocation:
			knightLocation = s

		# KNIGHT ATTACKERS
		attackers = board.attackers(False,knightLocation)
		
		# One attacker
		if(len(attackers) == 1):
			value = value-10
			
		# Two attackers
		else(len(attackers) == 2):
			value = value-20
	#-----------------------------------------------------------------------------------------------------------		
	# ROOK  -   It has a higher importance than the knight.
	# Is ROOK still there?
	rookLocation = board.pieces(chess.ROOK,True)
	 
	if(len(rookLocation) == 0):
		value = value - 80  # -80 if ROOK no longer there, 
	else:
		for s in rookLocation:
			rookLocation = s

		# ROOK ATTACKERS
		attackers = board.attackers(False,rookLocation)
		
		# One attacker
		if(len(attackers) == 1):
			value = value-20
			
		# Two attackers
		else(len(attackers) == 2):
			value = value-40
	#-----------------------------------------------------------------------------------------------------------
	
		# Location. We need to stall, protect or attack
		# So further closer to the other player, the better. And Opponents piece away from the king, the better 
		# The sides are better.
	
	#-----------------------------------------------------------------------------------------------------------
		# COLUMN
		knightLocation = chess.SQUARE_NAMES[knightLocation]
		currentCol =  knightLocation[6:8]
		if (currentCol == "a"):
			value = value-3	 #knight in the corner is a terrible idea		
			
		elif(currentCol == "b"):
			value = value+2
			
		elif(currentCol == "d"):
			value = value+4
			
		elif(currentCol == "e"):
			value = value+2
	#-----------------------------------------------------------------------------------------------------------			
		# ROW
		row = knightLocation[4:6]
		if (row == 4):
			value = value+40
			
		elif(row == 5):
			value = value+45
			
		elif(row == 6):
			value = value+35
			
		elif(row == 7):
			value = value+15
			
		elif(row == 8):
			value = value-10
		         
	#-----------------------------------------------------------------------------------------------------------
		
	
