tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(lst):
    z = 0
    for _ in range(len(tableData[0])):
        for x in range(len(tableData)):
            y = tableData[x][z]
            print(y.rjust(8, ' '), end=' ')
        print('')
        z = z + 1


print_table(tableData)

# this need to be tweaked. apparently the question expects me to decide column width depending on the longest word in it.
