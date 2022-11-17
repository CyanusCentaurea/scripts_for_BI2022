"""
The input is the cost matrix of size n×m, consisting of positive integers (2≤n, m≤1000, cost[1][1] = 0).
At the beginning, the chip is in the upper left corner (field (1,1)). At each step, the chip can be moved one cell to
the right or down. The cost of moving a chip to a cell with index (i,j) is cost[i][j].
Find the least cost path from cell (1,1) to cell (n,m).

sample input:
0 3 5
6 4 4

sample output:
11
"""
cost = []
rows = 0
while True:
    try:
        line = [[int(i), 0] for i in input().split()]
    except EOFError:
        break
    rows += 1
    cost.append(line)
cols = len(cost[0])


def cheap_way(cost, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i - 1 < 0:
                cost[i][j] = [cost[i][j][0], cost[i][j - 1][1] + cost[i][j][0]]
            elif j - 1 < 0:
                cost[i][j] = [cost[i][j][0], cost[i - 1][j][1] + cost[i][j][0]]
            else:
                cost[i][j] = [cost[i][j][0], min(cost[i - 1][j][1] + cost[i][j][0], cost[i][j - 1][1] + cost[i][j][0])]
    return cost[rows - 1][cols - 1][1]


print(cheap_way(cost, rows, cols))




