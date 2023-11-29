# Main Author: Wai Yin Chung
# Main Reviewer:

winning_score_base = 7

# this function is your evaluation function for the board


def evaluate_board(board, player):
    max_row_idx = len(board) - 1
    max_col_idx = len(board[0]) - 1
    pos_total = neg_total = zero_total = 0

    # loop through all cell
    for i in range(max_row_idx + 1):
        for j in range(max_col_idx + 1):

            # add base score, num of neighbour to the current value of the cell
            num_neighbour = (i > 0) + (i < max_row_idx) + \
                (j > 0) + (j < max_col_idx)
            score = abs(board[i][j]) + num_neighbour

            # check if the neighbour cell is -1 from overflow, if true, deduct mark
            # to simplify, ignore edge case
            if i > 1 and i < max_row_idx and j > 1 and j < max_col_idx:
                neighbour_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                neighbour_of = False
                for neighbour in neighbour_list:
                    if board[i + neighbour[0]][j + neighbour[1]] == 3:
                        neighbour_of = True
                if neighbour_of:
                    score -= 4

            # positive add to player 1
            if board[i][j] > 0:
                pos_total += score
            # negative to player 2
            elif board[i][j] < 0:
                neg_total -= score
            # store score for zero, depends on player 1 or 2, will be added if not winning board in final return
            else:
                zero_total += score
    # max score for winning board
    max_score = winning_score_base * (max_row_idx + 1) * (max_col_idx + 1)

    # check winning board
    if neg_total == 0:
        return player * max_score
    if pos_total == 0:
        return player * -1 * max_score
    # if not winning, return the score
    return player * pos_total - player * abs(neg_total) + player * zero_total
