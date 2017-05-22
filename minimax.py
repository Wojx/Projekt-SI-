MAX_DEEP = 1000
INFINITY = float('inf')

################################################
#              Classic MinMaxTree class        #
################################################


class MinMaxAI:

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

    # max state
    def max_value(self, node, deep):
        if self.is_game_over(node) or deep == 0:
            return self.get_value(node)

        maximum_value = -INFINITY
        successors = self.get_children(node)
        for state in successors:
            maximum_value = max(maximum_value, self.min_value(state, deep-1))
        return maximum_value

    # min state
    def min_value(self, node, deep):
        if self.is_game_over(node) or deep == 0:
            return self.get_value(node)

        minimum_value = INFINITY
        successors = self.get_children(node)
        for state in successors:
            minimum_value = max(minimum_value, self.max_value(state, deep-1))
        return minimum_value

    # initial method
    def start(self, node):
        best_value = self.max_value(self, node, MAX_DEEP)
        successors = self.get_children(node)
        best_move = None
        for elem in successors:
            if elem.value == best_value:
                best_move = elem
                break

        return best_move


