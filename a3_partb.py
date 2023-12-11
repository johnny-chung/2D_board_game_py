# Main Author: Wai Yin Chung
# Main Reviewer: Wai Tan Wong, Chi Cheung Cheung

# This function duplicates and returns the board. You may find this useful

from a1_partd import get_overflow_list, overflow
from a1_partc import Queue
from a3_parta import evaluate_board, winning_score_base
from heap import Heap

# given


def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board

# GameTree to store the possible moves and the score for each move


class GameTree:
    # store one of the possible move and it's corresponding info
    class Node:
        def __init__(self, board, depth, player, move=(-1, -1), tree_height=4):

            self.board = copy_board(board)
            # routine overflow operation from part a
            a_queue = Queue()
            if depth > 0 and overflow(self.board, a_queue) > 0:
                while a_queue:
                    self.board = a_queue.dequeue()            
            # store other parameter
            self.depth = depth
            self.player = player
            # store the change when compare to parent board, i.e. the move
            self.move = move
            self.score = 0

            # evulate the score if reach the max tree height
            if self.depth == tree_height - 1:
                self.score = evaluate_board(self.board, self.player)

            # children to store the moves
            self.children = Heap()

        # custom operator overload for comparison in heap
        def __lt__(self, other):
            return self.score < other.score

        def __gt__(self, other):
            return self.score > other.score

        def __le__(self, other):
            return self.score <= other.score

        def __ge__(self, other):
            return self.score >= other.score

        def __eq__(self, other):
            return self.score == other.score

        def __ne__(self, other):
            return self.score != other.score

    def __init__(self, board, player, tree_height=4):
        self.tree_height = tree_height
        self.player = player
        self.board = copy_board(board)
        print(tree_height)
        # store max row, col
        self.max_row = len(board)
        self.max_col = len(board[0])

        # store the winning score
        self.winning_score = winning_score_base * self.max_row * self.max_col

        # create a root
        self.root = GameTree.Node(board, 0, player, (-1, -1), tree_height)

        # generate the moves from root
        self.create_children(1, player, self.root)

    def create_children(self, child_depth, child_player, parent_node):

        # if reach tree_height, stop create
        if child_depth == self.tree_height:
            return

        # check if the current board is a winning one, if yes, stop create children
        if evaluate_board(parent_node.board, parent_node.player) == self.winning_score:
            parent_node.score = self.winning_score
            return

        # loop through the board and create possible moves
        for i in range(self.max_row):
            for j in range(self.max_col):

                # only cell with 0 or the same sign as player can add move
                if parent_node.board[i][j] * child_player >= 0:
                    child_board = copy_board(parent_node.board)
                    child_board[i][j] += child_player

                    # create new node
                    child_node = GameTree.Node(
                        child_board, child_depth, child_player, (i, j))
                    # call create children recursive for the newly created child
                    self.create_children(
                        child_depth + 1, child_player * -1, child_node)

                    # insert the children
                    parent_node.children.append_elem(child_node)

        # minimax using min heap and max heap
        if parent_node.depth % 2:
            parent_node.children.heapify_min()
        else:
            parent_node.children.heapify_max()

        # the root of the heap after heapify is the desire move
        if parent_node.score == 0:
            parent_node.score = parent_node.children.arr[0].score

    # get the desire move
    # the root of the heap after heapify is the desire move
    def get_move(self):
        return self.root.children.arr[0].move

    # clear the tree by assign it to None
    def clear_tree(self):
        self.clear_tree_rec(self.root)

    def clear_tree_rec(self, subtree):
        if subtree.children is None:
            return
        self.clear_tree_rec(subtree.children)
        subtree.children.arr.clear()


# =======================================
# self testing

# boards = [[
#     # a board that is one move away from winning for p1
#     [0, 2,  -2, 0, 0,  0],
#     [0,  0, -3,  -1,  0,  0],
#     [0,  0,  0,  0,  0, 0],
#     [0,  0,  0,  0,  2, 0],
#     [0,  0,  0,  2,  0, 0]
# ],
#     # a board that is one move away from winning for p2
#     [
#     [0, -2, 2, 0, 0,  0],
#     [0,  0,  3,  1,  0,  0],
#     [0,  0,  -1,  0,  0, 0],
#     [0,  0,  0,  0, -2, 0],
#     [0,  0,  0,  -2,  0, 0]
# ],
#     # a board where p1 places piece in any corner will guarantee a win for p2 (p1 must avoid corners)
#     [
#     [0, 0,  0,  0,  0,  0],
#     [-1, 0,  0,  0,  0,  -1],
#     [-2, 3,  3,  3,  3, -2],
#     [-1, 0,  0,  0,  0, -1],
#     [0,  0,  -2,  -1,  0,  0]
# ],
#     # a board where p2 places piece in any corner will guarantee a win for p1 (p2 must avoid corners)
#     [
#     [0, 0,  0,  0,  0,  0],
#     [1, 0,  0,  0,  0,  1],
#     [2, -3,  -3,  -3,  -3, 2],
#     [1, 0,  0,  0,  0, 1],
#     [0,  0,  2,  1,  0,  0]
# ], [
#     [1, 1,  1],
#     [-1, 0,  1],
#     [-1, -1, -1]
# ]

# ]

# # tree=GameTree(boards[4],1)

# # (row, col) = tree.get_move()
# # print('move:', row, col)

# tree = GameTree(boards[0], 1)
# (row, col) = tree.get_move()
# print('move:', row, col)
# # 0,1

# # print(tree.root.children.arr[0].move)
# # print(tree.root.children.arr[0].board)
# # print(tree.root.children.arr[0].score)
# # print(tree.root.children.arr[1].move)
# # print(tree.root.children.arr[1].board)
# # print(tree.root.children.arr[1].score)

# tree = GameTree(boards[1], -1)
# (row, col) = tree.get_move()
# print('move:', row, col)
# # 0, 1

# # print(tree.root.board)
# # print(tree.root.children.arr[0].move)
# # print(tree.root.children.arr[0].board)
# # print(tree.root.children.arr[0].score)

# # tree = GameTree(boards[3], -1)
# # (row, col) = tree.get_move()
# # print('move:', row, col)
# # not coner

# # print(tree.root.children.arr[0].move)
# # print(tree.root.children.arr[0].board)
# # print(tree.root.children.arr[0].score)

# # print('children')
# # for child in tree.root.children[0].children:
# #     print(child.depth, child.change, child.score)
# # if child.score == 180:
# #     print(child.depth)
# #     print(child.change)
# #     print(child.board)
# #     print(child.score)
# # print(tree.root.children[1].change)
# # print(tree.root.children[1].board)
# # print(tree.root.children[1].score)
# # print(tree.root.children[3].change)
# # print(tree.root.children[3].board)
# # print(tree.root.children[3].score)

# test_board = [[0, -3, 2, 0, 0,  0],
#               [0,  0,  3,  1,  0,  0],
#               [0,  0,  -1,  0,  0, 0],
#               [0,  0,  0,  0, -2, 0],
#               [0,  0,  0,  -2,  0, 0]]
# test_queue = Queue()
# overflow(test_board, test_queue)
# # while test_queue:
# #     print(test_queue.dequeue())
