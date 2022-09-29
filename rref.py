import argparse
import json
from fractions import Fraction
import operator


def print_matrix(matrix, prec=3):
    # pretty print the matrix
    string = "["
    if len(matrix) != 0:
        # take float because Fraction doesn't use the :.xf formatting
        values = [[f"{float(value):.{prec}f}" for value in row] for row in matrix]
        # get the maximum string length to pad each value equally
        maxlen = max([len(values[x][y]) for x in range(len(matrix)) for y in range(len(matrix[0]))])
        for x in range(len(values)):
            string += "["
            for y in range(len(values[x])):
                string += f"{values[x][y]: >{maxlen}}, "
            string += f"\b\b]"  # remove the last comma and add the closing bracket
            if x != len(values) - 1:  # there's another row, so add a new line
                string += "\n "
    string += "]"
    print(string)


def ref(matrix, subm = 0):
    # subm is used for recurion, it's the row and column number of the submatrix

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    if len(matrix) - subm <= 1 or len(matrix[0]) - subm <= 1:
        return matrix

    # handle case where entry being looked at is 0 and case where entire column is 0
    if matrix[subm][subm] == 0:
        for i in range(subm + 1, len(matrix)):
            if matrix[i][subm] != 0:
                matrix[subm], matrix[i] = matrix[i], matrix[subm]  # swap rows
                break
        else:  # if for loop never breaks (column is all zeros)
            return ref(matrix, subm + 1)

    # get zeros in entries below current leading entry
    for i in range(subm + 1, len(matrix)):
        # usage of map for operations on lists from https://stackoverflow.com/a/534914/18413833
        # faster than using list comprehension
        row_multiple = map((matrix[i][subm] / matrix[subm][subm]).__mul__, matrix[subm])
        matrix[i][:] = map(operator.sub, matrix[i], row_multiple)

    # repeat with next row and column
    return ref(matrix, subm + 1)


def rref(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    ref(matrix)  # reuse instead of rewriting to integrate code below

    for i in range(len(matrix)):
        if matrix[i][i] != 1 and matrix[i][i] != 0:  # all leading entries need to be 1 for rref
            matrix[i][:] = map(matrix[i][i].__rtruediv__, matrix[i])
        for j in range(0, i):  # subtract current row from rows above it to get 0 in the entire column
            row_multiple = map(matrix[j][i].__mul__, matrix[i])
            matrix[j][:] = map(operator.sub, matrix[j], row_multiple)

    return matrix


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates the row echelon form / reduced row echelon form of a "
                                                 "matrix.")
    parser.add_argument("matrix",
                        nargs="+",
                        help="the string representing the matrix to find the ref / rref of. Must be a valid JSON "
                             "string of an array of arrays of numbers. For example: \"[[1, 2, 3], [4, 5, 6]]\". Make "
                             "sure to enclose the array in quotes.")
    parser.add_argument("-m", "--mode",
                        default="rref",
                        choices=["ref", "rref"],
                        help="the form to calculate. ref for row echelon form, rref for reduced row echelon "
                             "form (default: %(default)s)")
    parser.add_argument("-p", "--precision",
                        default=3,
                        type=int,
                        help="the number of digits after the decimal point to print (default: %(default)s)")

    args = parser.parse_args()

    for matrix in args.matrix:
        try:
            matrix = json.loads(matrix)
            if type(matrix) != list:
                print("Input matrix must be an array")
                exit(1)
            elif len(matrix) != 0 and type(matrix[0]) != list:
                print("Input matrix must be an array of arrays")
                exit(1)
            matrix = [[Fraction(value) for value in row] for row in matrix]
        except json.decoder.JSONDecodeError:
            print("Invalid JSON string input for the matrix.")
            exit(1)
        mode = args.mode
        precision = args.precision
        if mode == "ref":
            print_matrix(ref(matrix), precision)
        else:
            print_matrix(rref(matrix), precision)
