MAX_DEEP = 1000
INFINITY = float('inf')

################################################
#              Classic AlphaBetaTree class        #
################################################


class AlphaBetaAI:

    def __init__(self, game_tree):
        self.game_tree = game_tree
        self.root = game_tree.root
        self.successors_list = []
        self.node = None
        return

    # return TRUE when the node don't have any children (game is over)
    def is_game_over(self, node):
        assert node is not None
        return len(node.children) == 0

    # return list of children
    def get_children(self, node):
        assert node is not None
        return node.children

    # return value of the node
    def get_value(self, node):
        assert node is not None
        return node.value

    # return deep of the node
    def get_deep(self, node):
        assert node is not None
        return node.deep

    # max alfa state
    def max_value(self, node, deep, alpha, beta):
        if self.is_game_over(node) or deep == 0:
            return self.get_value(node)
        max_value = alpha
        successors = self.get_children(node)
        for state in successors:
            max_value = max(max_value, self.min_value(state, deep-1, max_value, beta))
            if max_value >= beta:
                break
        return max_value

    # min beta state
    def min_value(self, node, deep, alpha, beta):
        if self.is_game_over(node) or deep == 0:
            return self.get_value(node)
        min_value = beta
        successors = self.get_children(node)
        for state in successors:
            min_value = min(min_value, self.max_value(state, deep-1, alpha, min_value))
            if alpha >= min_value:
                break
        return min_value

    # initial method
    def start(self, node):
        best_value = -INFINITY

        successors = self.get_children(node)
        best_move = None
        for elem in successors:
            value = self.min_value(elem, MAX_DEEP, best_value, INFINITY)
            if value > best_value:
                best_value = value
                best_move = elem

        return best_move
