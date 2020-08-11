'''
CTCI #1.8 Zero Matrix
'''

import unittest


def zero_matrix(mat):
    M = len(mat)
    N = len(mat[0])

    MArr = []  # rows
    NArr = []  # cols

    for x in range(M):
        for y in range(N):
            if mat[x][y] == 0:
                MArr.append(x)
                NArr.append(y)

    MSet = set(MArr)
    NSet = set(NArr)

    for i in MSet:
        for j in range(len(mat[0])):
            mat[i][j] = 0

    for k in NSet:
        for l in range(M):
            mat[l][k] = 0

    return mat



class Test(unittest.TestCase):
    '''Test Cases'''

    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
