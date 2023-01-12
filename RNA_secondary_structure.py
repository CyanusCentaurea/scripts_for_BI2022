"""
The input is an RNA sequence.
Output the maximum number of paired bases in the optimal secondary structure without intersections.

Sample Input 1:
GCUGAUGGCAU

Sample Output 1:
4
"""
x = input()


def rna_secondary_structure(x):
    matrix = [[0 for j in range(len(x))] for i in range(len(x))]
    q = 1
    j = 0
    # moving diagonally
    while True:
        i = -1
        j = i + q + 1
        while j < len(x) - 1:
            i += 1
            j += 1
            matrix[i][j] = max(
                matrix[i + 1][j - 1] + 1 if {x[i], x[j]} == {'A', 'U'} or {x[i], x[j]} == {'G', 'C'} else matrix[i + 1][j - 1],
                max([matrix[i][k] + matrix[k + 1][j] for k in range(i, j)]))
        q += 1
        if i == 0 and j == len(x) - 1:
            for i in range(len(x)):
                for j in range(len(x)):
                    print(matrix[i][j], end=' ')
                print()
            break
    return matrix[0][len(x) - 1]


print(rna_secondary_structure(x))


