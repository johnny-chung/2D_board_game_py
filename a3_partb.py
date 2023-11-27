# Main Author:
# Main Reviewer:

# This function duplicates and returns the board. You may find this useful

from a3_parta import evaluate_board

def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height = 4):
            pass

    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)

    def get_move(self):
        height = len(self.board)
        width = len(self.board[0])
        if self.player == 1:
            return (0, 0)
        else:
            return (height-1, width-1)
   
    def clear_tree(self):
        pass     

    