
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        print_board(board)
        return True
    
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            res = solve_n_queens_util(board, row + 1, n) or res
            board[row][col] = False
    return res

def solve_n_queens(n):
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")
    else:
        print(f"Solutions for {n}-Queens problem are displayed above.")

# Simulate 4-Queen and 8-Queen problems
print("4-Queen Problem:")
solve_n_queens(4)
print("8-Queen Problem:")
solve_n_queens(8)

