# Main Author:
# Main Reviewer:

# This function duplicates and returns the board. You may find this useful

from a1_partd import get_overflow_list, overflow
from a1_partc import Queue
from a3_parta import evaluate_board


def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4, change=(-1, -1)):
            self.board = board
            self.depth = depth
            self.player = player
            # self.tree_height = tree_height
            self.change = change
            self.score = 0
            self.children = []

    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.root = GameTree.Node(board, 0, player, tree_height)
        self.create_moves(tree_height, player, self.root)

    def create_moves(self, player, tree_height, cur_node):
        # if reach tree_height, evaluate the board and return, don't create children
        if cur_node.depth == tree_height - 1:
            cur_node.score = evaluate_board(cur_node.board, cur_node.player)
            return

        num_row = len(cur_node.board)
        num_col = len(cur_node.board[0])

        # check if the current move is a winning board, if yes, skip creating children
        winning_score = 6 * num_row * num_col

        if evaluate_board(cur_node.board, cur_node.player) == winning_score:
            cur_node.score = cur_node.player * winning_score
            # print('depth:', cur_node.depth, 'player: ', cur_node.player,
            #       'winning: ', cur_node.change, '| score: ', cur_node.score)
            return

        # loop through the board, change the board and create child for each change
        for i in range(num_row):
            for j in range(num_col):

                child_board = copy_board(cur_node.board)
                # change the board
                child_board[i][j] = (
                    abs(child_board[i][j]) + 1) * player

                # update the newboard using routine overflow from part a1
                a_queue = Queue()
                if overflow(child_board, a_queue) > 0:
                    while a_queue:
                        child_board = a_queue.dequeue()
                
                # create new node based on the child_board
                child_move = GameTree.Node(
                    child_board, cur_node.depth + 1, player, tree_height, (i, j))
                self.create_moves(player * -1, tree_height, child_move)

                # add child_move (child) to self.children array)
                cur_node.children.append(child_move)

                # pick the score base on minimax of children if not leaf
                if cur_node.score == 0:
                    score_chosen = 0
                    for child in cur_node.children:
                        if abs(child.score) > abs(score_chosen):
                            score_chosen = child.score
                    cur_node.score = score_chosen

                # print('depth: ', depth, ' | ', child_move.board)
                # print(child_move.change, '| score: ', child_move.score)

    def get_move(self):
        best_move = (-1, -1)
        best_score = 0
        for child in self.root.children:
            if child.score > best_score:
                best_score = child.score
                best_move = child.change
        return best_move

    def clear_tree(self):
        self.root = None


boards = [[
    # a board that is one move away from winning for p1
    [0, 2,  -2, 0, 0,  0],
    [0,  0, -3,  -1,  0,  0],
    [0,  0,  0,  0,  0, 0],
    [0,  0,  0,  0,  2, 0],
    [0,  0,  0,  2,  0, 0]
],
    # a board that is one move away from winning for p2
    [
    [0, -2, 2, 0, 0,  0],
    [0,  0,  3,  1,  0,  0],
    [0,  0,  -1,  0,  0, 0],
    [0,  0,  0,  0, -2, 0],
    [0,  0,  0,  -2,  0, 0]
],
    # a board where p1 places piece in any corner will guarantee a win for p2 (p1 must avoid corners)
    [
    [0, 0,  0,  0,  0,  0],
    [-1, 0,  0,  0,  0,  -1],
    [-2, 3,  3,  3,  3, -2],
    [-1, 0,  0,  0,  0, -1],
    [0,  0,  -2,  -1,  0,  0]
],
    # a board where p2 places piece in any corner will guarantee a win for p1 (p2 must avoid corners)
    [
    [0, 0,  0,  0,  0,  0],
    [1, 0,  0,  0,  0,  1],
    [2, -3,  -3,  -3,  -3, 2],
    [1, 0,  0,  0,  0, 1],
    [0,  0,  2,  1,  0,  0]
]

]

tree = GameTree(boards[0], 1)
(row, col) = tree.get_move()
print('move:', row, col)
print(tree.root.children[0].change)
print(tree.root.children[0].board)
print(tree.root.children[0].score)
print(tree.root.children[1].change)
print(tree.root.children[1].board)
print(tree.root.children[1].score)

# tree = GameTree(boards[1], -1)
# (row, col) = tree.get_move()
# print('move:', row, col)

# tree = GameTree(boards[3], -1)
# (row, col) = tree.get_move()
# print('move:', row, col)

# print(tree.root.children[0].change)
# print(tree.root.children[0].board)
# print(tree.root.children[0].score)

# print('children')
# for child in tree.root.children[0].children:
#     print(child.depth, child.change, child.score)
    # if child.score == 180:
    #     print(child.depth)
    #     print(child.change)
    #     print(child.board)
    #     print(child.score)
# print(tree.root.children[1].change)
# print(tree.root.children[1].board)
# print(tree.root.children[1].score)
# print(tree.root.children[3].change)
# print(tree.root.children[3].board)
# print(tree.root.children[3].score)
