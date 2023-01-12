"""
Input - a directed graph. Find the shortest path between vertices 1 and 2.

The first line contains two numbers nn (2≤n≤100) and m, the number of vertices and edges in the graph.
The next m lines contain two numbers each: the vertices of the beginning and end of the edge.

Output the shortest path from vertex 1 to vertex 2 as a sequence of vertices.
Neighboring vertices must be connected by an edge. It is guaranteed that vertex 2 is reachable from vertex 1.

Sample Input:
8 10
1 4
4 3
1 3
3 5
3 8
5 6
6 2
8 2
8 6
2 7

Sample Output:
1 3 8 2
"""

from collections import deque

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
dist = {v: [] for v in range(1, v_number + 1)}


def shortest_path(s):
    q = deque()
    dist[s] = [s]
    q.append(s)
    while q:
        v = q.popleft()
        for comp in graph:
            if comp[0] == v:
                e = comp[1]
                if dist[e] == []:
                    dist[e] = dist[v] + [e]
                    q.append(e)
    return dist


print(*shortest_path(1)[2])
