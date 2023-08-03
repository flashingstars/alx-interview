#!/usr/bin/python3
"""
N Queens placement on NxN chessboard
"""


import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check if there is a queen in the upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 'Q':
            return False
    
    return True


def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]


    def backtrack(row):
        if row == N:
            for i in range(N):
                print(' '.join(board[i]))
            print()
            return
        
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)