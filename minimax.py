def minimax_value(node, depth, maximizing):
    if depth <= 0 or node.is_terminal:
        return node.score
    if maximizing:
        f = max
        bestvalue = float('-inf')
    else:
        f = min
        bestvalue = float('inf')
    for child in node.children:
        val = minimax_value(child, depth - 1, not maximizing)
        bestvalue = f(bestvalue, val)
    return bestvalue
