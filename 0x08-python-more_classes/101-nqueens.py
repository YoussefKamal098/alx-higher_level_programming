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
    The N-Queens problem involves placing N queens on an N x N
    chessboard in such a way that no two queens threaten each other.

    Attributes:
        __n (int): The size of the chessboard and the number of queens.
        __solution (List[List[int]]): A list to store possible solution,
        where each solution is represented by a list of queen positions.
        __cols (set): A set to track occupied columns.
        __pos_diagonal (set): A set to track occupied positive diagonals.
        __neg_diagonal (set): A set to track occupied negative diagonals.
        __solutions (List[List[List[int]]]):A list to store all possible
        solutions.

    Methods:
        __init__(self, n): Initializes the SolveNQueens object.
        __solve(self): Solves the N-Queens problem using backtracking.
        __backtrack(self, row): Recursive backtracking function to find
        solutions.
    """

    def __init__(self, n=4):
        """
        Initialize the SolveNQueens object.

        Args:
            n (int): The size of the chessboard and the number of queens.
        """

        if type(n) is not int:
            raise TypeError("N must be integer")
        if n < 4:
            raise ValueError("N must be at least 4")

        self.__n = n
        self.__solution = []
        self.__solutions = []
        self.__cols = set()
        self.__pos_diagonal = set()
        self.__neg_diagonal = set()

    def solve(self):
        """
        Solve the N-Queens problem using backtracking.

        Returns:
            List[List[List[int]]]: A list of solutions,
            where each solution is represented
            by a list of queen positions.
        """
        self.__backtrack(0)

        return self.__solutions

    def __backtrack(self, row):
        """
        Recursive backtracking function to find solutions.

        Args:
            row (int): The current row being explored.
        """

        if type(row) is not int:
            raise TypeError("row must be integer")
        if row < 0:
            raise ValueError("row must be positive")

        if row == self.__n:
            self.__solutions.append([
                [row, col] for row, col in self.__solution
            ])
            return

        for col in range(self.__n):
            if (col in self.__cols or
                    (row + col) in self.__pos_diagonal or
                    (row - col) in self.__neg_diagonal):
                continue

            self.__solution.append([row, col])
            self.__pos_diagonal.add(row + col)
            self.__neg_diagonal.add(row - col)
            self.__cols.add(col)

            self.__backtrack(row + 1)

            self.__solution.pop()
            self.__pos_diagonal.discard(row + col)
            self.__neg_diagonal.discard(row - col)
            self.__cols.discard(col)


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
    solution = SolveNQueens(n)

    solutions = solution.solve()
    for solution in solutions:
        print(solution)
