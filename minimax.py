import treelib
def minimax_value(node, depth, maximizing):
    if depth <= 0 or node.is_terminal:
        return node.score
    if maximizing:
        f = max
        bestvalue = float('-inf')
		for each child of node
            val := minimax(child, depth − 1, False)
            bestValue = f(bestvalue, val)
        return bestValue
    else:
        f = min
        bestvalue = float('inf')
    for child in node.children:
        val = minimax_value(child, depth - 1, True)
        bestValue = f(bestvalue, val)
    return bestvalue

