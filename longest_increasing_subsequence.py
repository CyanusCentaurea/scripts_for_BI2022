"""Find the largest increasing subsequence in an array of n numbers.
Subsequences of length k consist of array elements at positions i_1, i_2,…,i_k, where 1≤i_1<i_2<…<i_k≤n is an increasing
sequence of indices.
Output in ascending order the indices of this subsequence in the original array (index numbering starts from 1).

The input is n numbers (1≤n≤1000) от -10^6−10^6.

There may be several correct answers, print any of them. In the example, the answer 2 5 7 is also correct.

Sample Input:
5 -1 4 3 2 6 3

Sample Output:
2 3 6
"""
a = [int(i) for i in input().split()]


def lis(a):
    n = len(a)
    dp = [1] * n
    prev = [-1] * n
    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    length = max(dp)
    last = dp.index(length)
    ans = []
    while last != -1:
        ans.append(last + 1)
        last = prev[last]
    # return length
    return ans[::-1]


print(*lis(a))
