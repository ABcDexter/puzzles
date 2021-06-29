import sys

# Below lists detail all eight possible movements for a knight.
row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]

# total number of possible solutions
count = 0


def isValid(x, y, char):
    """
    Check if `(x, y)` is valid chessboard coordinates.
    Note that a knight cannot go out of the chessboard
    """
    check1 = not (x < 0 or y < 0 or x >= N or y >= N)
    if check1:
        check2 = grid[x][y] == char
        # if check2:
        #    print(check1, check2, grid[x][y], char)
        return check1 and check2
    return False


# Recursive function to perform the knight's tour using backtracking
def knightTour(visited, x, y, string):
    # mark the current square as visited
    # print("currn string", string, "len: ", len(string))
    visited[x][y] = True

    # if the length of remaining search string is 0, print the solution
    if len(string) <= 1:
        # for r in visited:
        #    print(r)
        # print()
        # backtrack before returning
        visited[x][y] = 0  # mark this as not visited
        global count
        count += 1
        return

    # check for all eight possible movements for a knight
    # and recur for each valid movement
    for k in range(8):

        # get the new position of the knight from the current
        # position on the chessboard
        newX = x + row[k]
        newY = y + col[k]

        # if the new position is valid and not visited yet
        if isValid(newX, newY, string[1]) and visited[newX][newY] == 0:
            # print(newX, newY)
            knightTour(visited, newX, newY, string[1:])

    # backtrack from the current square and remove it from the current path
    visited[x][y] = 0


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.rstrip('\n') for line in f]

    search_string = sys.argv[2]

    print(search_string)
    global grid
    grid = lines
    N = len(grid)
    M = len(grid[0])

    print("dims of grid", N, M)
    for i in range(N):
        for j in range(M):
            print(grid[i][j], end='')
        print()



    # visited serves two purposes:
    # 1. It keeps track of squares involved in the knight's tour.
    # 2. It stores the order in which the squares are visited.
    pos = 1

    for i in range(N):
        for j in range(N):
            visited = [[0 for x in range(N)] for y in range(N)]
            # start knight tour from the square `(i, j)`

            if grid[i][j] == search_string[0]:
                knightTour(visited, i, j, search_string )

    print("total count 0,0 : ", count)
