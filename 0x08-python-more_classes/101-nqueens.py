#!/usr/bin/python3
import sys


class Solution:
    def solveNQueens(self, n):
        board = []
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()
        res = []

        def backtrack(row):
            if row == n:
                res.append([[row, col] for row, col in board])
                return

            for col in range(n):
                if col in cols or row + col in pos_diagonal or row - col in neg_diagonal:
                    continue

                board.append([row, col])
                pos_diagonal.add(row + col)
                neg_diagonal.add(row - col)
                cols.add(col)

                backtrack(row + 1)

                board.pop()
                pos_diagonal.discard(row + col)
                neg_diagonal.discard(row - col)
                cols.discard(col)

        backtrack(0)

        return res


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

    solution = Solution()

    n = int(sys.argv[1])
    res = solution.solveNQueens(n)

    for solution in res:
        print(solution)
