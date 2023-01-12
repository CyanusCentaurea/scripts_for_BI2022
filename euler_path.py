"""
Find an Euler cycle - a cycle that traverses each edge in the graph exactly once.

The first line contains two numbers n (1≤n≤1000) and m, the number of vertices and edges in the graph.
The next m lines contain two numbers each: the vertices of the beginning and end of the edge.

Print the Euler cycle as a sequence of vertices, each pair of neighbors in which is connected by an edge.
It is guaranteed that such a cycle exists in the graph.

Sample Input:
4 5
1 2
2 1
2 3
3 4
4 2

Sample Output:
1 2 3 4 2
"""

graph = {}
with open('TEST1.txt') as f:
    v_number, e_number = [int(i) for i in f.readline().strip().split()]
    for i in range(e_number):
        cur_v, cur_e = [int(i) for i in f.readline().strip().split()]
        if cur_v not in graph:
            graph[cur_v] = [cur_e]
        else:
            graph[cur_v].append(cur_e)


def euler(v):
    stack = [v]
    while stack:
        v = stack[-1]
        if not graph[v]:
            res.append(v)
            stack.pop()
        else:
            e = graph[v].pop()
            stack.append(e)
    res.reverse()
    return res


res = []
print(*euler(1)[:-1])
