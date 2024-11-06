import tkinter as tk
from tkinter import messagebox

# Sudoku Solver using Backtracking Algorithm
def is_valid(board, row, col, num):
    # Check if num is not in the current row
    for c in range(9):
        if board[row][c] == num:
            return False
    # Check if num is not in the current column
    for r in range(9):
        if board[r][col] == num:
            return False
    # Check if num is not in the current 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True  # All cells filled correctly

# Function to extract the board from the Tkinter grid
def extract_board(entries):
    board = []
    for row in range(9):
        current_row = []
        for col in range(9):
            value = entries[row][col].get()
            if value == "":
                current_row.append(0)  # Empty cell
            else:
                try:
                    current_row.append(int(value))
                except ValueError:
                    current_row.append(0)  # Invalid input, treat as empty
        board.append(current_row)
    return board

# Function to update the Tkinter grid with the solved board
def update_grid(entries, solved_board):
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].insert(tk.END, solved_board[row][col] if solved_board[row][col] != 0 else "")

# Tkinter GUI for Sudoku Solver
class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.entries = [[None for _ in range(9)] for _ in range(9)]

        # Create a 9x9 grid of Entry widgets
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=("Arial", 18), justify="center", bd=2, relief="solid")
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.entries[row][col] = entry

        # Solve Button
        solve_button = tk.Button(self.root, text="Solve", font=("Arial", 16), command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9, pady=20)

    def solve(self):
        # Extract the current puzzle from the Tkinter grid
        board = extract_board(self.entries)

        # Solve the puzzle using backtracking
        if solve_sudoku(board):
            # Update the grid with the solved puzzle
            update_grid(self.entries, board)
        else:
            # If no solution is found, show an error message
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle.")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
