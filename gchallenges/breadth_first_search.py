import copy
from collections import deque

def answer(maze):
    mazelengths = []
    # Only compare when a path is opened
    # that would be when when the 1 either has 0's above and below
    # or to the left and right
    mazelengths.append(bfsearch(maze, 0, 0))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            # Is a 1
            if maze[y][x]:
                # not on border
                if 0 < x < len(maze[0])-1:
                    # 0's on both sides
                    if maze[y][x-1] == maze[y][x+1] == 0:
                        maze[y][x] = 0
                        mazelengths.append(bfsearch(maze, 0, 0))
                        maze[y][x] = 1
                        
                if 0 < y < len(maze)-1:
                    if maze[y-1][x] == maze[y+1][x] == 0:
                        maze[y][x] = 0
                        mazelengths.append(bfsearch(maze, 0, 0))
                        maze[y][x] = 1
    # print(mazelengths)
    return min(mazelengths)
    
    
def bfsearch(maze, x, y):
    """
    Breadth First Search is an algorithm to find the shortest path from the
    source.  It utilizes a queue, by queueing all the adjacent nodes in a
    pattern, you are able to address the closest nodes first before moving
    on to further nodes.  
    Queues can be made in python with lists and pop[0]
    but is inefficient (all other list entries must be moved by 1).  A more
    efficient queue is the deque method from collections module.
    """
    mazecopy = copy.deepcopy(maze)
    mazecopy[y][x] = 1

    queue = deque([(x,y)])
    while queue != deque([]):
        x, y = queue.popleft()
        # print("x, y", (x, y))

        if x < len(maze[0])-1:
            if mazecopy[y][x+1] == 0: # if right is open go right
                # print("Going right")
                mazecopy[y][x+1] = mazecopy[y][x]+1
                queue.append((x+1,y))
        if y < len(maze)-1:
            if mazecopy[y+1][x] == 0:  # if down is open go down
                # print("Going down")
                mazecopy[y+1][x] = mazecopy[y][x]+1
                queue.append((x,y+1))
        if x:
            if mazecopy[y][x-1] == 0:  # if left is open go left
                # print("Going left")
                mazecopy[y][x-1] = mazecopy[y][x]+1
                queue.append((x-1,y))
        if y:
            if mazecopy[y-1][x] == 0:  # if up is open go up
                # print("Going up")
                mazecopy[y-1][x] = mazecopy[y][x]+1
                queue.append((x,y-1))

    # for row in mazecopy:
    #     print(row)
    if mazecopy[len(maze)-1][len(maze[0])-1]:
        return mazecopy[len(maze)-1][len(maze[0])-1]
    else:
        return len(maze)*len(maze[0])

maze1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
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
