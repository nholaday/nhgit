import copy

def answer(maze):
    """Checks if every node is 1.  If it is, change it to a 0 then test the
    maze, then take the smallest maze length.
    """
    mazelengths = [len(maze)**2]
    mazelengths.append(run_maze(maze, mazelengths))  # maze with no changes

    # Only run run_path() when a path is opened
    # that would be when when the 1 either has 0's above and below
    # or to the left and right
    for y in range(len(maze)):
        for x in range(len(maze)):
            # Is a 1
            if maze[y][x]:
                # not on border
                if 0 < x < len(maze)-1:
                    # 0's on both sides
                    print("not on x border")
                    print(x,y)
                    if maze[y][x-1] == maze[y][x+1] == 0:
                        maze[y][x] = 0
                        mazelengths.append(run_maze(maze, mazelengths))
                        print mazelengths
                        maze[y][x] = 1
                if 0 < y < len(maze)-1:
                    print("not on y border")
                    print(x,y)
                    if maze[y-1][x] == maze[y+1][x] == 0:
                        maze[y][x] = 0
                        mazelengths.append(run_maze(maze, mazelengths))
                        print mazelengths
                        maze[y][x] = 1
            # just return if it can't get any shorter
            if min(mazelengths) == len(maze)*2-1:
                return min(mazelengths)
    return min(mazelengths)

    
def run_maze(maze, lenlist):
    """Returns the shortest path to the end of the current maze
    """
    move(maze, 0, 0, 1, lenlist)
    for row in maze:
        print(row)
    return min(lenlist)

def move(maze, x, y, length, lenlist):
    """Uses recursion to solve maze. Start a maze at 0,0. 
    Create a copy of the maze with a 1 at current location
    Try moving right, down, left, up.
    If right is open start the new maze by excecuting move() at 1,0
    If down is open start the new maze by excecuting move() at 0,1, etc.
    If the end is reached store the length in lenlist
    """
    size = len(maze)-1
    mazecopy = copy.deepcopy(maze)
    # change current location to 1
    mazecopy[y][x] = 1

    # More faster: stop recursive searching past a length already found.
    if x < size and length <= min(lenlist):
        if not mazecopy[y][x+1]: # if right is open go right
            move(mazecopy, x+1, y, length+1, lenlist)
    if y < size and length <= min(lenlist):
        if not mazecopy[y+1][x]:  # if down is open go down
            move(mazecopy, x, y+1, length+1, lenlist)
    if x and length <= min(lenlist):
        if not mazecopy[y][x-1]:  # if left is open go left
            move(mazecopy, x-1, y, length+1, lenlist)
    if y and length <= min(lenlist):
        if not mazecopy[y-1][x]:  # if up is open go up
            move(mazecopy, x, y-1, length+1, lenlist)

    if x == y == size:
        lenlist.append(length)

maze1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
maze3 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


if __name__ == "__main__":
    #print(answer(maze1))
    #print(answer(maze2))
    print(answer(maze3))
