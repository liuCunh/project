# 栈的深度有限搜索(回溯法)
# 1表示墙，0表示可以走的路
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


def maze_path(x1, y1, x2, y2):  # x1,y1表示起点位置，x2,y2表示终点位置
    stack = []  # 用栈模式存储走过的位置
    stack.append((x1, y1))
    while len(stack) > 0:
        curNode = stack[-1]  # 当前所在位置

        # 对路径进行输出
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            for i in maze:
                print(i)
            return True

        # x,y想四个方向行走
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])  # 下一步要走的节点

            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)  # 将满足条件的节点加入栈
                maze[nextNode[0]][nextNode[1]] = 2  # 标识已经走过的路程
                break
        else:
            maze[curNode[0]][curNode[1]] = 2
            stack.pop()
    else:
        print("没找到")
        return False


maze_path(1, 1, 8, 8)
