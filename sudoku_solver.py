class SudokuSolver:
    def __init__(self, game_board: list[list[int]], size: int = 9):
        self.board = game_board
        self.size = size

    def solve_sudoku(self) -> bool:
        """
        Solves the given Sudoku board using backtracking algorithm with forward checking.
        Returns True if solution exists, False otherwise. Works recursively!
        """
        row, col = self.find_empty_cell()
        if row is None or col is None:
            return False

        # If there are no empty locations left, solution is found
        if row == -1:
            return True

        for num in self.get_valid_values(row, col):
            self.board[row][col] = num
            # Recursively check if this leads to a valid solution
            if self.solve_sudoku():
                return True
            self.board[row][col] = 0  # Reset the number if it doesn't lead to a valid solution
        return False

    def find_empty_cell(self) -> (None, tuple[int, int]):
        """ Returns a cell with the best solution to choose and assign number. """
        # Find empty location to fill
        row, col = -1, -1
        min_remaining_values = self.size  # Initialize to max possible values

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    remaining_values = self.get_valid_values(i, j)
                    num_remaining_values = len(remaining_values)

                    if num_remaining_values <= min_remaining_values:
                        row, col = i, j
                        min_remaining_values = num_remaining_values

                    if num_remaining_values == 0:
                        return None, None
        return row, col

    def get_valid_values(self, row: int, col: int) -> list[int]:
        """
        Returns a list of remaining valid values for the given empty location in the board.
        First set all values, then delete invalid values from the set.
        """
        remaining_values = set(range(1, self.size+1))

        # Remove numbers already used in row
        row_values = set(self.board[row])
        remaining_values -= row_values

        # Remove numbers already used in column
        col_values = set(self.board[i][col] for i in range(self.size))
        remaining_values -= col_values

        # Remove numbers already used in sub-grid
        sqrt_n = int(self.size ** 0.5)
        row_start = (row // sqrt_n) * sqrt_n
        col_start = (col // sqrt_n) * sqrt_n
        for i in range(row_start, row_start + sqrt_n):
            for j in range(col_start, col_start + sqrt_n):
                remaining_values.discard(self.board[i][j])
        return list(remaining_values)

    def print_sudoku_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=" ")
            print()
