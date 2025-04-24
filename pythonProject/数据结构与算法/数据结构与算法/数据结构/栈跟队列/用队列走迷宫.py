# 队列--广度优先搜索
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 走的方向
dirs = [
    lambda x, y:(x-1, y),
    lambda x, y:(x, y+1),
    lambda x, y:(x+1, y),
    lambda x, y:(x, y-1)
]


def print_r(path):
    curNode = path[-1]
    realpath = []

    # 走过的路径
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]

    realpath.append(curNode[0:2])  # 存储起点
    realpath.reverse()
    for node in realpath:
        # print(node)
        pass


def maze_path_queue(x1, y1, x2, y2):  # x1,y1迷宫起点；x2,y2迷宫终点
    queue = deque()  # 存储路径
    queue.append((x1, y1, -1))
    path = []  # 存储路径和上一个源点
    while len(queue) > 0:
        curNode = queue.pop()
        print(f'\033[31m{path}\033[0m')
        print(f'\033[31m{len(path)-1}\033[0m')
        path.append(curNode)

        # 输出路径
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True

        # 找路
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])

            # 下一步能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # 后续节点进队，记录上个节点
                maze[nextNode[0]][nextNode[1]] = 2  # 标识已走路径
    else:
        print('没有路')
        return False


maze_path_queue(1, 1, 8, 8)
