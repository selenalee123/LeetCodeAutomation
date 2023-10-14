
"""
LeetCode Problem: 51. N-Queens
LeetCode Link: https://leetcode.com/problems/n-queens/submissions/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def solveNQueens(self, n):
        def is_valid(board, row, col):
            # Check if it's valid to place a queen at (row, col)
            for i in range(row):
                # Check if there's a queen in the same column
                if board[i][col] == "Q":
                    return False
                # Check if there's a queen in the left diagonal
                if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":
                    return False
                # Check if there's a queen in the right diagonal
                if col + (row - i) < n and board[i][col + (row - i)] == "Q":
                    return False
            return True

        def solve(row):
            if row == n:
                # If we've placed queens in all rows, it's a valid solution
                solutions.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_valid(board, row, col):
                    # Place a queen and recursively explore next row
                    board[row][col] = "Q"
                    solve(row + 1)
                    # Backtrack by removing the queen
                    board[row][col] = "."

        solutions = []  # To store the valid solutions
        board = [["." for _ in range(n)] for _ in range(n)]  # Initialize an empty board
        solve(0)  # Start solving from the first row
        return solutions

        
"""

# Test cases
# Add test cases to validate your solution
