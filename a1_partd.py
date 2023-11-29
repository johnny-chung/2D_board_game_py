# copy over your a1_partd.py file here
# don't forget to update your overflow() function

#    Main Author(s): Wai Yin Chung
#    Main Reviewer(s):

from a1_partc import Queue


def get_overflow_list(grid):

    # check for None
    if grid is None:
        return None
    max_row_idx = len(grid) - 1
    max_col_idx = len(grid[0]) - 1

    # empty list to store the overflow coordinate
    overflow_list = []

    # loop through the entire grid
    for i in range(max_row_idx + 1):
        for j in range(max_col_idx + 1):
            # look for the no of neighbour, i.e. max value, base on coordinate
            max_value = (i > 0) + (i < max_row_idx) + \
                (j > 0) + (j < max_col_idx)

            if abs(grid[i][j]) >= max_value:
                overflow_list.append((i, j))

    # return overflow list if found, else return None
    if overflow_list:
        return overflow_list

    return None


def overflow(grid, a_queue):
    return overflow_recursive(grid, a_queue, 0)


def overflow_recursive(grid, a_queue, counter):

    # get the overflow cells cooridinate
    overflow_list = get_overflow_list(grid)

    # return counter? if the grid is of the same sign
    if check_sign_changed(grid) is False:
        a_queue.enqueue(deep_copy_2d_array(grid))
        return counter

    # base condition
    # if there the grid is not overflow, return the counter
    if overflow_list is None:
        return counter

    # get the sign of overflow cells
    sign = 1
    if grid[overflow_list[0][0]][overflow_list[0][1]] < 0:
        sign = -1

    # overflow cells become 0
    for of_cell in overflow_list:
        grid[of_cell[0]][of_cell[1]] = 0

    max_row_idx = len(grid) - 1
    max_col_idx = len(grid[0]) - 1
    # add 1 to abs of neighbour value and change sign
    for of_cell in overflow_list:
        neighbour_list = [(0 - (of_cell[0] > 0), 0), (0, 0 - (of_cell[1] > 0)),
                          ((of_cell[0] < max_row_idx), 0), (0, (of_cell[1] < max_col_idx))]
        for neighbour in neighbour_list:
            if neighbour[0] != 0 or neighbour[1] != 0:
                x = of_cell[0] + neighbour[0]
                y = of_cell[1] + neighbour[1]
                grid[x][y] = (abs(grid[x][y]) + 1) * sign

    # add the new grid to the queue
    a_queue.enqueue(deep_copy_2d_array(grid))

    # call function recursively, updating the counter
    return overflow_recursive(grid, a_queue, counter + 1)


# deep copy of 2d array
# arg: a 2d array
# return: a deep copy
def deep_copy_2d_array(org_array):
    # if the array received is not exist, return
    if org_array is None:
        return None

    # get the length of the 2d array
    row = len(org_array)
    col = len(org_array[0])

    res = []
    # traverse the 2d array to make a deep copy
    for i in range(row):
        a_row = []
        for j in range(col):
            a_row.append(org_array[i][j])
        res.append(a_row)
    return res

# check if all the value in the grid is of the same sign


def check_sign_changed(grid):
    max_row = len(grid)
    max_col = len(grid[0])
    # cnt the number of positive and negative number
    pos_cnt = neg_cnt = 0

    for i in range(max_row):
        for j in range(max_col):
            if grid[i][j] > 0:
                pos_cnt += 1
            elif grid[i][j] < 0:
                neg_cnt += 1
            # if there are both positive and negative number, mean the grid is not of the same sign, break
            if pos_cnt > 0 and neg_cnt > 0:
                return True
    return False
