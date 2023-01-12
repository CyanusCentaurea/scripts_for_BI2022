"""
Input - an undirected graph.
Print all connected components of this graph using any graph traversal algorithm (DFS or BFS).

The first line contains two integers nn (1≤n≤500) and m, the number of vertices and edges in the graph.
The next m lines contain two numbers each: the vertices of the beginning and end of the edge.
A graph can have multiple edges and loops.

Output the connected components of this graph, one per line.
The order of the components and vertices within the components is not important.

Sample Input:
8 7
1 3
1 5
2 4
5 8
4 6
7 7
3 5

Sample Output:
2 4 6
7
1 3 5 8
"""

graph = []
visited = {}
with open('TEST1.txt') as f:
    v_number, e_number = [int(i) for i in f.readline().split()]
    for i in range(e_number):
        cur_v, cur_e = [int(i) for i in f.readline().split()]
        graph.append([cur_v, cur_e])
        visited[cur_v] = False
        visited[cur_e] = False
for v in range(1, v_number + 1):
    if v not in visited:
        visited[v] = False


def dfs(v):
    visited[v] = True
    res.add(v)
    for comp in graph:
        if v in comp:
            e = comp[0] if v == comp[1] else comp[1]
            res.add(e)
            if not visited[e]:
                dfs(e)


for v in visited:
    if not visited[v]:
        res = set()
        dfs(v)
        print(*res)
for v in visited:
    if not visited[v]:
        print(v)
