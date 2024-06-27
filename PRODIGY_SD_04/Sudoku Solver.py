def is_valid(grid, row, col, num):
  # Check row
  for x in range(6):
    if grid[row][x] == num:
      return False

  # Check column
  for x in range(6):
    if grid[x][col] == num:
      return False

  # Check 3x2 subgrid
  start_row = row - row % 3
  start_col = col - col % 2
  for i in range(3):
    for j in range(2):
      if grid[i + start_row][j + start_col] == num:
        return False

  return True

def find_empty_location(grid):
  for row in range(6):
    for col in range(6):
      if grid[row][col] == 0:
        return row, col
  return None

def solve_sudoku(grid):
  find = find_empty_location(grid)
  if not find:
    return True
  row, col = find

  for num in range(1, 7):
    if is_valid(grid, row, col, num):
      grid[row][col] = num

      if solve_sudoku(grid):
        return True

      grid[row][col] = 0  # Backtrack

  return False

grid =[
     [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0],
    [0, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 0],
    [4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5]
    ]

if solve_sudoku(grid):
  for row in grid:
    print(row)
else:
  print("No solution exists.")
