#!/usr/bin/env python3
""" Nqueens solutuon module """
import sys


def print_usage():
    """ prints how to use the module """
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """Ensure correct number of arguments"""
    if len(sys.argv) != 2:
        print_usage()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def solve_nqueens(N):
    """ solves nqueen """
    solutions = []

    def is_safe(board, row, col):
        """ checks if  a square in board is safe"""
        for i in range(row):
            if board[i] == col or board[i] - i \
               == col - row or board[i] + i == col + row:
                return False
        return True

    def place_queens(board, row):
        """ places queen on the board """
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(board, row + 1)
                board[row] = -1

    board = [-1] * N
    place_queens(board, 0)
    return solutions


def main():
    """ main func """
    N = validate_input()
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
