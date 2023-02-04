import heapq
import math

# heapq 优先队列，常使用两个函数，heappop(队列) 按照某种顺序先后弹出队列；
# heappush(队列，元素) 给元素建立一个小根堆，添加到队列中

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}


def init_distance(graph, s):
    distance = {s: 0}

    # 源点跟目的点的距离默认为正无穷
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf  # 正无穷
    return distance


def dijkstra(graph, s):
    """
    :param graph: 图结构
    :param s: 起始点
    :return: 终点和到达终点所用的距离
    """

    pqueue = []
    heapq.heappush(pqueue, (0, s))  # 将点加入优先队列

    seen = set()  # 保存已经访问 过的点，避免重复 eg: a->b, b->a避免这种情况出现
    parent = {s: None}
    distance = init_distance(graph, s)  # 点到起始点的距离

    while len(pqueue) > 0:
        pari = heapq.heappop(pqueue)  # 弹出一个元组（到达下一个节点距离的大小，将要到达的节点）
        dist = pari[0]
        vertex = pari[1]
        seen.add(vertex)  # 记录已经访问过的点

        nodes = graph[vertex].keys()  # 获取下一步可走节点.

        # 遍历可走路径
        for w in nodes:

            # 查看以前路径是否走过
            if w not in seen:

                # 比较新路径跟原路径长短
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))  # 添加下一次循环点

                    parent[w] = vertex  # 更新最短路径的点
                    distance[w] = dist + graph[vertex][w]  # 更新到达最短路径的长度
    return parent, distance


parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)
