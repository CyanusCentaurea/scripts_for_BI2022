"""
The input is two sequences x and y. Print the global alignment of these sequences using +1 for matches,
-1 for mismatches, and -2 for gaps.

Print the sequences on separate lines, using the "-" sign for spaces.

Sample input:
GATT
GCATG

Sample output:
G-ATT
GCATG
"""
x = input()
y = input()


def LCS(x, y):
    m = len(x) + 1
    n = len(y) + 1
    lcs = [[0] * n for _ in range(m)]
    lcs[0] = [i * -2 for i in range(n)]
    k = 0
    for row in lcs:
        row[0] += k
        k -= 2
    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                if lcs[i - 1][j - 1] - 1 >= lcs[i - 1][j] - 2 and lcs[i - 1][j - 1] - 1 >= lcs[i][j - 1] - 2:
                    lcs[i][j] = lcs[i - 1][j - 1] - 1
                elif lcs[i - 1][j] >= lcs[i][j - 1]:
                    lcs[i][j] = lcs[i - 1][j] - 2
                elif lcs[i][j - 1] >= lcs[i - 1][j]:
                    lcs[i][j] = lcs[i][j - 1] - 2
    i = m - 1
    j = n - 1
    ansx = ''
    ansy = ''
    while i != 0 or j != 0:
        if lcs[i][j] == lcs[i - 1][j - 1] - 1 and x[i - 1] != y[j - 1] or lcs[i][j] == lcs[i - 1][j - 1] + 1 and x[i - 1] == y[j - 1]:
            ansx += x[i - 1]
            ansy += y[j - 1]
            i -= 1
            j -= 1
        elif lcs[i][j] == lcs[i - 1][j] - 2:
            ansx += x[i - 1]
            ansy += '-'
            i -= 1
        elif lcs[i][j] == lcs[i][j - 1] - 2:
            ansx += '-'
            ansy += y[j - 1]
            j -= 1
    return [ansx[::-1], ansy[::-1]]


print(*LCS(x, y), sep='\n')
