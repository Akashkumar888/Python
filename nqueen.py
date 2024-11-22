

class Solution:
    def isSafe(self, row, col, n, board):
        # Check the column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i =i- 1
            j =j- 1
        
        # Check the anti-diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i =i- 1
            j =j+ 1
        
        return True

    def solve(self, row, n, board, result):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        
        for col in range(n):
            if self.isSafe(row, col, n, board):
                board[row][col] = 'Q'
                self.solve(row + 1, n, board, result)
                board[row][col] = '.'  # Backtrack

    def solveNQueens(self, n):
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]  # Create an empty n x n board
        self.solve(0, n, board, result)
        return result


# Directly solve for 4-Queens problem
if __name__ == "__main__":
    n = 4  # Set n directly to 4 for the 4-Queens problem
    solution = Solution()
    results = solution.solveNQueens(n)
    
    for i, solution in enumerate(results, start=1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

