"""
Input - an undirected graph. Find any cycle in this graph.

The first line contains two integers n (1≤n≤500) and m, the number of vertices and edges in the graph.
The next m lines contain two numbers each: the vertices of the beginning and end of the edge.
It is guaranteed that there are no loops and multiple edges in the graph.

Output any cycle as a sequence of vertices. It is guaranteed that there is at least one cycle in the graph.

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
3 4 1
"""


graph = []
color = {}
with open('TEST1.txt') as f:
    v_number, e_number = [int(i) for i in f.readline().strip().split()]
    for i in range(e_number):
        cur_v, cur_e = [int(i) for i in f.readline().strip().split()]
        graph.append([cur_v, cur_e])
        color[cur_v] = 'white'
        color[cur_e] = 'white'
for v in range(1, v_number + 1):
    if v not in color:
        color[v] = 'white'


def dfs(v):
    cycle.append(v)
    color[v] = 'grey'
    for comp in graph:
        if v in comp and (len(cycle) < 2 or set(comp) != {v, cycle[-2]}):
            e = comp[0] if v == comp[1] else comp[1]
            if color[e] == 'white':
                dfs(e)
            if color[e] == 'grey':
                for v in color:
                    color[v] = 'black'
                for i in cycle[::-1]:
                    if i != e:
                        print(i, end=' ')
                    else:
                        print(i)
                        break
    color[v] = 'black'
    cycle.pop()


cycle = []
for v in color:
    if color[v] == 'white':
        dfs(v)
