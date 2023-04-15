def rotate90(grid):
    return list(zip(*grid[::-1]))

def print2DGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], end='')

        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

gridRotated = rotate90(grid)
print2DGrid(gridRotated)
