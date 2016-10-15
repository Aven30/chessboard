import chess
totalMoves = 0
def h(board):
	return f(board)+g(board)
def g(board):
	# number of moves. Half will be other player's moves
	return len(board.move_stack)/2
def f(board):
	# Everything starts at 500(being the best move)
	value = 500
	####################################
	# IN CHECK?
	###################################
	if(board.is_check()): 
		value = value-100
		#print("in check, -100"+str(value))
	#####################################
	# R O O K  
	####################################
	# Is ROOK still there?
	rookLocation = board.pieces(chess.ROOK,False)
	# -60 if ROOK no longer there
	 
	if(len(rookLocation) == 0):
		value = value - 60
		#print("rook gone!, -60"+str(value))
	else:
		# There will only be one piece
		for s in rookLocation:
			rookLocation = s

		# ROOK ATTACKERS :(
		attackers = board.attackers(True,rookLocation)
		#print(str(len(attackers))+" number of rook attackers!")
		#print("Location: "+str(rookLocation))

		
		# One attacker
		if(len(attackers) == 1):
			value = value-10
			#print("Rook: one attacker, -10"+str(value))
		# Two attackers
		elif(len(attackers) == 2):
			value = value-20
			#print("Rook: two attacker, -20"+str(value))
		# at least Three attackers
		elif(len(attackers)>0):
			value = value-30
			#print("Rook: three attackers, -30"+str(value))
		# Now, let's deal with location. We need to stall
		# So further away from the player, the better. Also,
		# The sides are better.
		# COLUMN
		rookLocation = chess.SQUARE_NAMES[rookLocation]
		currentCol =  rookLocation[0:1]
		if (currentCol == "c"):
			value = value-2			
			#print("Rook: column c, -2"+str(value))
		elif(currentCol == "d"):
			value = value-6
			#print("Rook: column d, -6"+str(value))
		elif(currentCol == "e"):
			value = value-2
			#print("Rook: column e, -2"+str(value))
		# ROW
		row = rookLocation[1:2]
		if (row == 4):
			value = value-10
			#print("Rook: row 4, -10"+str(value))
		elif(row == 5):
			value = value-15
			#print("Rook: row 5, -15"+str(value))
		elif(row == 6):
			value = value-25
			#print("Rook: row 6, -25"+str(value))
		elif(row == 7):
			value = value-35
			#print("Rook: row 6, -35"+str(value))
		elif(row == 8):
			value = value-45
			#print("Rook: row 8, -45"+str(value))
	#####################################
	# K N I G H T
	####################################
	# Is ROOK still there?
	knightLocation = board.pieces(chess.KNIGHT,False)
	# -50 if knight no longer there
	if(len(knightLocation) == 0):
		value = value - 50
		#print("Knight gone, -50"+str(value))
	else:
		# There will only be one piece
		for a in knightLocation:
			knightLocation = a

		# KNIGHT ATTACKERS :(
		attackers = board.attackers(True,knightLocation)
		# One attacker
		if(len(attackers) == 1):
			value = value-8
			#print("Knight: one attacker, -8"+str(value))
		# Two attackers
		elif(len(attackers) == 2):
			value = value-18
			#print("Knight: two attackers, -18"+str(value))
		# at least Three attackers
		elif(len(attackers)>0):
			value = value-25
			#print("Knight: three attackers, -25"+str(value))
		# Now, let's deal with location. We need to stall
		# So further away from the player, the better. Also,
		# The sides are better.		
		knightLocation = chess.SQUARE_NAMES[knightLocation]
		# COLUMN
		currentCol =  knightLocation[0:1]
		if (currentCol == "c"):
			value = value-2
			#print("Knight: col c, -2"+str(value))
		elif(currentCol == "d"):
			value = value-6
			#print("Knight: col d, -6"+str(value))
		elif(currentCol == "e"):
			value = value-2
			#print("Knight: col e, -2"+str(value))
		# ROW
		row = knightLocation[1:2]
		if (row == 4):
			value = value-10
			#print("Knight: row 4, -10"+str(value))
		elif(row == 5):
			value = value-15
			#print("Knight: row 5, -15"+str(value))
		elif(row == 6):
			value = value-25
			#print("Knight: row 6, -25"+str(value))
		elif(row == 7):
			value = value-35
			#print("Knight: row 7, -35"+str(value))
		elif(row == 8):
			value = value-45
			#print("Knight: row 8, -45"+str(value))
	return value
	
