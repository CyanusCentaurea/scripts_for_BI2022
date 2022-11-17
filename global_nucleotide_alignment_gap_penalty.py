"""
The input is two sequences s and t, and two numbers open and cont.
Output the global alignment of these sequences, using +1 for matching characters, -1 for mismatching characters,
open for opening a skip and cont for continuing a skip.
The bottom line is that it is more biologically dangerous (reading frame) and less likely to have several gaps separately,
than several gaps in a row, so a large price is charged for opening a gap.

Sample Input 1:
CATCACTG
CACACG
-2 -1
Sample Output 1:
CATCACTG
CA-CAC-G

Sample Input 2:
CATCACTG
CACACG
-10 -1
Sample Output 2:
CATCACTG
CA--CACG
"""


x = input()
y = input()
open, cont = [int(i) for i in input().split()]


def LCS(x, y):
    m = len(x) + 1
    n = len(y) + 1
    main = [[0 for j in range(m)] for i in range(n)]
    vert = [[0 for j in range(m)] for i in range(n)]
    hor = [[0 for j in range(m)] for i in range(n)]

    vert[0] = [-1000000 for i in range(m)]
    for i in range(n):
        hor[i][0] = -1000000
    for i in range(m):
        if i == 0:
            continue
        if i == 1:
            main[0][i] = open + cont
        else:
            main[0][i] = main[0][i - 1] + cont
    for i in range(n):
        if i == 0:
            continue
        if i == 1:
            main[i][0] = open + cont
        else:
            main[i][0] = main[i - 1][0] + cont
    for i in range(n):
        if i == 0:
            continue
        if i == 1:
            vert[i][0] = open + cont
        else:
            vert[i][0] = vert[i - 1][0] + cont
    for i in range(m):
        if i == 0:
            continue
        if i == 1:
            hor[0][i] = open + cont
        else:
            hor[0][i] = hor[0][i - 1] + cont
    for i in range(1, n):
        for j in range(1, m):
            vert[i][j] = max(vert[i - 1][j] + cont, main[i - 1][j] + open + cont)
            hor[i][j] = max(hor[i][j - 1] + cont, main[i][j - 1] + open + cont)
            main[i][j] = max(main[i - 1][j - 1] + 1 if y[i - 1] == x[j - 1] else main[i - 1][j - 1] - 1, vert[i][j], hor[i][j])

    i = n - 1
    j = m - 1
    ans1 = ''
    ans2 = ''
    if max(main[i][j], vert[i][j], hor[i][j]) == hor[i][j]:
        status = 'hor'
    elif max(main[i][j], vert[i][j], hor[i][j]) == vert[i][j]:
        status = 'vert'
    else:
        status = 'main'
    while i != 0 or j != 0:
        if status == 'vert':
            if vert[i][j] == vert[i - 1][j] + cont:
                ans1 += '-'
                ans2 += y[i - 1]
                i -= 1
            elif main[i - 1][j] + open + cont:
                ans1 += '-'
                ans2 += y[i - 1]
                i -= 1
                status = 'main'
        elif status == 'hor':
            if hor[i][j] == hor[i][j - 1] + cont:
                ans1 += x[j - 1]
                ans2 += '-'
                j -= 1
            elif hor[i][j] == main[i][j - 1] + open + cont:
                ans1 += x[j - 1]
                ans2 += '-'
                j -= 1
                status = 'main'
        elif status == 'main':
            if main[i][j] == vert[i][j]:
                status = 'vert'
            elif main[i][j] == hor[i][j]:
                status = 'hor'
            elif main[i][j] == main[i - 1][j - 1] + 1 if y[i - 1] == x[j - 1] else main[i][j] == main[i - 1][j - 1] - 1:
                ans1 += x[j - 1]
                ans2 += y[i - 1]
                i -= 1
                j -= 1
    return [ans1[::-1], ans2[::-1]]


print(*LCS(x, y), sep='\n')
