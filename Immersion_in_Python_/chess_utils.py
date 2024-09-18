def are_queens_safe(queens):
    """Проверяет, не бьют ли друг друга ферзи на шахматной доске."""
    rows = set()
    cols = set()
    diag1 = set() # Диагонали вида row - col
    diag2 = set() # Диагонали вида row + col

    for row, col in queens:
        if row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False
        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    return True