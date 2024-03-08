import numpy as np


def multiply(mtx1, mtx2):
    if mtx1.shape != mtx2.shape:
        print("Wrong dimensions")
        return
    return np.dot(mtx1, mtx2)


if __name__ == '__main__':
    A = np.array([[1, 2], [4, 5], [7, 8]])
    B = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    E = multiply(A, B)
    F = multiply(C, B)

    if isinstance(E, np.ndarray):
        for line in E:
            print(line)
    print()
    if isinstance(F, np.ndarray):
        for line in F:
            print(line)
