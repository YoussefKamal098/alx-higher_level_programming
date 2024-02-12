#!/usr/bin/python3
"""
N-Queens Solver

This script provides a solution to the N-Queens problem,
which involves placing N queens on an N x N chessboard
in such a way that no two queens threaten each other.

Usage:
    python script_name.py N

    - N: The size of the chessboard and the number of queens.

Example:
    python script_name.py 8
"""
import sys


class SolveNQueens:
    """
    SolveNQueens Class

    A class that provides a solution to the N-Queens problem.
    The N-Queens problem involves placing N queens on an N x N chessboard
    in such a way that no two queens threaten each other.

    Attributes:
        __n (int): The default size of the chessboard and the number of queens.
        __solution (List): A list to store the current solution.
        __solutions (List[List[List[int]]]): A list to store all solutions.
        __cols (set): A set to track occupied columns.
        __pos_diagonal (set): A set to track occupied positive diagonals.
        __neg_diagonal (set): A set to track occupied negative diagonals.

    Methods:
        solve(cls, n): Solves the N-Queens problem for a given
        size of the chessboard.
        __backtrack(cls, row, n): Recursive backtracking function
        to find solutions.
    """
    __n = 4
    __solution = []
    __solutions = []
    __cols = set()
    __pos_diagonal = set()
    __neg_diagonal = set()

    @classmethod
    def solve(cls, n=4):
        """
        Solve the N-Queens problem for a given size of the chessboard.

        Args:
            n (int): The size of the chessboard and the number of queens.

        Returns:
            List[List[List[int]]]: A list of solutions, where each solution
            is represented by a list of queen positions.
        """
        if type(n) is not int:
            raise TypeError("N must be a integer")
        if n < 4:
            raise ValueError("N must be at least 4")

        cls.__backtrack(0, n)

        return cls.__solutions

    @classmethod
    def __backtrack(cls, row, n):
        """
        Recursive backtracking function to find solutions.

        Args:
            row (int): The current row being explored.
            n (int): The size of the chessboard and the number of queens.
        """
        if type(row) is not int:
            raise TypeError("row must be integer")
        if row < 0:
            raise ValueError("row must be positive")

        if type(n) is not int:
            raise TypeError("N must be a integer")
        if n < 4:
            raise ValueError("N must be at least 4")

        if row == n:
            cls.__solutions.append([
                [row, col] for row, col in cls.__solution
            ])
            return

        for col in range(n):
            if (col in cls.__cols or
                    (row + col) in cls.__pos_diagonal or
                    (row - col) in cls.__neg_diagonal):
                continue

            cls.__solution.append([row, col])
            cls.__pos_diagonal.add(row + col)
            cls.__neg_diagonal.add(row - col)
            cls.__cols.add(col)

            cls.__backtrack(row + 1, n)

            cls.__solution.pop()
            cls.__pos_diagonal.discard(row + col)
            cls.__neg_diagonal.discard(row - col)
            cls.__cols.discard(col)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    solutions = SolveNQueens.solve(n)

    for solution in solutions:
        print(solution)
