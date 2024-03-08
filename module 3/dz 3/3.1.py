""" Пожалуйста, указывайте в задании размерности матриц или используйте разделители, 
    иначе невозможно однозначно определить её форму
"""
import numpy as np


def transpose(mtx):
    res = np.zeros((len(mtx[0]), len(mtx)), dtype=np.int16)

    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            res[j][i] = mtx[i][j]

    return res


if __name__ == '__main__':
    A = np.array([[1, 54, 1], [6, 2, 7]])
    B = np.array([[1, 7, 8], [4, 2, 9], [5, 6, 3]])
    C = transpose(A)
    D = transpose(B)

    for line in C:
        print(line)
    print()
    for line in D:
        print(line)
