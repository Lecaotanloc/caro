player = ''
def minimax_search(game, state):
    player = game.to_move(state)
    value, move = max_value(game, state)
    return move

def max_value(game, state):
    if game.is_terminal(state):
        return game.utility(state, player), None
    v = float("-inf")
    for a in game.actions(state):
        v2, a2 = min_value(game, game.result(state, a))
        if v2 > v:
            v, move = v2, a
    return v, move

def min_value(game, state):
    if game.is_terminal(state):
        return game.utility(state, player), None
    v = float("inf")
    for a in game.actions(state):
        v2, a2 = max_value(game, game.result(state, a))
        if v2 < v:
            v, move = v2, a
    return v, move
