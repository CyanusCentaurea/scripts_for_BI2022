"""
Solve one of the variations of the knapsack problem.
The input is no more than 1000 elements with different weights w_i, and an integer S.
Find the number of possible sets that can be formed from given elements with a weight not exceeding S.

The first line contains integers w_i separated by spaces.
The second line contains one integer S.
All input numbers do not exceed 1000.

Sample Input:
1 2 2 3 5
8

Sample Output:
23
"""
w = [int(i) for i in input().split()]
W = int(input())


def knapsack(w, W):
    n = len(w)
    W += 1
    n = n + 1
    dp = [[[0, 1]] * W for _ in range(n)]
    for i in range(1, n):
        for j in range(1, W):
            if j >= w[i - 1]:
                dp[i][j] = [max(dp[i - 1][j][0], dp[i - 1][j - w[i - 1]][0] + w[i - 1]), dp[i - 1][j][1] + dp[i - 1][j - w[i - 1]][1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n - 1][W - 1][1]


print(knapsack(w, W))
