"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    no_of_O = 0
    no_of_X = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == O:
                no_of_O += 1
            if board[row][col] == X:
                no_of_X += 1

    if no_of_X > no_of_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Not a valid option")

    row, col = action
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check for rows
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != EMPTY:
            return board[row][0]

    # check for columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # check for diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def max_value(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v


def min_value(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    for action in actions(board):
        if player(board) == X:
            if max_value(board) == min_value(result(board, action)):
                return action
        else:
            if min_value(board) == max_value(result(board, action)):
                return action
