# character picture grid project from chapter 4

grid = [['.', '.', '.', '.', '.', '.',],
        ['.', '0', '0', '.', '.', '.',],
        ['0', '0', '0', '0', '.', '.',],
        ['0', '0', '0', '0', '0', '.',],
        ['.', '0', '0', '0', '0', '0',],
        ['0', '0', '0', '0', '0', '.',],
        ['0', '0', '0', '0', '.', '.',],
        ['.', '0', '0', '.', '.', '.',],
        ['.', '.', '.', '.', '.', '.',]]


z = 0                               # z is the iterable index of the sublists
for _ in range(len(grid[1])):
    for x in range(len(grid)):      # x is the iterable index of the main list
        print(grid[x][z], end='')   # printing 1st subelement of every element
    print("")                       # a new line
    z = z + 1                       # updating the index of the sublists
