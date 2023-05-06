import time

from sudoku_solver import SudokuSolver

if __name__ == "__main__":
    board_size = int(input("Enter size of your board: "))
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    c = int(input("Number of lines:"))
    while c:
        input_line_split = input("").split()
        i, j, val = int(input_line_split[0]), int(input_line_split[1]), int(input_line_split[2])
        board[i][j] = val
        c -= 1

    sudoku_solver = SudokuSolver(game_board=board, size=board_size)
    print("Initial Board:")
    sudoku_solver.print_sudoku_board()

    start_time = time.time()
    if sudoku_solver.solve_sudoku():
        print("Solution:")
        sudoku_solver.print_sudoku_board()
    else:
        print("Unsolvable CSP!")
    end_time = time.time()
    print("Elapsed time: ", end_time-start_time)