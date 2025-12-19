import numpy as np

class MineGrid:
    def __init__(self, rows=8, cols=8, num_mines=10):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = np.zeros((rows, cols), dtype=int)
        self.revealed = np.zeros((rows, cols), dtype=bool)
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        # mayın yerleştirme
        pass

    def _calculate_numbers(self):
        # sayı hesaplama
        pass

    def open_cell(self, row, col):
        pass

    def print_grid(self, reveal_all=False):
        pass
