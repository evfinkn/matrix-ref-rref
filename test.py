from fractions import Fraction
from rref import rref  # no need to test ref since ref has to work for rref to work

example1 = [[3, -2, 14],
            [1, 3, 1]]
solution1 = [[1, 0, 4],
             [0, 1, -1]]

example2 = [[-2, 1, -3],
            [1, -4, -2]]
solution2 = [[1, 0, 2],
             [0, 1, 1]]

example3 = [[3, -6, -9],
            [-2, -2, 12]]
solution3 = [[1, 0, -5],
             [0, 1, -1]]

example4 = [[3, 1, -2, 2],
            [1, -2, 1, 3],
            [2, -1, -3, 3]]
solution4 = [[1, 0, 0, 1],
             [0, 1, 0, -1],
             [0, 0, 1, 0]]

example5 = [[3, 1, -2, -7],
            [2, 2, 1, 9],
            [-1, -1, 3, 6]]
solution5 = [[1, 0, 0, -2],
             [0, 1, 0, 5],
             [0, 0, 1, 3]]

example6 = [[1, 3, 6, 9],
            [8, 3, 1, 7],
            [0, 1, 1, 1]]
solution6 = [[1, 0, 0, "12/13"],
             [0, 1, 0, "-9/13"],
             [0, 0, 1, "22/13"]]

example7 = [[10, 44, 0, 2, 7],
            [9, 8, 8, 3, 1],
            [50, 12, 7, 0, 0],
            [1, 10, 0, 0, 27]]
solution7 = [[1, 0, 0, 0, "-12889/3918"],
             [0, 1, 0, 0, "23735/7836"],
             [0, 0, 1, 0, "35860/1959"],
             [0, 0, 0, 1, "-182927/3918"]]

example8 = []
solution8 = []

example9 = [[]]
solution9 = [[]]

example10 = [[0]]
solution10 = [[0]]

example11 = [[5]]
solution11 = [[1]]

examples = [example1, example2, example3, example4, example5, example6, example7, example8, example9, example10, example11]
solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8, solution9, solution10, solution11]

for matrix in examples:
    for mr in matrix:
        mr[:] = map(Fraction, mr)

for matrix in solutions:
    for mr in matrix:
        mr[:] = map(Fraction, mr)

for example, solution in zip(examples, solutions):
    if (rref_matrix := rref(example)) != solution:
        print("failed\nrref:")
        print(rref_matrix)
        print("\nsolution:")
        print(solution)
        exit(1)

print("All tests passed successfully.")
